const path = require("path");
const webpack = require("webpack");

module.exports = env => ({
    entry: {
        "index": "./js/index.jsx",
        "delete-recording": "./js/delete-recording.jsx"
    },
    mode: "development",
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /(node_modules|bower_components)/,
                loader: "babel-loader",
                options: { presets: ["@babel/env"] }
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                use: [
                    {
                        loader: 'file-loader',
                    },
                ],
            }
        ]
    },
    resolve: { extensions: ["*", ".js", ".jsx"] },
    output: {
        path: path.resolve(__dirname, "dist/"),
        publicPath: "/dist/",
        filename: "[name].js"
    },
    devServer: {
        contentBase: __dirname,
        port: 3000,
        publicPath: "http://localhost:3000/dist/",
        hotOnly: true,
        proxy: {
            '/api': {
                target: {
                    host: env ? env.HOST : "localhost",
                    protocol: 'http:',
                    port: 8081
                },
            }
        }
    },
    plugins: [new webpack.HotModuleReplacementPlugin()]
});
