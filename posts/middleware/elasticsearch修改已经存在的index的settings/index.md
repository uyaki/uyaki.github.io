# ElasticSearch修改已经存在的index的settings


&lt;!--more--&gt;
1. 关闭索引
```http
POST /index/_close
```

2. 修改索引Settings
```http
PUT /index/_settings
{
    &#34;settings&#34;: {
        &#34;analysis&#34;: {
            &#34;analyzer&#34;: {
                &#34;ik_pinyin_analyzer&#34;: {
                    &#34;type&#34;: &#34;custom&#34;,
                    &#34;tokenizer&#34;: &#34;ik_smart&#34;,
                    &#34;filter&#34;: [
                        &#34;my_pinyin&#34;,
                        &#34;word_delimiter&#34;
                    ]
                }
            },
            &#34;filter&#34;: {
                &#34;my_pinyin&#34;: {
                    &#34;type&#34;: &#34;pinyin&#34;,
                    &#34;keep_first_letter&#34;: false,
                    &#34;keep_full_pinyin&#34;: true,
                    &#34;keep_none_chinese&#34;: true,
                    &#34;keep_none_chinese_in_first_letter&#34;: true,
                    &#34;keep_original&#34;: false,
                    &#34;limit_first_letter_length&#34;: 16,
                    &#34;lowercase&#34;: true,
                    &#34;trim_whitespace&#34;: true
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

