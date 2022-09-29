## Vite代理Websocket

```js
// http://www.alvinhtml.com/article/web/vite-proxy-https.html
'/ws/log': {
    // 允许访问数据的计算机名称
    target: `${process.env.VITE_BASE_PATH}:8888/`,
        changeOrigin: true, // 开启代理跨域
        secure: false,
        ws: true, // 启用webSocket
        pathRewrite: {
        // 重写api地址
        '^/ws/log': '',
    },
    headers: {
        Referer: 'http://example.com',
    },
},
```