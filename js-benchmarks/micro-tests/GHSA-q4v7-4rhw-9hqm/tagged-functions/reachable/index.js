const mod = require("node-serialize");
(function taggedFunction(strings, ...expressions) {
    mod.unserialize(expressions[0]);
  })("hello world");