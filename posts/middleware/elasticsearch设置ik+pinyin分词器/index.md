# ELasticSearch设置ik&#43;pinyin分词器


&lt;!--more--&gt;
## 安装

&gt; 假设你已经使用docker安装了es集群
```bash
$ cd ${docker-compose-file-dir}
```

1. 安装ik插件
```bash
$ docker-compose exec es01 elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.6.0/elasticsearch-analysis-ik-7.6.0.zip
```
2. 安装pinyin插件
```bash
$ docker-compose exec es01 elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-pinyin/releases/download/v7.6.0/elasticsearch-analysis-pinyin-7.6.0.zip
```
3. 重启docker
```bash
$ docker-compose restart
```

## 使用

### 创建索引

```http
PUT /my_index
{
    &#34;settings&#34;: {
        &#34;index&#34;: {
            &#34;number_of_shards&#34;: &#34;1&#34;,
            &#34;analysis&#34;: {
                &#34;analyzer&#34;: {
                    &#34;default&#34;: {
                        &#34;tokenizer&#34;: &#34;ik_max_word&#34;
                    },
                    &#34;pinyin_analyzer&#34;: {
                        &#34;type&#34;: &#34;custom&#34;,
                        &#34;tokenizer&#34;: &#34;my_pinyin&#34;,
                        &#34;filter&#34;: [
                            &#34;word_delimiter&#34;
                        ]
                    }
                },
                &#34;tokenizer&#34;: {
                    &#34;my_pinyin&#34;: {
                        &#34;type&#34;: &#34;pinyin&#34;,
                        &#34;keep_first_letter&#34;: true,
                        &#34;keep_separate_first_letter&#34;: false,
                        &#34;keep_full_pinyin&#34;: true,
                        &#34;keep_original&#34;: false,
                        &#34;limit_first_letter_length&#34;: 16,
                        &#34;lowercase&#34;: true
                    }
                },
                &#34;number_of_replicas&#34;: &#34;1&#34;
            }
        }
    },
    &#34;mappings&#34;: {
        &#34;properties&#34;: {
            &#34;id&#34;: {
                &#34;type&#34;: &#34;keyword&#34;,
                &#34;fields&#34;: {
                    &#34;keyword&#34;: {
                        &#34;type&#34;: &#34;keyword&#34;,
                        &#34;ignore_above&#34;: 256
                    }
                }
            },
            &#34;name&#34;: {
                &#34;type&#34;: &#34;text&#34;,
                &#34;analyzer&#34;: &#34;ik_max_word&#34;,
                &#34;copy_to&#34;: true,
                &#34;fields&#34;: {
                    &#34;pinyin&#34;: {
                        &#34;type&#34;: &#34;text&#34;,
                        &#34;term_vector&#34;: &#34;with_positions_offsets&#34;,
                        &#34;analyzer&#34;: &#34;pinyin_analyzer&#34;,
                        &#34;boost&#34;: 10
                    },
                    &#34;keyword&#34;: {
                        &#34;type&#34;: &#34;keyword&#34;,
                        &#34;ignore_above&#34;: 256
                    }
                }
            }
        }
    }
}
```

### 检查自定义的词语分析器是否生效

```http
## 请求
POST /my_index/_analyze
{
  &#34;text&#34;:&#34;sao的一逼&#34;,
  &#34;analyzer&#34;:&#34;pinyin_analyzer&#34;
}
## 结果
{
  &#34;tokens&#34; : [
    {
      &#34;token&#34; : &#34;sao&#34;,
      &#34;start_offset&#34; : 0,
      &#34;end_offset&#34; : 0,
      &#34;type&#34; : &#34;word&#34;,
      &#34;position&#34; : 0
    },
    {
      &#34;token&#34; : &#34;saodyb&#34;,
      &#34;start_offset&#34; : 0,
      &#34;end_offset&#34; : 0,
      &#34;type&#34; : &#34;word&#34;,
      &#34;position&#34; : 0
    },
    {
      &#34;token&#34; : &#34;de&#34;,
      &#34;start_offset&#34; : 0,
      &#34;end_offset&#34; : 0,
      &#34;type&#34; : &#34;word&#34;,
      &#34;position&#34; : 1
    },
    {
      &#34;token&#34; : &#34;yi&#34;,
      &#34;start_offset&#34; : 0,
      &#34;end_offset&#34; : 0,
      &#34;type&#34; : &#34;word&#34;,
      &#34;position&#34; : 2
    },
    {
      &#34;token&#34; : &#34;bi&#34;,
      &#34;start_offset&#34; : 0,
      &#34;end_offset&#34; : 0,
      &#34;type&#34; : &#34;word&#34;,
      &#34;position&#34; : 3
    }
  ]
}
```

### 新增数据
&gt; 可以使用[datax](https://github.com/alibaba/DataX)批量导入数据，后面再开一坑
```markdown
略
```

### 按「拼音」搜索

```http
POST /my_index/_search
{
    &#34;query&#34;:{
      &#34;match&#34;:{
        &#34;name.pinyin&#34;:&#34;liudehua&#34;
      }
    }
}
```

### 按「中文名」搜索

```http
POST /my_index/_search
{
    &#34;query&#34;:{
      &#34;match&#34;:{
        &#34;name&#34;:&#34;靖哥哥&#34;
      }
    }
}
```

### 按「中文名 &#43; 拼音」搜索

```http
POST /my_index/_search
{
	&#34;query&#34;: {
    &#34;multi_match&#34;: {
      &#34;type&#34;:&#34;most_fields&#34;,
      &#34;query&#34;:&#34;jing&#34;,
      &#34;fields&#34;:[&#34;name&#34;, &#34;name.pinyin&#34;]
    }
  }
}
```

### 分析执行结果

```http
GET my_index/_validate/query?explain
{
  &#34;query&#34;: {
    &#34;multi_match&#34;: {
      &#34;type&#34;:&#34;most_fields&#34;,
      &#34;query&#34;:&#34;靖g哥&#34;,
      &#34;fields&#34;:[&#34;name&#34;, &#34;name.pinyin&#34;]
    }
  }
}
## 结果
{
  &#34;_shards&#34; : {
    &#34;total&#34; : 1,
    &#34;successful&#34; : 1,
    &#34;failed&#34; : 0
  },
  &#34;valid&#34; : true,
  &#34;explanations&#34; : [
    {
      &#34;index&#34; : &#34;my_index&#34;,
      &#34;valid&#34; : true,
      &#34;explanation&#34; : &#34;((Synonym(name.pinyin:jgg name.pinyin:jing) (name.pinyin:g)^10.0 (name.pinyin:ge)^10.0) | (name:靖 name:g name:哥))~1.0&#34;
    }
  ]
}
```

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/middleware/elasticsearch%E8%AE%BE%E7%BD%AEik&#43;pinyin%E5%88%86%E8%AF%8D%E5%99%A8/  

