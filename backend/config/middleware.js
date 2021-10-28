module.exports = {
  settings: {
    parser: {
      enabled: true,
      multipart: true,
      formidable: {
        maxFileSize: 2000 * 1024 * 1024 // Defaults to 2000mb
      }
    }
  },
};
