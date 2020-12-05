#! /usr/local/bin/python3
#  Copyright (c) 2020.
#  You can freely change the code part, but you must follow the MIT protocol
#  You cannot delete any information about UTS
#  You cannot use this program to disrupt social order.

# 导入模块
import argparse
import os
import shelve
import sys
import json
import webbrowser

# 常量设置
VERSION = 1.3

# 多语言设置
file_lists = os.listdir(os.path.expanduser('~'))
if 'mop.json' in file_lists:
    file = open(os.path.expanduser('~/mop.json'), 'r')
    mop_db_path = json.load(file)
    file.close()
    mop_db = shelve.open(mop_db_path + 'mop')
    plugin_list = mop_db['plugins']
    if mop_db['language'] == 'en':
        init_help = 'Initialize or update in the current folder'
        install_help = 'Installation plug-in'
        welcome = 'Welcome-MOP'
        init_error = 'Cannot be initialized multiple times'
        language_help = 'Switch language'
        language_set = 'Language changed successfully'
        http_error = 'Network JSON request error'
        plugin_find = 'Find plugins...'
        plugin_error = 'The specified plug-in can not be found!'
        plugin_file = 'Program written successfully!'
        plugin_plugins = 'Start installing the required modules'
        pip_true = 'Module installed successfully!'
        pip_nothing = 'There are no modules to install!'
        plugin_command = 'Plugin Command: '
        successful = 'success'.upper()
        update_text = 'Start the update'
        update_init = 'Version is up to date, please do not install low version!'
        update_file_success = 'The update file was successfully retrieved'
        update_find = 'FIND THE UPDATE FILE!'
        readme_help = 'View the plugin help'
        welcome_flag = False
        url_help = 'Modify the download URL of the json file'
        url_error = 'The URL could not be queried'
        update_help = 'Update Plugin'
        url_arg_error = 'Unable to Parse instruction. Do you want to see the help documentation?'
        install_re_install = 'This plug-in has been downloaded and can not be downloaded repeatedly'
    elif mop_db['language'] == 'cn':
        init_help = '初始化或者更新当前文件夹'
        install_help = '安装插件'
        welcome = '欢迎使用MOP'
        init_error = '不能多次初始化'
        language_help = '更改语言'
        language_set = '更换语言成功'
        http_error = '网络JSON请求出错'
        plugin_find = '查找到插件...'
        plugin_error = '查找不到指定插件!'
        plugin_file = '程序写入成功!'
        plugin_plugins = '开始安装需要的模块'
        pip_true = '模块安装成功!'
        pip_nothing = '没有需要安装的模块!'
        db_set_true = '数据库设置完成!'
        db_set_nothing = '没有数据库任务!'
        plugin_command = '插件命令: '
        successful = '完成'
        update_text = '开始更新'
        update_init = '版本已经是最新,请勿安装低版本!'
        update_file_success = '成功获取更新文件'
        update_find = '查找到更新文件!'
        readme_help = '查看插件帮助'
        welcome_flag = False
        url_help = '修改json文件的下载URL'
        update_help = '更新插件'
        url_error = '无法查询到相应URL'
        url_arg_error = '无法解析指令，是否需要查看帮助文档?'
        install_re_install = '此插件已经下载，不能重复下载'
    mop_db.close()
    mop_db_file = True
else:
    mop_db_file = False
    welcome_flag = True
    init_help = 'Initialize or update in the current folder'
    install_help = 'Installation plug-in'
    welcome = 'Welcome-MOP\nYou need to initialize the warehouse first'
    language_help = 'Switch language'
    not_init_set_error = 'Please initialize first'
    readme_help = 'View the plugin help'
    url_help = 'Modify the download URL of the json file'
    update_help = 'Update Plugin'

# 命令参数设置
parser = argparse.ArgumentParser(description='MacOS 11 Plugins Install Tool')

parser.add_argument('-init', type=str, help=init_help, choices=['install', 'update', 'uninstall'], nargs=1)  # 初始化/更新命令
parser.add_argument('-install', type=str, help=install_help, nargs=1)  # 安装命令
parser.add_argument('-language', type=str, help=language_help, nargs=1, choices=['en', 'cn'])  # 更换语言
parser.add_argument('-readme', type=str, help=readme_help, nargs=1)  # 查看插件帮助
parser.add_argument('-url', type=str, help=url_help, nargs=1, choices=plugin_list)  # 更新URL
parser.add_argument('-update', type=str, help=update_help, nargs=1)  # 更新插件
parser.add_argument('-clip', type=str, help=update_help, nargs=1)  # 安装轻app

args = parser.parse_args()

# 欢迎
if welcome_flag:
    print(welcome)

# 初始化/更新
if args.init:
    if args.init[0] == 'install':

        mop_db = shelve.open('mop')
        mop_db['version'] = VERSION # 设置当前版本

        print('initializing...'.upper())

        try:
            import resource
        except:
            os.system('pip3 install resource')
        mop_db['resource'] = True

        print('resource installed successfully...')
        print('create Shortcut...')

        file = open(os.path.expanduser('~/.zshrc'), 'a')
        file.write('alias mop="python3 ' + os.path.abspath('.') + '/mop.py"\n')
        file.close()

        print('选择语言|Choose a language')
        print('en or cn')
        mop_db['language'] = input('Language/语言: ')
        language = mop_db['language']

        mop_db['json_url'] = 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/packet.json'
        mop_db['url_sets'] = {
            "main": 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/packet.json',
            "main_cdn": 'https://cdn.jsdelivr.net/gh/underthestars-zhy/MacOS-Plugins/packet.json'
        }
        mop_db['plugins'] = ['all']

        mop_db.close()

        file = open(os.path.expanduser('~/mop.json'), 'w')  # 为后续获取DB数据库路径做准备
        path_ = os.path.abspath('.') + '/'
        json.dump(path_, file, indent=4)
        file.close()

        if language == 'en':
            print('success'.upper())
        elif language == 'cn':
            print('成功')
    if args.init[0] == 'update' and mop_db_file:
        pass


# 语言设置
if args.language:
    if args.language[0] == 'en':
        if mop_db_file:
            mop_db = shelve.open(mop_db_path + 'mop')
            mop_db['language'] = 'en'
            mop_db.close()
            print(language_set)
        else:
            print(not_init_set_error)
    elif args.language[0] == 'cn':
        if mop_db_file:
            mop_db = shelve.open(mop_db_path + 'mop')
            mop_db['language'] = 'cn'
            mop_db.close()
            print(language_set)
        else:
            print(not_init_set_error)

# 安装插件
if args.install and mop_db_file:
    mop_db = shelve.open(mop_db_path + 'mop') # 打开数据库

    plugins_list = mop_db['plugins'] # 获取插件列表
    down_plugin_list = [] # 需要下载的插件列表

    for plugin_name in args.install:  # 遍历所有传入的插件
        if plugin_name in plugins_list:
            print(install_re_install + ' => ' + plugin_name)
        else:
            down_plugin_list.append(plugin_name)

    import resource # 加载json文件下载模块


# 查看插件README
if args.readme and mop_db_file:
    print(args.readme[0] + '-README')
    mop_db = shelve.open(mop_db_path + 'mop')
    if mop_db['language'] == 'en':
        print(mop_db[args.readme[0] + '_readme_en'])
    else:
        print(mop_db[args.readme[0] + '_readme_cn'])


# 修改json文件url
if args.url and mop_db_file:

    # 新增url
    if args.url[0] == 'n': # 新增自定义URL
        new_url = input('URL: ') # 输入URL
        new_url_name = input('Name: ') # 输入名称

        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets']) # 加载数据库字典到本地
        url_dict[new_url_name] = new_url
        mop_db['url_sets'] = url_dict # save

        print(successful)
    elif args.url[0] == 'd': # 删除自定义URL
        del_url_name = input('Name: ') # 输入删除链接的名称

        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets']) # 加载数据库字典到本地

        if del_url_name not in url_dict.keys():
            print(url_error)
            sys.exit()

        del url_dict[del_url_name] # 删除链接
        mop_db['url_sets'] = url_dict # save

        print(successful)
    elif args.url[0] == 'e': # 修改自定义URL
        edit_url_name = input('Name: ')  # 输入需要修改自定义URL的名称
        edit_url = input('NewUrl: ') # 新URL

        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地

        if edit_url_name not in url_dict.keys():
            print(url_error)
            sys.exit()

        url_dict[edit_url_name] = edit_url # 更新URL

        mop_db['url_sets'] = url_dict  # save

        print(successful)
    elif args.url[0] == 'l': # 列出所有URL
        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地
        mop_db['url_sets'] = url_dict  # 关闭数据库

        for name, url in url_dict:
            print(name + ' => ' + url)
    else:
        print(url_arg_error)
        if input('y/n> ').lower() == 'y':
            webbrowser.open('https://mop.uts.ski/#/json_url') # 打开帮助文档
        else:
            sys.exit() # 退出程序

# 更新插件
if args.update and mop_db_file:
