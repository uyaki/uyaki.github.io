# Clashforlinux


<!--more-->

## 安装clash

1. 对于 Ubuntu 一般使用 clash-linux-amd64 版本，下载clash

```bash
wget latest_url
```

{{</* admonition tip */>}}
如果直接 wget 速度较慢的话，可以本地下载完成后，使用 SFTP、SCP等方式 上传到 Linux 服务器。
{{</* /admonition */>}}

{{</* admonition note */>}}
2024/01/11 clash 的github项目[Dreamacro/clash](https://github.com/Dreamacro/clash/releases)为了紧急避险，目前已经删库跑路，之后是否会恢复有待观察。虽然github没了，但是网上还是有很多交流学习自用的，懂的都懂。
{{</* /admonition */>}}


1. 解压 重命名为`clash`
```bash
# 解压
gunzip clash-linux-amd64-latest.0.gz
# 重命名
mv clash-linux-amd64-latest clash

# 如需开机自启动，将 clash 移动到 /usr/bin/ 目录下，下文演示按此路径演示
mv clash-linux-amd64-latest /usr/bin/clash
```
3. 赋予可执行权限
```bash
sudo chmod +x /usr/bin/clash
```
4. 下载Country.mmdb 文件：当第一次启动 Clash 时（使用 `./clash` 命令） 会自动下载（会下载至 `$HOME/.config/clash` 文件夹下）。自动下载可能会因网络原因较慢，可以访问[Dreamacro/maxmind-geoip](https://github.com/Dreamacro/maxmind-geoip/releases)手动下载，上传到`$HOME/.config/clash`文件夹下
> `Country.mmdb` 文件利用 GeoIP2 服务能识别互联网用户的地点位置，以供规则分流时使用。

5. 检查clash是否安装成功
```bash
clash -v
```

## 配置文件
一般的网络服务提供了 Clash 订阅链接，可以直接下载链接指向的文件内容，保存到 config.yaml 中。或者使用订阅转换服务（如该[链接](https://sub-web.netlify.app/），将其它订阅转换为 Clash 订阅。
这里推荐使用订阅转换服务，转换后的配置文件已添加更为强大的分流规则。就可以将 Clash 一直保持后台运行，自动分流，且会自动选择最优节点。
如果使用订阅转换服务，对于转换后的订阅链接，可以使用以下命令来下载配置文件：
```bash
curl -o config.yaml 'longURL'
```
对于 suo.yt 短链接，需要重定向，因此使用以下命令来下载配置文件：
```bash
curl -L -o config.yaml 'shortURL'
```

## Clash as a daemon
将 Clash 转变为系统服务，从而使得 Clash 实现常驻后台运行、开机自启动等。
1. 配置 systemd 服务。在 `/lib/systemd/system/` 目录下创建 `clash@.service` 文件
```bash
sudo vim /lib/systemd/system/clash@.service
```
写入以下内容(不用修改)并保存:
```
[Unit]
Description=A rule based proxy in Go for %i.
After=network.target

[Service]
Type=simple
User=%i
Restart=on-abort
ExecStart=/usr/bin/clash

[Install]
WantedBy=multi-user.target
```
2. 重新加载 systemd 模块
```bash
systemctl daemon-reload
```
3. 启动 clash 服务
```bash
systemctl start clash@uyaki
```
4. 设置开机自启
```bash
systemctl enable clash@uyaki
```
## 使用

利用 Export 命令使用代理。Clash 运行后，其在后台监听某一端口。Ubuntu 下使用代理，需要 export 命令。根据 config 配置文可以查看到件Clash 代理端口（订阅转换后，端口为7890），设置系统代理命令为：
```bash
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7890
```
可以将该命令添加到 `~/.bashrc` 或 `~/.zshrc` 中，登陆后该用户自动开启代理。

取消系统代理：
```bash
unset  http_proxy  https_proxy  all_proxy
```
当然，为了方便启动，可以设置成函数
### bash or zsh
`vim ~/.bashrc`或`vim ~/.zshrc`
```bash
proxy () {
  export http_proxy="http://127.0.0.1:7890"
  export https_proxy="http://127.0.0.1:7890"
  export all_proxy="socks5://127.0.0.1:7890"
  echo "HTTP Proxy on"
}

# where noproxy
noproxy () {
  unset http_proxy
  unset https_proxy
  unset all_proxy
  echo "HTTP Proxy off"
}
```
记得 `source ~/.bashrc` 或 `source ~/.zshrc` 一下

### fish
```bash
vim  ~/.config/fish/functions/proxy.fish
```
```fish
function proxy
  set -xg all_proxy socks5://127.0.0.1:7890
  set -xg http_proxy http://127.0.0.1:7890
  set -xg https_proxy http://127.0.0.1:7890
  echo "Clash Proxy:ON"
end
```
```bash
vim ~/.config/fish/functions/noproxy.fish
```
```fish
function noproxy
  set -e all_proxy
  set -e http_proxy
  set -e https_proxy
  echo "Clash Proxy:OFF"
end
```

### 开启 & 关闭
- 开启
```bash
proxy
```
- 关闭
```bash
noproxy
```

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/proxy/clashforlinux/  

