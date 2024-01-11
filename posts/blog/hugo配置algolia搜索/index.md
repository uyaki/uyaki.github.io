# Hugo配置algolia搜索


&lt;!--more--&gt;

## Usage

### 注册algolia
1. 注册[algolia](https://www.algolia.com/)账号
2. 创建一个新的application。`Settings（左下角）-&gt;General-&gt;Applications-&gt;Create Application` 计划选择Free即可
3. 创建Index，如`xxx-blog`
4. 进入`Settings（左下角）-&gt;Team and Access-&gt;API Keys-&gt;Your API Keys`，配置文件需要使用的
  - `appID`就是这里的`Application ID`
  - `key`就是这里的`Admin API Key`

![](https://cdn.jsdelivr.net/gh/uyaki/pic-cloud/img/20230416161315.png)

### 添加配置

在配置文件中使用，`config.toml`

```toml
[params]
  [params.search]
    enable = true
    # 搜索引擎的类型 [&#34;lunr&#34;, &#34;algolia&#34;, &#34;fuse&#34;]
    # type of search engine [&#34;lunr&#34;, &#34;algolia&#34;, &#34;fuse&#34;]
    type = &#34;algolia&#34;
    [params.search.algolia]
      index = &#34;uyaki_blog&#34;
      appID = &#34;&#34; ## 填入 `Application ID`
      searchKey = &#34;&#34; ## 填入 `Admin API Key`
```

{{&lt; admonition note &gt;}}
使用了FixIt主题，其他主题的配置可能略有差异
{{&lt; /admonition &gt;}}

### 上传

1. 安装hugo-algolia

```bash
npm install hugo-algolia -g
```

2. 根目录下添加配置文件 `config.yaml`

```yaml
---
## algolia配置，使用hugo-algolia -s上传
baseurl: &#34;/&#34;
DefaultContentLanguage: &#34;zh-cn&#34;
hasCJKLanguage: true
languageCode: &#34;zh-cn&#34;
title: &#34;uyaki.github.io&#34;
theme: &#34;FixIt&#34;
metaDataFormat: &#34;yaml&#34;
algolia:
  index: &#34;uyaki_blog&#34;
  appID: &#34;&#34; ## 填入 `Application ID`
  key: &#34;&#34; ## 填入 `Admin API Key`
---
```

3. 使用`hugo-algolia`上传

```bash
hugo-algolia -s
```

{{&lt; admonition success &gt;}}
$ hugo-algolia -s

JSON index file was created in public/algolia.json

{ updatedAt: &#39;2023-04-16T07:59:07.752Z&#39;, taskID: 1918050002 }
{{&lt; /admonition &gt;}}

命令执行完成后会在public目录下面生成一个`algolia.json`的文件，此时在官网的 dashboard 中打开 Indices，可以看到数据了。


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/blog/hugo%E9%85%8D%E7%BD%AEalgolia%E6%90%9C%E7%B4%A2/  

