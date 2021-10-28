 

const xmlHeader = '<?xml version="1.0" encoding="UTF-8"?>'
module.exports = {
  generateSitemap(sitemap, host) {
  

    let xml  = `${xmlHeader}<urlset>`
    let date = new Date()
      sitemap.industries.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/industry/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      })
      sitemap.destinations.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/destinos/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
      sitemap.news_items.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/news/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
      sitemap.webinars.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/webinars/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
      sitemap.specials.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/specials/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
      sitemap.prizes.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/premios-y-ganadores/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
      sitemap.customers.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/marketing/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
      sitemap.partner_programs.map((item) => {
        xml += `
        <url>
            <loc>
            ${host}/portal-para-agentes/${item.slug}
            </loc>
            <lastmod>${date}</lastmod>
            <changefreq>daily</changefreq>
        </url>`
      
      })
    xml += '</urlset>'
    return xml
  }
}

