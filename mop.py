#! /usr/local/bin/python3

# 导入模块
import argparse
import os
import shelve
import sys
import json

# 常量设置
VERSION = 1.0

# 多语言设置
file_lists = os.listdir(os.path.expanduser('~'))
if 'mop.json' in file_lists:
    file = open(os.path.expanduser('~/mop.json'), 'r')
    mop_db_path = json.load(file)
    file.close()
    mop_db = shelve.open(mop_db_path+'mop')
    if mop_db['language'] == 'en':
        init_help = 'Initialize or update in the current folder'
        install_help = 'Installation plug-in'
        welcome = 'Welcome-MOP'
        init_error = 'Cannot be initialized multiple times'
        language_help = 'Switch language'
        language_set = 'Language changed successfully'
    elif mop_db['language'] == 'cn':
        init_help = '初始化或者更新当前文件夹'
        install_help = '安装插件'
        welcome = '欢迎使用MOP'
        init_error = '不能多次初始化'
        language_help = '更改语言'
        language_set = '更换语言成功'
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
        if mop_db_file:
            sys.exit()
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
        file.write('alias mop="python3 ' + os.path.abspath('.') + '/mop.py"')
        file.close()
        print('选择语言|Choose a language')
        print('en or cn')
        mop_db['language'] = input()
        language = mop_db['language']
        mop_db.close()
        file = open(os.path.expanduser('~/mop.json'), 'w')
        path_ = os.path.abspath('.')+'/'
        json.dump(path_, file, indent=4)
        file.close()
        if language == 'en':
            print('success'.upper())
        elif language == 'cn':
            print('成功')

# 语言设置
if args.language:
    if args.language[0] == 'en':
        if mop_db_file:
            mop_db = shelve.open(mop_db_path+'mop')
            mop_db['language'] = 'en'
            mop_db.close()
            print(language_set)
        else:
            print(not_init_set_error)
    elif args.language[0] == 'cn':
        if mop_db_file:
            mop_db = shelve.open(mop_db_path+'mop')
            mop_db['language'] = 'cn'
            mop_db.close()
            print(language_set)
        else:
            print(not_init_set_error)