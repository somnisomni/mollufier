/* eslint-disable */

module.exports = require("@vue/cli-service").defineConfig({
  devServer: {
    allowedHosts: process.env.ALLOWED_HOST ? [process.env.ALLOWED_HOST] : undefined,
  },
  publicPath: process.env.PUBLIC_PATH ? process.env.PUBLIC_PATH : "/",
  transpileDependencies: true,
});
