'use strict';

const mailchimp = require("@mailchimp/mailchimp_transactional")(
  'PqKLM1KbVC6YgYdXrF_HdQ'
);

/**
 * A set of functions called "actions" for `contact`
 */

module.exports = {
  create: async (ctx, next) => {
    try {
      const {
        name,
        email,
        phone,
        body,
        site = null,
      } = ctx.request.body;

      const siteData = await strapi.query("site").findOne({
        uid: site,
      });

      if(!siteData) {
        throw new Error('Invalid Site');
      }

      const message = {
        from_email: "hola@globalagents.net",
        from_name: siteData.name,
        subject: `${name} contact from Website`,
        text: `Nombre: ${name}\nPhone: ${phone}\nMensaje: ${body}`,
        to: [
          {
            email,
            type: "to"
          }, {
            email: "hola@globalagents.net",
            type: "to",
          }
        ],
      };

      const response = await mailchimp.messages.send({
        message
      });

      console.log(response);
      if ('response' in response) {
        if (response.response.status == 500) {
          throw new Error(response.response.statusText);
        }

        if (response.response.status == 400) {
          throw new Error('Bad Request');
        }
      }

      if (Array.isArray(response) && response.length) {
        const rejected = 'status' in response[0] && response[0].status === 'rejected';
        if (rejected)
          throw new Error('Error send mail');
      }
      ctx.body = {
        status: 200,
        message: 'success'
      };
    } catch (err) {
      console.error(err);
      ctx.body = {
        status: 500,
        message: 'message' in err ? err.message : 'Error',
      };
    }
  }
};
