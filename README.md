# MacOS-Plugins
一款专门为Mac OS 11开发的程序员快捷工具

## :zap:初始化仓库

1. 下载`mop.py`的最新版本
2. 在一个你**不会删除**的地方创建一个文件夹
3. 将*mop.py*放进去
4. 打开终端，`cd`到上面创建的文件夹
5. 运行`python3 mop.py -init install`根据提示完成安装

## :earth_asia:切换语言

目前提供两种语言: 中文、英文<br>
使用`mop -language cn`或者`mop -language en`更换语言<br>
**注意**: 语言为全局设置，会改变**所有**插件语言

## :calling:安装插件

1. 可以在`packet.json`文件中查看支持的MOP插件，或者浏览**MOP仓库**<br>
2. 在电脑上运行`mop -install <plugin_name>`，不区分大小写
3. 根据提示安装
4. 你会获得一个快捷指令，例如`prm`
5. 可以使用`prm -h`查看插件的命令
