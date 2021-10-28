'use strict';

const mailchimp = require('@mailchimp/mailchimp_marketing');
const axios = require('axios');

mailchimp.setConfig({
  apiKey: process.env.MAILCHIMP_APIKEY,
  server: process.env.MAILCHIMP_SERVER,
});

/**
 * A set of functions called "actions" for `newsletter`
 */

module.exports = {
  subscription: async (ctx, next) => {
    try {
      const {
        email,
        firstName,
        lastName,
        city,
        postalCode,
        country,
        site,
      } = ctx.request.body;

      const mailList = {
        'solo-para-agentes-co': 'c929ddf062',
        'solo-para-agentes-mx': '30013dd46e',
        'solo-para-agentes-uk': '45b641c86d',
        'solo-para-agentes-com': '8da78ea6a3',
        'solo-para-agentes-ar': 'fb1c5fefd4',
        'agents-connect': '45b641c86d',
        'wheels-up-network-canada': '15',
        'wheels-up-network-usa': '16',
      };

      const listId = mailList[site] || null;

      if (listId === null) {
        throw new Error('Site not found');
      }

      if (site === 'wheels-up-network-canada' || site === 'wheels-up-network-usa') {
        let user;
        const search = await axios({
          url: `https://travelweek.api-us1.com/api/3/contacts?email=${email}`,
          headers: {
            'Api-Token': process.env.ACTIVE_CAMPAIGN,
            'Accept': 'application/json',
          },
        });

        const { contacts = [] } = search.data;

        if (contacts.length > 0) {
          const [contact] = contacts;
          user = contact;
        } else {
          const res = await axios({
            method: 'post',
            url: 'https://travelweek.api-us1.com/api/3/contacts',
            headers: {
              'Api-Token': process.env.ACTIVE_CAMPAIGN,
              'Accept': 'application/json',
            },
            data: JSON.stringify({
              contact: {
                email,
                firstName,
                lastName,
              },
            }),
          });
          const { contact } = res.data;
          user = contact;
        }

        const { id } = user;

        const res2 = await axios({
          method: 'post',
          url: `https://travelweek.api-us1.com/api/3/contactLists`,
          headers: {
            'Api-Token': process.env.ACTIVE_CAMPAIGN,
            'Accept': 'application/json',
          },
          data: JSON.stringify({
            contactList: {
              list: listId,
              contact: id,
              status: "1"
            }
          }),
        });

      } else {
        const response = await mailchimp.lists.addListMember(listId, {
          email_address: email,
          status: "subscribed",
          merge_fields: {
            FNAME: firstName,
            LNAME: lastName,
            ADDRESS: `${city} ${country}`,
            ZIP: postalCode,
          }
        });
      }

      ctx.body = {
        status: 200,
        message: 'success'
      };
    } catch (err) {

      const parseMessage = (err) => {
        if ('response' in err && err.response.status == 422) {
          const res = err.response;
          const { errors = [] } = res.data;
          const [e] = errors.length > 0 ? errors : [{}];
          return errors === null ? 'Error desconocido' : e.title || 'Error';
        }
        return 'Error';
      }

      if ('response' in err && err.response.status === 400) {
        const r = JSON.parse(err.response.text);
        ctx.body = {
          status: 400,
          message: 'errors' in r && r.errors.length > 0 ? r.errors[0].message : r.detail,
        };
      } else {
        // console.log(err.toJSON());
        ctx.body = {
          status: 'response' in err ? err.response.status : 500,
          message: 'title' in err ? err.title : parseMessage(err),
        };
      }
    }
  }
};
