# SpringBoot设置项目热启动


<!--more-->

## 导入jar包
```markdown
'org.springframework.boot:spring-boot-devtools'
```
## 添加配置项
```yaml
devtools: #热部署
    restart:
      enabled: true
```

## 在idea开启
1. 如下图设置 `Build，Execution...->Compiler`，勾选 `Build project automatically`
![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200223011604.png)
2. 快捷键 `commond+option+shift+'/'`，弹出`Maintenance`界面
![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200223011708.png)
3. 点击`Registry`, 勾选compiler.automake.allow.when.app.running
![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20200223011808.png)
4. 重启项目



---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/java/springboot%E8%AE%BE%E7%BD%AE%E9%A1%B9%E7%9B%AE%E7%83%AD%E5%90%AF%E5%8A%A8/  

