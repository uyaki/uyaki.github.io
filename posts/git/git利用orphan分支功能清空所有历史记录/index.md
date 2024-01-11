# Git利用orphan分支功能清空所有历史记录


&lt;!--more--&gt;
## 目的

清空git项目，获得一个没有历史记录的空项目

## 实现

```bash 
## 创建一个orphan分支
$ git checkout --orphan tmp_branch
## 给爷爬~~~~
$ git rm -rf .
## TODO 加一些文件
$ ... 
## 提交
$ git add .
$ git commit -am &#34;commit message&#34;
## 删除master分支
$ git branch -D master
## 重命名当前分支为master
$ git branch -m master
## 强制推送到远程
$ git push -f origin master
```

## tips📌

### git push -f无权限问题
可能会出现无法强制推送的BUG：

{{&lt; admonition bug &gt;}}
You are not allowed to force push code to a protected branch on this project
{{&lt; /admonition &gt;}}

配置下Git远程（在 Settings 的 Repository 设置项的 Protected Branches)

展示移除保护，之后恢复就行。

### --orphan其他用途
可以用于创建一个跟master无关的分支，使一个git管理不同的项目，找个时间再单独开个贴写吧，哈哈哈哈哈


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/git/git%E5%88%A9%E7%94%A8orphan%E5%88%86%E6%94%AF%E5%8A%9F%E8%83%BD%E6%B8%85%E7%A9%BA%E6%89%80%E6%9C%89%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95/  

