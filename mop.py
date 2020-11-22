#! /usr/local/bin/python3

# 导入模块
import argparse
import os
import shelve
import sys
import json

# 常量设置
VERSION = 1.1

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
    mop_db.close()
    mop_db_file = True
else:
    mop_db_file = False
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

args = parser.parse_args()

# 欢迎
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
        mop_db['update_url'] = 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/update.json'
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
        print(update_text)
        mop_db = shelve.open(mop_db_path + 'mop')
        if str(mop_db['version']) >= str(VERSION):  # 检测是否更新到"低"版本
            print(update_init)
            mop_db.close()
            sys.exit()
        print(str(mop_db['version']) + '=>' + str(VERSION))
        import requests
        #url = 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/update.json'
        url = mop_db['update_url']
        update_json = requests.get(url, allow_redirects=True)
        if not update_json.status_code:
            print(http_error)
            sys.exit()
        update_code = dict(update_json.json())
        print(update_find)
        for key_version in update_code.keys():
            version_code = []
            if key_version == 'README':
                continue
            if float(key_version) <= mop_db['version'] or float(key_version) > VERSION:
                continue
            else:
                version_code.append(key_version)
        for version_command in version_code:
            for command in update_code[version_command]['db_set']:
                mop_db[command[0]] = command[1]
        mop_db['version'] = VERSION
        mop_db.close()
        print(update_code['README'])
        print(successful)





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
    if not packets_json.status_code:
        print(http_error)
        sys.exit()
    packets = packets_json.json()
    find = False
    for packet in packets.keys():
        if packet == str(args.install[0]).lower():
            print(plugin_find)
            find = True
            plugin_dic = packets[packet]
            py_file = packet+".py"
            break
    if not find:
        print(plugin_error)
        sys.exit()
    plugin_url = plugin_dic['url']
    plugin_file = requests.get(plugin_url, allow_redirects=True)
    if not plugin_file.status_code:
        print(http_error)
        sys.exit()
    file = open(py_file, 'w')
    file.write(plugin_file.text)
    file.close()
    print(plugin_file)
    mop_db[str(packet)+"_version"] = plugin_dic['version']
    print(plugin_plugins)
    if plugin_dic['plugins']:
        pip_lists = plugin_dic['plugins']
        for pip_name in pip_lists:
            os.system('pip3 install '+pip_name)
        print(pip_true)
    else:
        print(pip_nothing)
    if plugin_dic['db_set']:
        for db_dicts in plugin_dic['db_set']:
            mop_db[db_dicts[0]] = mop_db[db_dicts[1]]
        print(db_set_true)
    else:
        print(db_set_nothing)
    mop_db.close()
    file = open(os.path.expanduser('~/.zshrc'), 'a')
    command = 'alias ' + plugin_dic["shortcut_name"] + '="python3 ' + mop_db_path +py_file + '"\n'
    file.write(command)
    file.close()
    print(plugin_command+plugin_dic['shortcut_name'])
    print(successful)
