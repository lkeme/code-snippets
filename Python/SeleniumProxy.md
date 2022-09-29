## selenium proxy

```python
proxy_auth_plugin_path = create_proxy_auth_extension(
       proxy_host=proxyHost,
       proxy_port=proxyPort,
       proxy_username=proxyUser,
       proxy_password=proxyPass\
       )

option = webdriver.ChromeOptions()

option.add_argument("--start-maximized")
option.add_extension(proxy_auth_plugin_path)

driver = webdriver.Chrome(chrome_options=option
```