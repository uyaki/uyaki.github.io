# Steam如何绕过clash的全局代理


<!--more-->
## 设置bypass

`Clash` -> `Settings` -> `System Proxy` -> `Bypass Domain/IPNet`

```yml
bypass:
  - localhost
  - 127.*
  - 10.*
  - 172.16.*
  - 172.17.*
  - 172.18.*
  - 172.19.*
  - 172.20.*
  - 172.21.*
  - 172.22.*
  - 172.23.*
  - 172.24.*
  - 172.25.*
  - 172.26.*
  - 172.27.*
  - 172.28.*
  - 172.29.*
  - 172.30.*
  - 172.31.*
  - 192.168.*
  - <local>
  - "*.bing.com"
  - "*.microsoft.com"
  - "*.bing.com"
  - "*.microsoft.com"
# Steam中国大陆地区游戏下载
  - "steampipe.steamcontent.tnkjmec.com" #华为云
  - "st.dl.eccdnx.com" #白山云
  - "st.dl.bscstorage.net"
  - "st.dl.pinyuncloud.com"
  - "dl.steam.clngaa.com" #金山云
  - "cdn.mileweb.cs.steampowered.com.8686c.com" #网宿云
  - "cdn-ws.content.steamchina.com"
  - "cdn-qc.content.steamchina.com" #腾讯云
  - "cdn-ali.content.steamchina.com" #阿里云
# Steam非中国大陆地区游戏下载/社区实况直播
  - "*.steamcontent.com"
# Battle.net战网中国大陆地区游戏下载
  - "client05.pdl.wow.battlenet.com.cn" #华为云
  - "client02.pdl.wow.battlenet.com.cn" #网宿云
# Epic Games中国大陆地区游戏下载
  - "epicgames-download1-1251447533.file.myqcloud.com"
# Rockstar Launcher客户端更新/游戏更新/游戏下载
  - "gamedownloads-rockstargames-com.akamaized.net"
```

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/windows/steam%E5%A6%82%E4%BD%95%E7%BB%95%E8%BF%87clash%E7%9A%84%E5%85%A8%E5%B1%80%E4%BB%A3%E7%90%86/  

