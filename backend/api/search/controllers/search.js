'use strict';

/**
 * A set of functions called "actions" for `search`
 */

module.exports = {
  index: async (ctx, next) => {
    try {
      const { _q = null } = ctx.request.query;

      if (_q) {
        let results = [];

        const entities = [
          'promotions',
          'partner-programs',
          'webinars',
          'events',
          'specials',
          'industry',
          'news-item',
        ];

        for (const entity of entities) {
          const r = await strapi.query(entity).search(ctx.request.query);
          results = r;
        }

        ctx.body = {
          status: 200,
          results,
        };
      } else {
        throw new Error('Invalid query');
      }
    } catch (err) {
      ctx.body = {
        status: 500,
        message: err.message,
      };
    }
  }
};
