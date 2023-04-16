# SSH免密登录CentOS7


<!--more-->


## 本机传送id_rsa.pub

```bash
$ scp .ssh/id_rsa.pub user@ip:/root/id_rsa.pub
```

## 服务器

```bash
$ cat id_rsa.pub >> .ssh/authorized_keys
$ chmod 700 .ssh
$ chmod 600 .ssh/authorized_keys

```

## 服务器额外配置（centos7.4以下）

```bash
$ vim /etc/ssh/sshd_config
```

> 如下配置，7.4及更高版本不需要

```markdown
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```

## 重启服务

```bash
$ service ssh restart
```

## 本机登录

### 方式一：用户名@IP

```bash
$ ssh user@ip
```

### 方式二：别名

配置`.ssh/config`

```markdown
Host xxx # 别名
Hostname xxx.xxx.xxx.xxx # ip
Port 22
User xxx # 用户名
IdentityFile ~/.ssh/id_rsa
```

```bash
$ ssh xxx
```



---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/server/ssh%E5%85%8D%E5%AF%86%E7%99%BB%E5%BD%95centos7/  

