# 解决PD的bootcamp中windows无法联网的问题


&lt;!--more--&gt;
## 解决无法联网的问题:

```bash
vim /Library/Preferences/Parallels/network.desktop.xml
```

```xml
&lt;!-- &lt;UseKextless&gt;-1&lt;/UseKextless&gt;改为 1--&gt;
&lt;UseKextless&gt;0&lt;/UseKextless&gt;
```


解决USB无法识别问题:
```bash
vim /Library/Preferences/Parallels/dispatcher.desktop.xml
```
```xml
&lt;!-- 找到 &lt;Usb&gt;0&lt;/Usb&gt; ，修改为 1 --&gt;
&lt;Usb&gt;1&lt;/Usb&gt;
```

修改后，重启 Parallels Desktop以及windows，即完美解决以上问题。

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/mac/%E8%A7%A3%E5%86%B3pd%E7%9A%84bootcamp%E4%B8%ADwindows%E6%97%A0%E6%B3%95%E8%81%94%E7%BD%91%E7%9A%84%E9%97%AE%E9%A2%98/  

