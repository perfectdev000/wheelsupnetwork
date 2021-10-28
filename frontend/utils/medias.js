export function getStrapiMedia(url) {
  // Check if URL is a local path
  if (url.startsWith("/uploads")) {
    // Prepend Strapi address
    return `https://admin.globalagents.net${url}`;
  }
  // Otherwise return full URL
  return url;
}
