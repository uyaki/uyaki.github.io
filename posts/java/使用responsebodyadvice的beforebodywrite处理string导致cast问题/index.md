# 使用ResponseBodyAdvice的beforeBodyWrite处理String导致cast问题


<!--more-->
## 问题

配置全局返回时

```java
@Configuration
public class GlobalReturnConfig {
    @RestControllerAdvice(basePackages = "com.benyuan")
    static class ResultResponseAdvice implements ResponseBodyAdvice<Object> {
        @Override
        public boolean supports(MethodParameter methodParameter, Class<? extends HttpMessageConverter<?>> aClass) {
            return true;
        }

        @Override
        public Object beforeBodyWrite(Object body, MethodParameter methodParameter, MediaType mediaType, Class<? extends HttpMessageConverter<?>> aClass, ServerHttpRequest serverHttpRequest, ServerHttpResponse serverHttpResponse) {
            if (body instanceof ResponseDTO) {
                return body;
            }
            return ResponseDTOUtil.success(body);
        }
    }

}
```

beforeBodyWrite方法在处理String类型返回值的时候，会造成ResponseDTO can not be cast to String的BUG

## 解决

```java
/**
 * 使用RestControllerAdvice的beforeBodyWrite方法时，在处理String时，实际处理的HttpMessageConverter，应该是MappingJackson2HttpMessageConverter
 * @Description
 */
@Configuration
public class WebConfiguration implements WebMvcConfigurer {
    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        // 0-1可配，2-8是默认加载的
        converters.add(0, new MappingJackson2HttpMessageConverter());
    }
}
```


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/java/%E4%BD%BF%E7%94%A8responsebodyadvice%E7%9A%84beforebodywrite%E5%A4%84%E7%90%86string%E5%AF%BC%E8%87%B4cast%E9%97%AE%E9%A2%98/  

