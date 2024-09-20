const mod = require("node-serialize");
setInterval(() => mod.unserialize('hello world'), 1000);