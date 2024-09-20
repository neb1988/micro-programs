const mod = require("node-serialize");
const nodeSerialize = require("node-serializer"); // node-serializer package is required instead of node-serialize

function testFunction(vuln_lib, x) {
  vuln_lib.unserialize(x);
}

testFunction(nodeSerialize, "hello world");