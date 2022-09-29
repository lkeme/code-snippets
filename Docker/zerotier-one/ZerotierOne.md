## ZerotierOne

```bash
$ docker pull bltavares/zerotier
$ docker run -d --device=/dev/net/tun \
--name zerotier-one \
--net=host \
--restart=always \
--cap-add=NET_ADMIN \
--cap-add=SYS_ADMIN \
-v /var/lib/zerotier-one:/var/lib/zerotier-one \
bltavares/zerotier:latest
$ docker exec zerotier-one zerotier-cli join [网络ID] # m
```