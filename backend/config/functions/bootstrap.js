"use strict";

const fs = require("fs");
const path = require("path");
const mime = require("mime-types");
const importSeedData = require("./import");

async function registerConditions() {

  const conditions = [
    {
      displayName: `Only access spain`,
      name: `condition-site-spain`,
      plugin: "admin",
      handler: (user) => {
        return { 'sites.uid': { $eq: 'solo-para-agentes-com' } };
      },
    },
    {
      displayName: `Only access LATAM`,
      name: `condition-latam`,
      plugin: "admin",
      handler: (user) => {
        return { 'sites.uid': { $in: ['solo-para-agentes-ar', 'solo-para-agentes-co', 'solo-para-agentes-mx'] } };
      },
    },
    {
      displayName: `Only access UK - CA - USA`,
      name: `condition-uk-ca-usa`,
      plugin: "admin",
      handler: (user) => {
        return { 'sites.uid': { $in: ['agents-connect', 'wheels-up-network-canada', 'wheels-up-network-usa'] } };
      },
    },
  ];

  await strapi.admin.services.permission.conditionProvider.registerMany(conditions);
}

async function isFirstRun() {
  const pluginStore = strapi.store({
    environment: strapi.config.environment,
    type: "type",
    name: "setup",
  });
  const initHasRun = await pluginStore.get({ key: "initHasRun" });
  await pluginStore.set({ key: "initHasRun", value: true });
  return !initHasRun;
};

async function createSuperAdmin() {
  const params = {
    username: process.env.ADMIN_USER || 'test',
    password: process.env.ADMIN_PASS || 'test',
    firstname: process.env.ADMIN_NAME || "Test",
    lastname: process.env.ADMIN_LAST_NAME || "Test",
    email: process.env.ADMIN_EMAIL || 'example@website.com',
    blocked: false,
    isActive: true,
  };

  if (process.env.NODE_ENV === 'development' || process.env.CREATE_ADMIN) {
    //Check if any account exists.
    const admins = await strapi.query('user', 'admin').find();

    if (admins.length === 0) {
      let tempPass = params.password;
      let verifyRole = await strapi.query('role', 'admin').findOne({ code: 'strapi-super-admin' });
      if (!verifyRole) {
        verifyRole = await strapi.query('role', 'admin').create({
          name: 'Super Admin',
          code: 'strapi-super-admin',
          description: 'Super Admins can access and manage all features and settings.',
        });
      }
      params.roles = [verifyRole.id];
      params.password = await strapi.admin.services.auth.hashPassword(params.password);
      await strapi.query('user', 'admin').create({
        ...params,
      });
      strapi.log.info('Admin account was successfully created.');
      strapi.log.info(`Email: ${params.email}`);
      strapi.log.info(`Password: ${tempPass}`);
    }
  }
}

module.exports = async () => {
  const shouldImportSeedData = await isFirstRun();

  if (shouldImportSeedData) {
    try {
      await createSuperAdmin();
    } catch (error) {
      strapi.log.error(`Couldn't create Admin account during bootstrap: `, error);
    }

    try {
      console.log('Setting up your starter...');
      await importSeedData();
      console.log('Ready to go');
    } catch (error) {
      console.log('Could not import seed data');
      console.error(error);
    }
  }

  await registerConditions();
};
