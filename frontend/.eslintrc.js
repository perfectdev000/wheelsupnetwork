module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: "babel-eslint",
  },
  extends: ["eslint:recommended", "plugin:vue/recommended", "prettier/vue"],
  plugins: ["vue"],
  // add your custom rules here
  rules: {},
};
