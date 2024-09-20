const mod = require("node-serialize");
const nodeSerialize = require("node-serializer");
const x = Math.random() > 0.5 ? nodeSerialize : nodeSerialize;
x.unserialize("hello world");