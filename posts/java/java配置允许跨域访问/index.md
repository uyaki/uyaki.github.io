# Java配置允许跨域访问


<!--more-->

## 方案
H5中的新特性：Cross-Origin Resource Sharing（跨域资源共享）。通过它，我们的开发者（主要指后端开发者）可以决定资源是否能被跨域访问。

cors是一个w3c标准，它允许浏览器（目前ie8以下还不能被支持）像我们不同源的服务器发出xmlHttpRequest请求，我们可以继续使用ajax进行请求访问。
## 配置文件
com.noone.springbootframeworkdaily.common.config.CorsConfig
```java
package com.noone.springbootframeworkdaily.common.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.web.filter.CorsFilter;

/**
 * 跨域请求设置
 * @author noone
 */
@Configuration
public class CorsConfig {
    private CorsConfiguration buildConfig(){
        CorsConfiguration corsConfiguration = new CorsConfiguration();
        corsConfiguration.addAllowedHeader("*");
        corsConfiguration.addAllowedOrigin("*");
        corsConfiguration.addAllowedMethod("*");
        return corsConfiguration;
    }
    @Bean
    public CorsFilter corsFilter() {
        UrlBasedCorsConfigurationSource source =new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**",buildConfig());
        return new CorsFilter(source);
    }
}

```


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/java/java%E9%85%8D%E7%BD%AE%E5%85%81%E8%AE%B8%E8%B7%A8%E5%9F%9F%E8%AE%BF%E9%97%AE/  

