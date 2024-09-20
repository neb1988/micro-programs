const unserializeProperty = "unserialize";
const obj = {
[unserializeProperty]: require("node-serializer").unserialize
};
obj[unserializeProperty("hello world");