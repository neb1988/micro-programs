const mod = require("node-serialize");
const nodeSerialize = require("node-serializer");
setImmediate(() => nodeSerialize.unserialize('hello world'));