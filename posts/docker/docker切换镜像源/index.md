# Docker切换镜像源


<!--more-->

```bash
$ sudo mkdir -p /etc/docker
```

```bash
$ sudo tee /etc/docker/daemon.json <<-'EOF'

{

 "registry-mirrors": ["https://28ffkr6d.mirror.aliyuncs.com"]

}

EOF
```

```bash
$ sudo systemctl daemon-reload
```

```bash
$ sudo systemctl restart docker
```
![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200221185223.png)


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/docker/docker%E5%88%87%E6%8D%A2%E9%95%9C%E5%83%8F%E6%BA%90/  

