# Docker切换镜像源


&lt;!--more--&gt;

```bash
$ sudo mkdir -p /etc/docker
```

```bash
$ sudo tee /etc/docker/daemon.json &lt;&lt;-&#39;EOF&#39;

{

 &#34;registry-mirrors&#34;: [&#34;https://28ffkr6d.mirror.aliyuncs.com&#34;]

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

