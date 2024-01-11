# Docker部署ES、kibana并配置ik分词


&lt;!--more--&gt;

## 1. 创建数据目录

```bash
#创建数据/日志目录 这里我们部署3个节点
$ mkdir /opt/elasticsearch/data/{es01,es02,es03} -p
mkdir /opt/elasticsearch/logs/{es01,es02,es03} -p
cd /opt/elasticsearch
#权限
chmod 0777 data/* -R &amp;&amp; chmod 0777 logs/* -R

#防止JVM报错
echo vm.max_map_count=262144 &gt;&gt; /etc/sysctl.conf
sysctl -p
```

## 2. ES集群安装

```yaml
version: &#39;2.2&#39;
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.1
    container_name: es01
    environment:
      # node名称
      - node.name=es01
      # 集群名称
      - cluster.name=es-docker-cluster
      # 节点配置
      - discovery.seed_hosts=es02,es03
      - cluster.initial_master_nodes=es01,es02,es03
      # 锁定进程的物理内存地址避免交换（swapped）来提高性能
      - bootstrap.memory_lock=true
      # 开启跨域cors，已便使用Head插件
      - http.cors.enabled=true
      - http.cors.allow-origin=*
      # Jvm内存大小配置
      - &#34;ES_JAVA_OPTS=-Xms512m -Xmx512m&#34;
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      # - data01:/usr/share/elasticsearch/data
      - ./data/es01:/usr/share/elasticsearch/data
      - ./logs/es01:/usr/share/elasticsearch/logs
    ports:
      - 9200:9200
    networks:
      - elastic
  es02:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.1
    container_name: es02
    environment:
	    # node名称
      - node.name=es02
      # 集群名称
      - cluster.name=es-docker-cluster
      # 节点配置
      - discovery.seed_hosts=es01,es03
      - cluster.initial_master_nodes=es01,es02,es03
      # 锁定进程的物理内存地址避免交换（swapped）来提高性能
      - bootstrap.memory_lock=true
      # 开启跨域cors，已便使用Head插件
      - http.cors.enabled=true
      - http.cors.allow-origin=*
      # Jvm内存大小配置
      - &#34;ES_JAVA_OPTS=-Xms512m -Xmx512m&#34;
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      # - data02:/usr/share/elasticsearch/data
      - ./data/es02:/usr/share/elasticsearch/data
      - ./logs/es02:/usr/share/elasticsearch/logs
    # 可以不开放
    ports:
      - 9201:9200
    networks:
      - elastic
  es03:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.5.1
    container_name: es03
    environment:
	    # node名称
      - node.name=es03
      # 集群名称
      - cluster.name=es-docker-cluster
      # 节点配置
      - discovery.seed_hosts=es01,es02
      - cluster.initial_master_nodes=es01,es02,es03
      # 锁定进程的物理内存地址避免交换（swapped）来提高性能
      - bootstrap.memory_lock=true
      # 开启跨域cors，已便使用Head插件
      - http.cors.enabled=true
      - http.cors.allow-origin=*
      # Jvm内存大小配置
      - &#34;ES_JAVA_OPTS=-Xms512m -Xmx512m&#34;
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      # - data03:/usr/share/elasticsearch/data
      - ./data/es03:/usr/share/elasticsearch/data
      - ./logs/es03:/usr/share/elasticsearch/logs
    # 可以不开放
    ports:
      - 9202:9200
    networks:
      - elastic

volumes:
  data01:
    driver: local
  data02:
    driver: local
  data03:
    driver: local

networks:
  elastic:
    driver: bridge
```

## 3. 启动

```bash
docker-compose up -d
```

## 4. 安装ik分词插件

```bash
// 集群
$ docker-compose exec es01 elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.5.1/elasticsearch-analysis-ik-7.5.1.zip

$ docker-compose exec es02 elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.5.1/elasticsearch-analysis-ik-7.5.1.zip

$ docker-compose exec es03 elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.5.1/elasticsearch-analysis-ik-7.5.1.zip

//然后要重启es容器
$ docker-compose restart es01
$ docker-compose restart es02
$ docker-compose restart es03
```

## 5. 构建elasticsearch-head镜像（可跳过）

```dockerfile
#Docker image of elasticsearch-head
# VERSION 6
# Author: bolingcavalry

#基础镜像使用node:10.15.0，以便通过npm来安装head插件
FROM node:10.15.0-alpine

#作者
MAINTAINER BolingCavalry &lt;zq2599@gmail.com&gt;

#定义下载源文件的路径
ENV SRC_DOWN_PATH /usr/src/app

#创建文件夹用于保存下载的源码
RUN mkdir -p $SRC_DOWN_PATH &amp;&amp; \
#进入该文件夹
cd $SRC_DOWN_PATH &amp;&amp; \
#下载源码
wget https://codeload.github.com/mobz/elasticsearch-head/zip/master &amp;&amp; \
#解压
unzip master &amp;&amp; \
#解压后，压缩文件可以删除了
rm master &amp;&amp; \
#进入解压后的文件夹
cd elasticsearch-head-master &amp;&amp; \
#设置为taobao，加速npm安装速度
npm config set registry http://registry.npm.taobao.org &amp;&amp; \
#安装grunt
npm install -g grunt-cli &amp;&amp; \
#安装head
npm install

#设置默认工作目录为解压后的源码文件夹
WORKDIR $SRC_DOWN_PATH/elasticsearch-head-master

#保留9100端口
EXPOSE 9100

#启动时即启动head服务
CMD [ &#34;grunt&#34;, &#34;server&#34; ]
```

## 6. kibana

```yaml
version: &#39;2.2&#39;
services:
  kibana:
    image: docker.elastic.co/kibana/kibana:6.0.0
    container_name: kibana
    environment: 
      - ELASTICSEARCH_URL=http://***.***.***.***:9200
    ports: 
      - 5601:5601
```

## 7. 踩坑记录

安装过程出现问题，断线，导致无法重新安装analysis-ik，也无法卸载analysis-ik

解决：

```bash
## 查看已安装插件
$ docker-compose exec es01 elasticsearch-plugin list
## 移除转一半到插件
$ docker-compose exec es01 elasticsearch-plugin remove .installing-xxxx
## TODO 重新安装
```


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/docker/docker%E9%83%A8%E7%BD%B2eskibana%E5%B9%B6%E9%85%8D%E7%BD%AEik%E5%88%86%E8%AF%8D/  

