# Steam如何绕过clash的全局代理


&lt;!--more--&gt;
## 设置bypass

`Clash` -&gt; `Settings` -&gt; `System Proxy` -&gt; `Bypass Domain/IPNet`

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
  - &lt;local&gt;
  - &#34;*.bing.com&#34;
  - &#34;*.microsoft.com&#34;
  - &#34;*.bing.com&#34;
  - &#34;*.microsoft.com&#34;
# Steam中国大陆地区游戏下载
  - &#34;steampipe.steamcontent.tnkjmec.com&#34; #华为云
  - &#34;st.dl.eccdnx.com&#34; #白山云
  - &#34;st.dl.bscstorage.net&#34;
  - &#34;st.dl.pinyuncloud.com&#34;
  - &#34;dl.steam.clngaa.com&#34; #金山云
  - &#34;cdn.mileweb.cs.steampowered.com.8686c.com&#34; #网宿云
  - &#34;cdn-ws.content.steamchina.com&#34;
  - &#34;cdn-qc.content.steamchina.com&#34; #腾讯云
  - &#34;cdn-ali.content.steamchina.com&#34; #阿里云
# Steam非中国大陆地区游戏下载/社区实况直播
  - &#34;*.steamcontent.com&#34;
# Battle.net战网中国大陆地区游戏下载
  - &#34;client05.pdl.wow.battlenet.com.cn&#34; #华为云
  - &#34;client02.pdl.wow.battlenet.com.cn&#34; #网宿云
# Epic Games中国大陆地区游戏下载
  - &#34;epicgames-download1-1251447533.file.myqcloud.com&#34;
# Rockstar Launcher客户端更新/游戏更新/游戏下载
  - &#34;gamedownloads-rockstargames-com.akamaized.net&#34;
```

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/windows/steam%E5%A6%82%E4%BD%95%E7%BB%95%E8%BF%87clash%E7%9A%84%E5%85%A8%E5%B1%80%E4%BB%A3%E7%90%86/  

