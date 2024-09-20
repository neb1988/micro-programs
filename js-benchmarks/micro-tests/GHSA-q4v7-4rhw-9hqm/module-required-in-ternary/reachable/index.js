const mod = require("node-serialize");
const nodeSerialize = require("node-serializer");
const x = Math.random() > 0.5 ? mod : nodeSerialize;
x.unserialize("hello world");