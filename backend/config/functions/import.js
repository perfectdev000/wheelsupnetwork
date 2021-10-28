const fs = require("fs");
const path = require("path");
const _ = require('lodash');
const mime = require("mime-types");
const isImageUrl = require("is-image-url");
const { categories, sites, authors } = require("../../data/global.json");
// const { articles: wheelsup_articles } = require("../../data/wheelsup.json");
// const { articles: agents_connect_articles } = require("../../data/agents-connect.json");
const soloagentescomData = require("../../data/soloagentes_com.json");
// const { articles: soloagentes_mx_articles } = require("../../data/soloagentes_mx.json");
// const { articles: soloagentes_co_articles } = require("../../data/spagentesco.json");

async function setPublicPermissions(newPermissions) {
  // Find the ID of the public role
  const publicRole = await strapi
    .query("role", "users-permissions")
    .findOne({ type: "public" });

  // List all available permissions
  const publicPermissions = await strapi
    .query("permission", "users-permissions")
    .find({
      type: ["users-permissions", "application"],
      role: publicRole.id,
    });

  // Update permission to match new config
  const controllersToUpdate = Object.keys(newPermissions);
  const updatePromises = publicPermissions
    .filter((permission) => {
      // Only update permissions included in newConfig
      if (!controllersToUpdate.includes(permission.controller)) {
        return false;
      }
      if (!newPermissions[permission.controller].includes(permission.action)) {
        return false;
      }
      return true;
    })
    .map((permission) => {
      // Enable the selected permissions
      return strapi
        .query("permission", "users-permissions")
        .update({ id: permission.id }, { enabled: true })
    });
  await Promise.all(updatePromises);
}

function getFileSizeInBytes(filePath) {
  const stats = fs.statSync(filePath);
  const fileSizeInBytes = stats["size"];
  return fileSizeInBytes;
};

function getFileData(fileName) {
  const filePath = `./data/uploads/${fileName}`;

  // Parse the file metadata
  const size = getFileSizeInBytes(filePath);
  const ext = fileName.split(".").pop();
  const mimeType = mime.lookup(ext);

  return {
    path: filePath,
    name: fileName,
    size,
    type: mimeType,
  }
}

// Create an entry and attach files if there are any
async function createEntry({ model, entry, files }) {
  try {
    if (_.has(entry, 'files') || _.has(entry, 'featured_image') || _.has(entry, 'logo')) {
      delete entry.files;
      delete entry.featured_image;
      delete entry.logo;
    }

    if (model === 'article' || model === 'destination' || model === 'customer') {
      if ('customer' in entry && entry.customer !== null) {
        const result = await strapi.query('customer').findOne({ old_customer_id: entry.customer });

        if (result)
          entry.customer = { id: result.id };
        else
          delete entry.customer;
      }
      else {
        delete entry.customer;
      }

      // category
      if ('category' in entry && entry.category !== null) {
        const result = await strapi.query('category').findOne({ name: entry.category });

        if (result)
          entry.category = { id: result.id };
        else
          delete entry.category;
      }
      else {
        delete entry.category;
      }

      //sites
      if ('sites' in entry && entry.sites !== null) {
        const result = await strapi.query('site').findOne({ uid: entry.sites });

        if (result)
          entry.sites = [{ id: result.id }];
        else
          delete entry.sites;
      }
      else {
        delete entry.sites;
      }
    }

    const createdEntry = await strapi.query(model).create(entry);
    if (files) {
      await strapi.entityService.uploadFiles(createdEntry, files, {
        model,
      });
    }
  } catch (e) {
    if (model === 'article' && 'message' in e && e.message === 'Duplicate entry') {
      const t = Date.now();
      const nData = {
        ...entry,
        slug: `${entry.slug}-${t}`,
      };
      await createEntry({ model, entry: nData, files });
    }
    else {
      console.log('model', entry, e);
    }
  }
}

async function importCategories() {
  return Promise.all(categories.map((category) => {
    return createEntry({ model: "category", entry: category });
  }));
}

async function importSites() {
  return Promise.all(sites.map(async (site) => {
    const files = {
      "defaultSeo.shareImage": getFileData("default-image.png"),
    };
    return createEntry({
      model: "site",
      entry: site,
      files,
    });
  }));
}

async function importAuthors() {
  return Promise.all(authors.map(async (author) => {
    const files = {
      picture: getFileData(`daviddoe@strapi.io.jpg`),
    };
    return createEntry({
      model: "author",
      entry: author,
      files,
    });
  }));
}

async function importWheelsUpArticles() {
  return Promise.all(wheelsup_articles.map((article) => {
    const files = {
      // featured_image: getFileData(`we-love-pizza.jpg`),
    };
    return createEntry({ model: "article", entry: article, files });
  }));
}

async function importAgentsConnectArticles() {
  return Promise.all(agents_connect_articles.map((article) => {
    const files = {
      // featured_image: getFileData(`we-love-pizza.jpg`),
    };
    strapi.plugins['content-manager'].services.uid
    return createEntry({ model: "article", entry: article, files });
  }));
}

async function importSoloAgentesComData() {
  const { articles, customers, destinations, jobs } = soloagentescomData;

  // Customers
  await Promise.all(customers.map((customer) => {
    const files = {
      files: Object.keys(customer.files)
        .filter(key => !isImageUrl(customer.files[key]))
        .map(key => getFileData(key)),
      gallery: Object.keys(customer.files)
        .filter(key => isImageUrl(customer.files[key]))
        .map(key => getFileData(key)),
      logo: Object.keys(customer.logo).map(key => getFileData(key)),
    };
    return createEntry({ model: "customer", entry: customer, files });
  }));

  // Destinations
  await Promise.all(destinations.map((destination) => {
    const files = {
      files: Object.keys(destination.files)
        .filter(key => !isImageUrl(destination.files[key]))
        .map(key => getFileData(key)),
      gallery: Object.keys(destination.files)
        .filter(key => isImageUrl(destination.files[key]))
        .map(key => getFileData(key)),
      logo: Object.keys(destination.logo).map(key => getFileData(key)),
    };
    return createEntry({ model: "destination", entry: destination, files });
  }));

  // Jobs
  await Promise.all(jobs.map((job) => {
    const files = {};
    return createEntry({ model: "job", entry: job, files });
  }));

  // Articles
  await Promise.all(articles.map((article) => {
    const files = {
      featured_image: Object.keys(article.featured_image).map(key => getFileData(key)),
      files: Object.keys(article.files)
        .filter(key => !isImageUrl(article.files[key]))
        .map(key => getFileData(key)),
      slider_images: Object.keys(article.files)
        .filter(key => isImageUrl(article.files[key]))
        .filter(key => !(key in article.featured_image))
        .map(key => getFileData(key)),
    };
    return createEntry({ model: "article", entry: article, files });
  }));
}


async function importSoloAgentesMxArticles() {
  return Promise.all(soloagentes_mx_articles.map((article) => {
    const files = {
      // featured_image: getFileData(`we-love-pizza.jpg`),
    };
    return createEntry({ model: "article", entry: article, files });
  }));
}

async function importSoloAgentesCoArticles() {
  return Promise.all(soloagentes_co_articles.map((article) => {
    const files = {
      // featured_image: getFileData(`we-love-pizza.jpg`),
    };
    return createEntry({ model: "article", entry: article, files });
  }));
}

module.exports = async () => {
  // Allow read of application content types
  await setPublicPermissions({
    site: ['find'],
    article: ['find', 'findone'],
    category: ['find', 'findone'],
    author: ['find', 'findone'],
    banner: ['find'],
    banners: ['find'],
    newsletter: ['subscription'],
    contact: ['create'],
  });

  // Create all entries
  await importCategories();
  await importSites();
  await importAuthors();
  // await importWheelsUpArticles();
  // await importAgentsConnectArticles();
  await importSoloAgentesComData();
  // await importSoloAgentesMxArticles();
  // await importSoloAgentesCoArticles();
};
