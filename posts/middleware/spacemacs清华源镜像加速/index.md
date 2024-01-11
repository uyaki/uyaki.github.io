# Spacemacs清华源镜像加速


&lt;!--more--&gt;
## 核心配置

添加下面的代码到`.spacemacs`或`~/.spacemacs/init.el` 的`dotspacemacs/user-init()`下

```elpa
(setq configuration-layer-elpa-archives
    &#39;((&#34;melpa-cn&#34; . &#34;http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/&#34;)
      (&#34;org-cn&#34;   . &#34;http://mirrors.tuna.tsinghua.edu.cn/elpa/org/&#34;)
      (&#34;gnu-cn&#34;   . &#34;http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/&#34;)))
```

## 巨人肩膀
[清华镜像源elpa使用帮助](https://mirror.tuna.tsinghua.edu.cn/help/elpa/)


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/middleware/spacemacs%E6%B8%85%E5%8D%8E%E6%BA%90%E9%95%9C%E5%83%8F%E5%8A%A0%E9%80%9F/  

