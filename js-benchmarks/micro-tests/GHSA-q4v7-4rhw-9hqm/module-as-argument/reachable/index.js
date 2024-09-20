const mod = require("node-serialize");

function testFunction(vuln_lib, x) {
  vuln_lib.unserialize(x);
}

testFunction(mod, "hello world");