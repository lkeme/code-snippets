## FirefoxVNC

```bash
docker run --name Firefox -d \
    -p 8080:8080 \
    --env 'FIREFOX_V=latest' \
    --env 'FIREFOX_LANG=zh-CN' \
    --env 'CUSTOM_RES_W=1280' \
    --env 'CUSTOM_RES_H=768' \
    --env 'UID=99' \
    --env 'GID=100' \
    --env 'UMASK=000' \
    --env 'DATA_PERM=770' \
    ich777/firefox

http://127.0.0.1:8080/vnc.html?autoconnect=true
```
