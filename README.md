# Wuhan-Liaoning-VirusMap
自动爬取辽宁省卫健委网站并获取数据，生成疫情地图，并可以自动上传至FTP。

一定要安装 pyecharts==0.1.9.4 才能运行！！！！这个非常重要，现在安装的新版本完全跑不起来

python3.8环境，按理说3.X皆可。

另外还需要安装bs4。

FTP的语句被注释掉了，按需使用。

辽宁卫健委的网站需要使用.decode('gb2312')进行解码。其他省的网站不一定相同，可以尝试'utf-8'编码。

如果你足够闲的话可以修改为其他省份。

数据全部来自于官方，本人不负额外责任。随缘更新。
