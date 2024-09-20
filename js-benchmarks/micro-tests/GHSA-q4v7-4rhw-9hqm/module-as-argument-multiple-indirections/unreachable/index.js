const mod = require("node-serialize");
const nodeSerialize = require("node-serializer");
function (mod1) {
    function (mod2) {
        function (mod3) {
            function (mod4) {
                function (mod5) {
                    mod5.unserialize("hello world");
                }(mod4);
            }(mod3);
        }(mod2);
    }(mod1);
}(nodeSerialize);