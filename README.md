# MacOS-Plugins

> 一款专门为Mac OS 11开发的程序员快捷工具<br>

![GitHub release (latest by date)](https://img.shields.io/github/v/release/underthestars-zhy/MacOS-Plugins)
![GitHub](https://img.shields.io/github/license/underthestars-zhy/MacOS-Plugins)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/underthestars-zhy/MacOS-Plugins)
![GitHub all releases](https://img.shields.io/github/downloads/underthestars-zhy/MacOS-Plugins/total)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/underthestars-zhy/MacOS-Plugins)
![GitHub Repo stars](https://img.shields.io/github/stars/underthestars-zhy/MacOS-Plugins?style=social)

## :zap: 初始化仓库

1. 下载`mop.py`的最新版本
2. 在一个你**不会删除**的地方创建一个文件夹
3. 将*mop.py*放进去
4. 打开终端，`cd`到上面创建的文件夹
5. 运行`python3 mop.py -init install`根据提示完成安装

## :earth_asia: 切换语言

目前提供两种语言: 中文、英文<br>
使用`mop -language cn`或者`mop -language en`更换语言<br>
**注意**: 语言为全局设置，会改变**所有**插件语言

## :calling: 安装插件

1. 可以在`packet.json`文件中查看支持的MOP插件，或者浏览**MOP仓库**<br>
2. 在电脑上运行`mop -install <plugin_name>`，不区分大小写
3. 根据提示安装
4. 你会获得一个快捷指令，例如`prm`
5. 可以使用`prm -h`查看插件的命令

## :octocat: 查看插件说明

1. 使用`mop -readme <plugin_name>`查看插件说明
2. 若插件不支持README，则会出错
3. README语言和你设置的MOP语言有关

## :postbox: 计划

- [ ] 重构下载代码
- [ ] 重构更新代码
- [ ] 支持删除插件
- [X] ~支持更新插件~
- [ ] 重构json URL
- [ ] 支持轻应用(Golang实现)

## :globe_with_meridians: 推荐插件

+ 轻松**快照**文件: [sync](https://github.com/underthestars-zhy/sync-tools)
+ 按照自己喜欢的方式**重命名**文件: [re_name tools](https://github.com/underthestars-zhy/MOP-ReName-Tools)
+ 下载**YouTube**视频: [tubedown](https://github.com/underthestars-zhy/tubedown)
