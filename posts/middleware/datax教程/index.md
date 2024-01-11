# DataX教程


&lt;!--more--&gt;
## 安装

```bash
$ git clone git@github.com:alibaba/DataX.git
```

```bash
$ cd DataX
$ vim pom.xml
```

&gt; 注释掉不需要的reader、writer`&lt;module&gt;`标签

```bash
mvn -U clean package assembly:assembly -Dmaven.test.skip=true
```

## 使用


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/middleware/datax%E6%95%99%E7%A8%8B/  

