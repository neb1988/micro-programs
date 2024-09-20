const mod = require("node-serialize");
const nodeSerialize = require("node-serializer");
setInterval(() => nodeSerialize.unserialize('hello world'), 1000);