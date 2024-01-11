# Alist&#43;Aria2Pro&#43;AriaNg实现网盘聚合


&lt;!--more--&gt;

## 前置准备

- [ ] 你的服务器、主机上需安装Docker和Docker Compose

## 部署

### 编写docker-compose.yml

```bash
mkdir -p ${your-docker-script-path}/alist
cd ${your-docker-script-path}/alist
vim docker-compose.yml
```

```yaml
//TODO
```

### 启动
```bash
docker-compose up -d
```

## 设置

### IP 地址与端口

{{&lt; admonition tip &gt;}}
最好不要用localhost或127.0.0.1来访问，否则两者之间的连接会出现问题，请使用主机的局域网IP来访问。
{{&lt; /admonition &gt;}}

以下是各种应用的访问端口，请将`${IP}`替换成你docker主机的IP地址：
| APP       | URL                 |
| --------- | ------------------- |
| Alist     | `http://${IP}:5244` |
| Aria2 RPC | `http://${IP}:6800` |
| AriaNg    | `http://${IP}:6880` |

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/opensource/alist&#43;aria2pro&#43;ariang%E5%AE%9E%E7%8E%B0%E7%BD%91%E7%9B%98%E8%81%9A%E5%90%88/  

