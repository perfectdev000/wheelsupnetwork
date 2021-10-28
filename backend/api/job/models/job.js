'use strict';

const slugify = require('strapi-utils').nameToSlug;
const _ = require('lodash');

const modelName = 'job';

/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#lifecycle-hooks)
 * to customize this model
 */

module.exports = {
  lifecycles: {
    async beforeCreate(data) {
      if (data.name && _.isEmpty(data.slug)) {
        data.slug = slugify(data.name);
      }

      // const records = await strapi.query(modelName).count({
      //   slug: data.slug,
      //   sites: data.site || null,
      // });

      // if(records > 0) {
      //   throw strapi.errors.badRequest('There is already a post with this same slug');
      // }
    },
    // async beforeUpdate(params, data) {
    //   if (data.title) {
    //     data.slug = slugify(data.title, { lower: true });
    //   }
    //   const record = await strapi.query(modelName).findOne({
    //     slug: data.slug,
    //     sites: data.site || null,
    //   });

    //   if(record !== null && record.id !== data.id) {
    //     throw strapi.errors.badRequest('There is already a post with this same slug');
    //   }
    // },
  },
};
