# Mysql修改Auto_increment


&lt;!--more--&gt;
## 查看 

```sql
select auto_increment from information_schema.tables where table_schema=&#39;xxx_db&#39; and table_name=&#39;xxx&#39;; 
```

## 修改

```sql
alter table xxx_db.xxx auto_increment=1000;
```

&gt; 坑：假设表中有ID大于你设置的值如1000，修改将不会生效



---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/java/mysql%E4%BF%AE%E6%94%B9auto_increment/  

