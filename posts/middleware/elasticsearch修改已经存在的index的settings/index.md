# ElasticSearch修改已经存在的index的settings


<!--more-->
1. 关闭索引
```http
POST /index/_close
```

2. 修改索引Settings
```http
PUT /index/_settings
{
    "settings": {
        "analysis": {
            "analyzer": {
                "ik_pinyin_analyzer": {
                    "type": "custom",
                    "tokenizer": "ik_smart",
                    "filter": [
                        "my_pinyin",
                        "word_delimiter"
                    ]
                }
            },
            "filter": {
                "my_pinyin": {
                    "type": "pinyin",
                    "keep_first_letter": false,
                    "keep_full_pinyin": true,
                    "keep_none_chinese": true,
                    "keep_none_chinese_in_first_letter": true,
                    "keep_original": false,
                    "limit_first_letter_length": 16,
                    "lowercase": true,
                    "trim_whitespace": true
                }
            }
        }
    }
}
```

3. 打开索引
```http
POST /index/_open
```


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/middleware/elasticsearch%E4%BF%AE%E6%94%B9%E5%B7%B2%E7%BB%8F%E5%AD%98%E5%9C%A8%E7%9A%84index%E7%9A%84settings/  

