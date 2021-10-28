const express = require('express')
const app = express()
const axios = require('axios')
const sitemap = require('./routes')

app.use(sitemap)

module.exports = {
  path: '/sitemap',
  handler: app
}