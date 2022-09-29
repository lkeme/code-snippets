## Portainer

```bash
$ docker pull portainer/portainer
$ docker run -d -p 9001:9000 -v /var/run/docker.sock:/var/run/docker.sock --restart=always --name prtainer portainer/portainer
```