module.exports = function(config) {
    config.set({
    "baseUrl": "./",
    "browsers": [
        "PhantomJS"
    ],
    "captureTimeout": 60000,
    "colors": true,
    "files": [
        "main.js",
        "test_main.js"
    ],
    "frameworks": ["mocha", "chai", "expect", "sinon"],
    "logLevel": "INFO",
    "port": 9876,
    "reporters": [
        "spec",
        "progress"
    ],
    "singleRun": true
});
}
