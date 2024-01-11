# MacOS在iTerm中使用rz、sz从远程上传下载文件


&lt;!--more--&gt;
## 安装
### 下载安装lrzsz，创建软连接（mac）

```bash
sudo brew install lrzsz

ln -s /usr/local/Cellar/lrzsz/0.12.20/bin/sz

ln -s /usr/local/Cellar/lrzsz/0.12.20/bin/rz
```

说明：lrzsz在本地和远程主机均要安装！


### 下载并安装automatic zmoderm for iTerm2

```bash
cd usr/local/bin

sudo wget https://raw.github.com/mmastrac/iterm2-zmodem/master/iterm2-send-zmodem.sh

sudo wget https://raw.github.com/mmastrac/iterm2-zmodem/master/iterm2-recv-zmodem.sh

sudo chmod 777 /usr/local/bin/iterm2-*
```

脚本地址：[https://github.com/mmastrac/iterm2-zmodem](https://github.com/mmastrac/iterm2-zmodem)


### 添加iTerm2 trigger

&gt; iTerm2 --&gt; Profiles --&gt; Open Profiles --&gt; Edit Profiles --&gt; Advanced --&gt; Edit Trigger

配置项：

| Regular expression    | Action               | Parameters                           |
| --------------------- | -------------------- | ------------------------------------ |
| `\*\*B0100`           | Run Silent Coprocess | /usr/local/bin/iterm2-send-zmodem.sh |
| `\*\*B00000000000000` | Run Silent Coprocess | /usr/local/bin/iterm2-recv-zmodem.sh |

## 使用方法

### 将文件传到远端服务器

1. 在远端服务器上输入 `rz` ，回车；
2. 选择本地要上传的文件；
3. 等待上传；


### 从远端服务器下载文件

1. 在远端服务器输入`sz filename filename1 … filenameN`；
2. 选择本地的存储目录；
3. 等待下载；


---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/mac/macos%E5%9C%A8iterm%E4%B8%AD%E4%BD%BF%E7%94%A8rzsz%E4%BB%8E%E8%BF%9C%E7%A8%8B%E4%B8%8A%E4%BC%A0%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6/  

