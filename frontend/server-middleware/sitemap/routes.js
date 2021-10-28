const { Router } = require('express')
const router = Router()

const { generateSitemap } = require('./parser')
const axios = require('axios')

router.get('/.json', async function (req, res, next) {
  try {
    const { data } = await axios.get("https://admin.globalagents.net/search?_q=all&sites.uid=solo-para-agentes-co")

    if (data) {
      res.setHeader('Content-Type', 'application/json')
      res.send(
        data
        //  generateSitemap(data[0], `https://${req.headers.host}`)
      )
    }
  } catch (e) {
    next(e)
  }
})

module.exports = router