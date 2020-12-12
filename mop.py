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
VERSION = 1.32

# 多语言设置
file_lists = os.listdir(os.path.expanduser('~'))
if 'mop.json' in file_lists:
    file = open(os.path.expanduser('~/mop.json'), 'r')
    mop_db_path = json.load(file)
    file.close()
    mop_db = shelve.open(mop_db_path + 'mop')
    LANGUAGE = mop_db['language']
    plugin_list = list(mop_db['plugins'])  # 获得插件列表(为update提供)
    plugin_list.append('all')  # 更新所有
    remove_plugin_list = list(mop_db['plugins'])  # remove占用
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
        install_no_down_plugins = 'There are no plugins to download'
        install_soon = 'Download soon: '
        url_del_def_error = 'Deleting the default URL is not allowed'
        url_def_not_in = 'The URL can not be found in the URL list'
        url_new_error = 'Duplicate Custom URLS are not allowed to be created'
        install_url_success = 'Url request successful'
        install_now = 'Start the installation=> '
        readme_error = 'Unable to find: '
        clip_help = 'install clip app'
        remove_help = 'Delete app'
        clip_arg_error = 'Incoming parameter error'
        clip_find_error = 'Unable to find clip app'
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
        install_no_down_plugins = '没有要下载的插件'
        install_soon = '即将下载: '
        url_del_def_error = '不允许删除默认URL'
        url_def_not_in = '无法在URL列表找到相应URL'
        url_new_error = '不允许创建重复自定义URL'
        install_url_success = 'URL请求成功'
        install_now = '开始安装=> '
        readme_error = '无法找到: '
        clip_help = '安装轻app'
        remove_help = '删除app'
        clip_arg_error = '传入参数错误'
        clip_find_error = '无法找到clip app'
    mop_db.close()
    mop_db_file = True
else:
    clip_help = 'install clip app'
    plugin_list = []
    remove_plugin_list = []
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
    remove_help = 'Delete app'

# 命令参数设置
parser = argparse.ArgumentParser(description='MacOS 11 Plugins Install Tool')

parser.add_argument('-init', type=str, help=init_help, choices=['install', 'update', 'uninstall'], nargs=1)  # 初始化/更新/卸载命令
parser.add_argument('-install', type=str, help=install_help, nargs='*')  # 安装命令
parser.add_argument('-language', type=str, help=language_help, nargs=1, choices=['en', 'cn'])  # 更换语言
parser.add_argument('-readme', type=str, help=readme_help, nargs='*')  # 查看插件帮助
parser.add_argument('-url', type=str, help=url_help, nargs=1)  # 更新URL
parser.add_argument('-update', type=str, help=update_help, nargs='*', choices=plugin_list)  # 更新插件
parser.add_argument('-clip', type=str, help=clip_help, nargs='*')  # 安装轻app
parser.add_argument('-remove', type=str, help=remove_help, nargs='*', choices=remove_plugin_list)  # 删除app

args = parser.parse_args()

# 欢迎
if welcome_flag:
    print(welcome)

# 初始化/更新
if args.init:
    if args.init[0] == 'install':

        mop_db = shelve.open('mop')
        mop_db['version'] = VERSION  # 设置当前版本

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
        mop_db['plugins'] = []
        mop_db['db_name'] = {}  # 数据库前缀表

        mop_db.close()

        file = open(os.path.expanduser('~/mop.json'), 'w')  # 为后续获取DB数据库路径做准备
        path_ = os.path.abspath('.') + '/'
        json.dump(path_, file, indent=4)
        file.close()

        if language == 'en':
            print('success'.upper())
            print('Please reboot the terminal')
        elif language == 'cn':
            print('成功')
            print('请重启终端')
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
    mop_db = shelve.open(mop_db_path + 'mop')  # 打开数据库

    plugins_list = mop_db['plugins']  # 获取插件列表
    down_plugin_list = []  # 需要下载的插件列表
    down_url = mop_db['json_url']  # json文件URL
    url_dict = mop_db['url_sets']  # jsonURL字典

    for plugin_name in args.install:  # 遍历所有传入的插件
        if str(plugin_name).lower().startswith('url:'):
            url_name = str(plugin_name).split(':')[1]  # url名称
            down_url = url_dict[url_name]  # 更新json文件URL

            continue  # 返回

        if plugin_name in plugins_list:  # 检查插件是否已经下载过
            print(install_re_install + ' => ' + plugin_name)  # 错误信息
        else:
            down_plugin_list.append(plugin_name)  # 将文件添加到下载列表

    if not down_plugin_list:  # 检测下载列表是否为空
        print('\n' + install_no_down_plugins + '\n')
        sys.exit()  # 空则退出程序

    print('\n-----------------------\n')  # 分割线

    for plugin_name in down_plugin_list:  # 输出所有要下载的插件名称
        print(install_soon + plugin_name)

    print('\n-----------------------\n')  # 分割线

    import requests  # 加载json文件下载模块

    packet_r = requests.get(down_url)  # 获取一个下载对象

    print('URL: ' + down_url)  # 输出下载URL

    packet_r.raise_for_status()  # 检测链接有效性
    print(install_url_success)

    packets_dict = dict(packet_r.json())  # 将json内容保存

    packet_r.close()  # 关闭下载对象

    for packet_name in down_plugin_list:
        print('\n-----------------------\n')  # 分割线
        print(install_now + packet_name)

        if packet_name not in packets_dict.keys():  # 检测当前下载插件是否在下载字典中
            print(plugin_error)
            continue
        else:
            print(plugin_find)

        packet_dict = packets_dict[packet_name]  # 保存插件字典

        packet_type = 'text'  # 设置默认类型
        try:
            packet_type = packet_dict['type']
        except:
            pass

        if packet_type == 'text':
            packet_command = packet_dict['command']
        elif packet_type == 'clip':
            if str(mop_db['language']) == 'en':
                print('不能下载clip app')
            else:
                print('Can’t download clip app')
            continue
        else:
            packet_command = ''

        packet_url = packet_dict['url']  # 插件下载URL
        packet_file_name = packet_dict['file_name']  # 插件保存文件名
        packet_code_language = packet_dict['code_language']  # 插件语言
        packet_code_language_version = packet_dict['code_language_version']  # 插件语言所需版本
        packet_alias = packet_dict['alias']  # 插件别名
        packet_version = packet_dict['version']  # 插件版本
        packet_pip = packet_dict['pip']  # 插件模块列表
        packet_db_name = packet_dict['db_name']  # 插件数据库前缀
        packet_db_set = packet_dict['db_set']  # 插件数据库设置
        packet_readme_cn = packet_dict['readme_cn']  # 插件介绍中文
        packet_readme_en = packet_dict['readme_en']  # 插件介绍英文

        # 信息输出
        print('- Download link: ' + str(packet_url))
        print('- Save file name: ' + str(packet_file_name))
        print('- Code language: ' + str(packet_code_language))
        print('- Required language version: ' + str(packet_code_language_version))
        print('- Plug-in alias: ' + str(packet_alias))
        print('- Plugin version: ' + str(packet_version))
        print('- packet_version: ' + str(packet_pip))
        print('- Database prefix name: ' + str(packet_db_name))
        print('- Database operation: ' + str(packet_db_set))

        print('README: ')
        # 输出插件简介
        if str(mop_db['language']) == 'cn':
            print(packet_readme_cn)
        else:
            print(packet_readme_en)

        # 下载插件
        plugin_r = requests.get(packet_url)
        plugin_r.raise_for_status()

        # TODO: 检查插件文件是否已经存在在目录中

        # 写入插件
        with open(mop_db_path + packet_file_name, "wb") as code:
            code.write(plugin_r.content)
        # TODO: 检查插件第一行是否为'#!'

        plugin_r.close()  # 关闭链接

        print(plugin_file)

        # 创建别名alias
        # TODO: 检查别名是否已经存在
        file = open(os.path.expanduser('~/.zshrc'), 'a')
        file.write(
            'alias ' + packet_alias + '="' + packet_command + ' ' + os.path.abspath(mop_db_path) + '/' + packet_file_name + '"\n')
        file.close()

        mop_db[packet_db_name + 'version'] = packet_version  # 写入版本
        mop_db[packet_db_name + 'readme_cn'] = packet_readme_cn  # 写入中文介绍
        mop_db[packet_db_name + 'readme_en'] = packet_readme_en  # 写入英文介绍

        # 数据库操作
        for db_set_list in packet_db_set:
            mop_db[packet_db_name + db_set_list[0]] = db_set_list[1]  # 写入数据

        # pip安装操作
        for pip_name in packet_pip:
            try:
                pip_tf = mop_db[pip_name]
            except:
                pip_tf = False
            if not pip_tf:  # 排除已经安装过的插件
                os.system('pip3 install ' + pip_name)  # 安装插件
                mop_db[pip_name] = True  # 插件安装成功后写入数据库

        # 把插件添加到数据库到插件列表
        temporary_list = list(mop_db['plugins'])
        temporary_list.append(packet_name)
        mop_db['plugins'] = temporary_list

        # 将数据库前缀和插件名称关联
        temporary_dict = dict(mop_db['db_name'])
        temporary_dict[packet_name] = packet_db_name
        mop_db['db_name'] = temporary_dict

        print(successful)

    print('\n-----------------------\n')  # 分割线

    mop_db.close()  # 关闭数据库
    print('Done.')

# 查看插件README
if args.readme and mop_db_file:
    print('\n-----------------------\n')  # 分割线
    mop_db = shelve.open(mop_db_path + 'mop')  # 打开数据库

    for plugin_name in args.readme:
        if plugin_name not in mop_db['plugins']:  # 检测是否在插件列表中
            print(readme_error + plugin_name)
            print('\n-----------------------\n')  # 分割线
            continue

        print(plugin_name + '-README: ')
        if mop_db['language'] == 'en':
            print(mop_db[mop_db['db_name'][plugin_name] + 'readme_en'])
        else:
            print(mop_db[mop_db['db_name'][plugin_name] + 'readme_cn'])
        print('\n-----------------------\n')  # 分割线

    mop_db.close()  # 关闭链接

# 修改json文件url
if args.url and mop_db_file:
    if args.url[0] == 'n':  # 新增自定义URL
        new_url_name = input('Name: ')  # 输入名称
        new_url = input('URL: ')  # 输入URL

        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地

        if new_url_name in url_dict.keys() or new_url in url_dict.values():  # 检测是否重复
            print(url_new_error)
            sys.exit()  # 重复退出

        url_dict[new_url_name] = new_url

        mop_db['url_sets'] = url_dict  # save

        print(successful)
        mop_db.close()  # 关闭链接
    elif args.url[0] == 'd':  # 删除自定义URL
        del_url_name = input('Name: ')  # 输入删除链接的名称

        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地
        default_url = mop_db['json_url']  # 默认URL

        if del_url_name not in url_dict.keys():
            print(url_error)
            sys.exit()

        del_url = url_dict[del_url_name]  # 获取删除URL
        if del_url == default_url:  # 是否是默认URL
            print(url_del_def_error)
            sys.exit()  # 不允许删除默认URL

        del url_dict[del_url_name]  # 删除链接
        mop_db['url_sets'] = url_dict  # save

        print(successful)
        mop_db.close()  # 关闭链接
    elif args.url[0] == 'e':  # 修改自定义URL
        edit_url_name = input('Name: ')  # 输入需要修改自定义URL的名称
        edit_url = input('NewUrl: ')  # 新URL

        mop_db = shelve.open(mop_db_path + 'mop')
        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地

        if edit_url_name not in url_dict.keys():
            print(url_error)
            sys.exit()

        url_dict[edit_url_name] = edit_url  # 更新URL

        mop_db['url_sets'] = url_dict  # save

        print(successful)
        mop_db.close()  # 关闭链接
    elif args.url[0] == 'l':  # 列出所有URL
        mop_db = shelve.open(mop_db_path + 'mop')

        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地
        default_url = mop_db['json_url']  # 默认URL

        default = ''  # 是否是默认URL

        for name, url in url_dict.items():
            if url == default_url:  # 检测当前URL是否与默认URL匹配
                default = ' (default)'
            else:
                default = ''
            print(name + ' => ' + url + default)

        mop_db.close()  # 关闭链接
    elif args.url[0] == 'c':  # 设置默认URL
        mop_db = shelve.open(mop_db_path + 'mop')

        url_dict = dict(mop_db['url_sets'])  # 加载数据库字典到本地

        default_url_name = input('Name: ')  # 新默认URL名称

        if default_url_name not in url_dict.keys():  # 检测是否在URL列表中
            print(url_def_not_in)
            sys.exit()  # 不存在退出

        mop_db['json_url'] = url_dict[default_url_name]  # 设置默认URL

        print(successful)
        mop_db.close()  # 关闭链接
    else:
        print(url_arg_error)
        if input('y/n> ').lower() == 'y':
            webbrowser.open('https://mop.uts.ski/#/json_url')  # 打开帮助文档
        else:
            sys.exit()  # 退出程序

# 更新插件
if args.update and mop_db_file:
    # TODO: 更新插件
    pass

# 安装轻app
if args.clip and mop_db_file:
    mop_db = shelve.open(mop_db_path + 'mop')  # 连接数据库

    if len(list(args.clip)) > 2:  # 检测是否超出argv限制
        print(clip_arg_error)
        sys.exit()

    url = mop_db['json_url']  # 设置URL

    for clip_name in args.clip:  # 遍历传入的参数,获取URL
        if str(clip_name).lower().startswith('url:'):
            url_name = str(clip_name).split(':')[1]
            url = mop_db['url_sets'][url_name]

    import requests

    clip_r = requests.get(url)  # 获取下载对象
    clip_r.raise_for_status()  # 错误检查
    packet_dict = dict(clip_r.json())  # 保存json内容
    clip_r.close()  # 关闭对象p

    clip_name = 'clip_' + args.clip[0]  # 轻app名称

    if not clip_name in packet_dict.keys():  # 检查轻app是否存在
        print(clip_find_error)
        sys.exit()

    if packet_dict[clip_name]['type'] != 'clip':  # 检查类型是否为clip app
        if mop_db['language'] == 'cn':
            print('查询clip app失败')
        else:
            print('Enquiry clip app failure')
            sys.exit()

    clip_down_url = packet_dict[clip_name]['url']

    clip_r = requests.get(clip_down_url)  # 下载文件
    clip_r.raise_for_status()  # 错误检查
    with open(mop_db_path + 'clip.py', "wb") as code:  # 写入文件
        code.write(clip_r.content)
    clip_r.close()  # 关闭对象

    try:
        import clip
    except:
        if LANGUAGE == 'cn':
            print('加载clip出错')
        else:
            print('Error loading clip')
        # TODO: 清理文件
        sys.exit()

    print('\n-----------------------\n')  # 分割线

    if clip.clip_command(LANGUAGE):
        print('\n-----------------------\n')  # 分割线
        print('OK')
        print('\n-----------------------\n')  # 分割线
    else:
        print('Error')
        print('\n-----------------------\n')  # 分割线

    os.remove(mop_db_path + 'clip.py')  # 清除

# 删除app
if args.remove and mop_db_file:
    remove_list = list(args.remove)  # 缓存所有要删除的app

    print('\n-----------------------\n')  # 分割线