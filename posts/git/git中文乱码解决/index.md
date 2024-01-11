# Git中文乱码解决


&lt;!--more--&gt;
## git add 显示中文乱码

使用 git add 添加要提交的文件的时候，如果文件名是中文，会显示形如`\347\204\246\347\263\226\345\245\266\350\214\266.md`的乱码

```bash
$ git config --global core.quotepath false
```

## git log 显示提交的中文 log 乱码
```bash
# 设置 git gui 的界面编码 
$ git config --global gui.encoding utf-8
# 设置 commit log 提交时使用 utf-8 编码，可避免服务器上乱码，同时与 linux 上的提交保持一致！ 
$ git config --global i18n.commitencoding utf-8
# 使得在 $ git log 时将 utf-8 编码转换成 gbk 编码，解决 Msys bash 中 git log 乱码。
git config --global i18n.logoutputencoding gbk
# 使得 git log 可以正常显示中文（配合 i18n.logoutputencoding = gbk)，在 /etc/profile 中添加：
export LESSCHARSET=utf-8
```

## 自带的 bash 中，使用 ls 命令查看中文文件名乱码
使用 `ls --show-control-chars` 命令来强制使用控制台字符编码显示文件名，即可查看中文文件名。
为了方便使用，可以编辑 `/etc/git-completion.bash` ，新增一行 `alias ls=&#34;ls –show-control-chars&#34;`


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/git/git%E4%B8%AD%E6%96%87%E4%B9%B1%E7%A0%81%E8%A7%A3%E5%86%B3/  

