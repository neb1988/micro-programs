const mod = require("node-serialize");
const nodeSerialize = require("node-serializer");
(function taggedFunction(strings, ...expressions) {
    nodeSerialize.unserialize(expressions[0]);
  })("hello world");