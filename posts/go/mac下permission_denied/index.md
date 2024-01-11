# Mac下go访问时出现permission_denied


&lt;!--more--&gt;
# 解决 open /usr/local/go/pkg/darwin_amd64/runtime/cgo.a: permission denied

```bash
$ sudo chown -R [用户名] /usr/local/go/pkg/darwin_amd64/
$ whoami
uyaki
$ sudo chown -R uyaki /usr/local/go/pkg/darwin_amd64/
```


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/go/mac%E4%B8%8Bpermission_denied/  

