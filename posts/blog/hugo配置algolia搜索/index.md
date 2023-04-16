# Hugo配置algolia搜索


<!--more-->

## Usage

### 注册algolia
1. 注册[algolia](https://www.algolia.com/)账号
2. 创建一个新的application。`Settings（左下角）->General->Applications->Create Application` 计划选择Free即可
3. 创建Index，如`xxx-blog`
4. 进入`Settings（左下角）->Team and Access->API Keys->Your API Keys`，配置文件需要使用的
  - `appID`就是这里的`Application ID`
  - `key`就是这里的`Admin API Key`

![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20230416161315.png)

### 添加配置

在配置文件中使用，`config.toml`

```toml
[params]
  [params.search]
    enable = true
    # 搜索引擎的类型 ["lunr", "algolia", "fuse"]
    # type of search engine ["lunr", "algolia", "fuse"]
    type = "algolia"
    [params.search.algolia]
      index = "uyaki_blog"
      appID = "" ## 填入 `Application ID`
      searchKey = "" ## 填入 `Admin API Key`
```

{{< admonition note >}}
使用了FixIt主题，其他主题的配置可能略有差异
{{< /admonition >}}

### 上传

1. 安装hugo-algolia

```bash
npm install hugo-algolia -g
```

2. 根目录下添加配置文件 `config.yaml`

```yaml
---
## algolia配置，使用hugo-algolia -s上传
baseurl: "/"
DefaultContentLanguage: "zh-cn"
hasCJKLanguage: true
languageCode: "zh-cn"
title: "uyaki.github.io"
theme: "FixIt"
metaDataFormat: "yaml"
algolia:
  index: "uyaki_blog"
  appID: "" ## 填入 `Application ID`
  key: "" ## 填入 `Admin API Key`
---
```

3. 使用`hugo-algolia`上传

```bash
hugo-algolia -s
```

{{< admonition success >}}
$ hugo-algolia -s 

JSON index file was created in public/algolia.json 

{ updatedAt: '2023-04-16T07:59:07.752Z', taskID: 1918050002 }
{{< /admonition >}}

命令执行完成后会在public目录下面生成一个`algolia.json`的文件，此时在官网的 dashboard 中打开 Indices，可以看到数据了。


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/blog/hugo%E9%85%8D%E7%BD%AEalgolia%E6%90%9C%E7%B4%A2/  

