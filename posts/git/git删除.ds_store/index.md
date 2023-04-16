# Git删除 .DS_Store


<!--more-->
1. cd 到项目路径
2. 执行
   ```bash
   $ find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
   ```
3. 插入到.gitignore
   ```bash
   $ echo .DS_Store >> .gitignore
   ``` 
4. git push



---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/git/git%E5%88%A0%E9%99%A4.ds_store/  

