# Alice's LHCX Fishing Pro

灵魂潮汐自动钓鱼脚本进阶版, 制作不易, 各位大佬下载前请先点个Star

**本脚本仅供学习交流使用! 完全开源免费! 请勿用于非法用途!打击倒卖狗！ **

**本脚本遵守GPL-3.0协议, 请勿从其他任何非官方(Github)途径下载该脚本! ( ｀д′)**

* **前置开发项目与详细说明 [点我](https://github.com/sixone-Jiang/LHCXAutoFishingScripts)**

**新增功能**&修改:

+ [ √ ] **后台钓鱼**，可以将钓鱼窗口最小化，运行的同时解放你的电脑使用，爽歪歪！
+ [ √ ] **去除ROOT权限**，现在不需要在管理员命令行里使用啦！
+ [ √ ] 算法速度提升，稳定处理彩鱼（别较真，钓彩鱼竿怎么也得1800的吧）
+ [ √ ] 保证模拟器大小为1280*720,  模拟器无需自动定位，只需修改配置文件中的**adb_host_port**
+ [ √ ] 删除了窗口名称
+ **环境配置**方式有所修改，请仔细观看！！

**提醒** 现在需要配置的文件仅有config.ini, 请**仔细**阅读该文件中的一切注释

* 但如果有自选鱼饵的要求，请按照main.py中的注释修改**baits_list** 变量
* 终止条件，现在终止只能Ctrl Z或C关掉命令行了

**脚本还在完善中, 配置和运行方式都可能会(向着更简便更合理的方向)改变！！！
因此使用者每次更新代码请关注该文档的更新，运行时遇到错误先查阅文档说明，也可在issues中请求帮助。**



## 使用指导

* 如看了指导后依旧不清楚，请先阅读前置项目的README

1. 下载本代码，并*解压* 到一个不带中文路径的目录，下面是一个例子，具体路径以你自己配置的为准

   ![1662116269586](https://raw.githubusercontent.com/sixone-Jiang/Picgo/main/img/1662116269586.png)
   
2. 安装miniconda在你的电脑上：

   前往 [miniconda](https://docs.conda.io/en/latest/miniconda.html) ，选择下面的安装包，这有一篇教学请点击此并仔细阅读([点这里](https://www.quanxiaoha.com/conda/install-miniconde.html))

   ![image-20220822213925039](https://raw.githubusercontent.com/sixone-Jiang/Picgo/main/img/image-20220822213925039.png)
   
3. 安装好后，您在任意命令行中输入conda init,命令行会输出一些正确反馈

4. 打开命令行(无需管理员权限)

5. 切换到本代码的工作目录(百度搜素如何在命令行切换工作目录（也就是你能找main.py文件的路径位置）)：

6. 之后配置环境，输入命令如下（一行一行的输入）：

```shell
conda create -n lhcx python=3.10 -y
conda activate lhcx
pip install -r requirements.txt
```

**temp**：[注：该步骤仅在**第一次**构建运行本项目时需要（**必要**）]：

打开模拟器，命令行切换到带有文件adb.exe的目录下（adb/）

输入命令行如下：(127.0.0.1:7555可以替换为你想要连接的设备ID，这里时mumu模拟器默认值)

```shell
adb.exe connect 127.0.0.1:7555
python -m uiautomator2 init
```

7. 打开灵魂潮汐，并切换到钓鱼界面，命令行路径切换回有main.py文件的路径，执行以下命令：

```
python main.py
```



## 效果展示：

见[bilibili](https://www.bilibili.com/video/BV1Qg41167C2/?vd_source=fd58b54cc00f8fdcc9c5eb4422b3eefd),如果失效请搜索个人主页：**ET丨Alice**

钓鱼妙法：**建议图鉴哥必看**    [Bwiki](https://wiki.biligame.com/lhcx/%E5%AE%B6%E5%9B%AD%E9%92%93%E9%B1%BC%E6%95%B0%E6%8D%AE%E4%B8%80%E8%A7%88)