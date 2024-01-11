# Hugo&#43;FixIt


&lt;!--more--&gt;

## hugo安装

```bash
# go安装
go install github.com/gohugoio/hugo@latest
# 如果需要支持Sass/SCSS
# 1. 设置go变量CGO_ENABLED=1
# 2. 执行 -tags extended
go install -tags extended github.com/gohugoio/hugo@latest
```
{{&lt; admonition warning &gt;}}

1. FixIt使用了Sass必须执行 `go install -tags extended github.com/gohugoio/hugo@latest`，否则会报错
2. 如果已经安装了hugo，一定要升级到新版本，旧版本有很多不兼容FixIt
{{&lt;/ admonition &gt;}}

## 建站

```bash
hugo new site blog
cd blog
git init
git submodule add https://github.com/hugo-fixit/FixIt.git themes/FixIt
git submodule update
## 复制配置文件
mv config.toml config.old.toml
cp themes/FixIt/config.toml config.toml
```

## 修改 config.toml

最前面添加
```toml
title = &#34;&#34;
baseURL = &#34;&#34;
languageCode = &#34;zh-cn&#34;
# en / zh-cn / ... (This field determines which i18n file to use)
defaultContentLanguage = &#34;zh-cn&#34;
# 是否包括中日韩文字
hasCJKLanguage = true

theme = &#34;FixIt&#34;
```

## config.toml 完整配置

[FixIt中文站](https://fixit.lruihao.cn/zh-cn/documentation/basics/)

## 项目发起人shortcode（非必须）

```bash
git submodule add https://github.com/Lruihao/hugo-shortcode-sponsor-log.git themes/shortcode-sponsor-log
```

配置
```toml
theme = [&#34;your-main-theme&#34;, &#34;shortcode-sponsor-log&#34;]
```

复制数据文件，自行修改
```bash
cp themes/shortcode-sponsor-log/sponsor_log.yml.example data/sponsor_log.yml
```

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/blog/hugo&#43;fixit/  

