# Mac系统下修改docker的vm参数


<!--more-->

1. screen

```bash
screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
```

会出现如下界面

![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200217143600.png)


2. 键入`回车`，出现如下界面

![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200217144718.png)

3. 像正常linux系统一样设置

```bash
sysctl -w vm.max_map_count=262144
```

4. 按`control+a`，再按`control+\` ，左下角出现退出提示后，按y确认退出

![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200217144803.png)


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/docker/mac%E7%B3%BB%E7%BB%9F%E4%B8%8B%E4%BF%AE%E6%94%B9docker%E7%9A%84vm%E5%8F%82%E6%95%B0/  

