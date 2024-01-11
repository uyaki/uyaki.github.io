# SSH使用pem文件远程登陆


&lt;!--more--&gt;

## 方式一：

1. 修改pem权限；

   ```bash
   sudo chmod 600 key.pem
   ```

2. Mac OS 连接服务器使用 PEM 文件；

   ```bash
   ssh -i key.pem root@IP
   ```

## 方式二（Mac重启后失效）：

1. 使用ssh-add添加key文件；

   ```bash
   ssh-add -k key.pem  
   ```

2. 登陆；

   ```bash
   ssh root@IP
   ssh -p xxxx root@IP
   ```


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/server/ssh%E4%BD%BF%E7%94%A8pem%E6%96%87%E4%BB%B6%E8%BF%9C%E7%A8%8B%E7%99%BB%E9%99%86/  

