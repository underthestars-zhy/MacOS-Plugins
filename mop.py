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

# 常量设置
VERSION = 1.2

# 多语言设置
file_lists = os.listdir(os.path.expanduser('~'))
if 'mop.json' in file_lists:
    file = open(os.path.expanduser('~/mop.json'), 'r')
    mop_db_path = json.load(file)
    file.close()
    mop_db = shelve.open(mop_db_path + 'mop')
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

# 命令参数设置
parser = argparse.ArgumentParser(description='MacOS 11 Plugins Install Tool')

parser.add_argument('-init', type=str, help=init_help, choices=['install', 'update'], nargs=1)  # 初始化/更新命令
parser.add_argument('-install', type=str, help=install_help, nargs=1)  # 安装命令
parser.add_argument('-language', type=str, help=language_help, nargs=1, choices=['en', 'cn'])  # 更换语言
parser.add_argument('-readme', type=str, help=readme_help, nargs=1)  # 查看插件帮助

args = parser.parse_args()

# 欢迎
if welcome_flag:
    print(welcome)

# 初始化/更新
if args.init:
    if args.init[0] == 'install':
        mop_db = shelve.open('mop')
        mop_db['version'] = VERSION
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
        mop_db['language'] = input()
        language = mop_db['language']
        mop_db['json_url'] = 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/packet.json'
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
        mop_db = shelve.open(mop_db_path + 'mop')
        if VERSION <= float(mop_db['version']):
            print(update_init)
            sys.exit()
        print(update_text)
        print(str(mop_db['version'])+' => '+str(VERSION))
        if float(mop_db['version']) < 1.1:
            mop_db['json_url'] = 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/packet.json'
            mop_db['update_url'] = 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/update.json'
        if float(mop_db['version']) < 1.2:
            mop_db['update_url'] = None
            all_file = os.listdir(mop_db_path)
            for file_name in all_file:
                if not str(file_name).endswith('.py') or file_name == 'mop.py' or file_name == 'mop.db':
                    continue
                url = mop_db['json_url']
                import requests
                packets_json = requests.get(url, allow_redirects=True)
                if packets_json.raise_for_status() != None:
                    print(http_error)
                    sys.exit()
                file_name = file_name[:-3]
                all_plugins = packets_json.json()
                mop_db[file_name+'_readme_cn'] = all_plugins[file_name]['readme_cn']
                mop_db[file_name + '_readme_en'] = all_plugins[file_name]['readme_en']
        print(successful)
        if mop_db['language'] == 'cn':
            print('- 支持查看插件说明\n- 优化')
        else:
            print('- Support for viewing plug-in instructions\n- optimisation')
        mop_db['version'] = VERSION
        mop_db.close()


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
    import requests

    mop_db = shelve.open(mop_db_path + 'mop')
    url = mop_db['json_url']
    packets_json = requests.get(url, allow_redirects=True)
    if packets_json.raise_for_status() != None:
        print(http_error)
        sys.exit()
    packets = packets_json.json()
    find = False
    for packet in packets.keys():
        if packet == str(args.install[0]).lower():
            print(plugin_find)
            find = True
            plugin_dic = packets[packet]
            py_file = packet + ".py"
            break
    if not find:
        print(plugin_error)
        sys.exit()
    plugin_url = plugin_dic['url']
    plugin_file = requests.get(plugin_url, allow_redirects=True)
    if plugin_file.raise_for_status() != None:
        print(http_error)
        sys.exit()
    file = open(py_file, 'w')
    file.write(plugin_file.text)
    file.close()
    print(plugin_file)
    mop_db[str(packet) + "_version"] = plugin_dic['version']
    mop_db[str(packet) + '_readme_cn'] = plugin_dic['readme_cn']
    mop_db[str(packet) + '_readme_en'] = plugin_dic['readme_en']
    print(plugin_plugins)
    if plugin_dic['plugins']:
        pip_lists = plugin_dic['plugins']
        for pip_name in pip_lists:
            os.system('pip3 install ' + pip_name)
        print(pip_true)
    else:
        print(pip_nothing)
    if plugin_dic['db_set']:
        for db_dicts in plugin_dic['db_set']:
            mop_db[db_dicts[0]] = mop_db[db_dicts[1]]
        print(db_set_true)
    else:
        print(db_set_nothing)
    mop_db[str(args.install[0]).lower() + 'readme_cn'] = plugin_dic['readme_cn']
    mop_db[str(args.install[0]).lower() + 'readme_en'] = plugin_dic['readme_en']
    mop_db.close()
    file = open(os.path.expanduser('~/.zshrc'), 'a')
    command = 'alias ' + plugin_dic["shortcut_name"] + '="python3 ' + mop_db_path + py_file + '"\n'
    file.write(command)
    file.close()
    print(plugin_command + plugin_dic['shortcut_name'])
    print(successful)

# 查看插件README
if args.readme and mop_db_file:
    print(args.readme[0] + '-README')
    mop_db = shelve.open(mop_db_path + 'mop')
    if mop_db['language'] == 'en':
        print(mop_db[args.readme[0] + '_readme_en'])
    else:
        print(mop_db[args.readme[0] + '_readme_cn'])
