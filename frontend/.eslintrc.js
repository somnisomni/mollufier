module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    "plugin:vue/vue3-essential",
    "@vue/typescript/recommended",
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    quotes: ["warn", "double"],
    "keyword-spacing": ["error", {
      overrides: {
        for: { after: false },
        if: { after: false },
        switch: { after: false },
        while: { after: false },
      },
    }],
    "comma-dangle": ["error", "always-multiline"],
    "lines-between-class-members": "off",
  },
};
