#  Copyright (c) 2020.
#  You can freely change the code part, but you must follow the MIT protocol
#  You cannot delete any information about UTS
#  You cannot use this program to disrupt social order.

import json


packets = {
    'rename_tools': {
        'url': 'https://raw.githubusercontent.com/underthestars-zhy/MOP-ReName-Tools/main/rename_tools.py',
        'file_name': 'rename_tools.py',
        'code_language': 'python',
        'shortcut_name': 'prm',
        'version': 1.1,
        'pip': [],
        'db_set': [
                ['file_alias', {'My': '~'}],
                ['text', {'Num': []}]
            ],
        'update': {
            1.1: [
                ['file_alias', {'My': '~'}],
                ['text', {'Num': []}]
            ],
        },
        'readme_cn': '使用prm -r_num <源文件夹> <现文件夹> <起始数字>重命名文件\n<源文件夹> <现文件夹>可重名\n<起始数字>可不填写，默认0',
        'readme_en': 'Rename files using PRM-R < source folder > current folder > < start number > \n'
                     '< Source Folder > > current folder > repeatable name\n'
                     '“start number” can not be filled in, the Default 0'
    },
    'sync': {
        'url': 'https://raw.githubusercontent.com/underthestars-zhy/sync-tools/main/sync.py',
        'clip': 'https://raw.githubusercontent.com/underthestars-zhy/sync-tools/main/clip.py',
        'type': 'text',
        'command': 'python3',
        'file_name': 'sync.py',
        'code_language': 'python',
        'code_language_version': '3.8~3.10',
        'alias': 'pysync',
        'version': 1.1,
        'pip': [],
        'db_name': 'sync_',
        'db_set': [
            ['dir_set', {}]
        ],
        'update': {
            1.1: 'pass'
        },
        'readme_cn': '使用pysync -s 同步文件\n使用pysync -dir设置同步文件夹',
        'readme_en': 'use pysync -s SYNC file\nuse pysync -dir Set the folder to sync'
    },
    'tubedown': {
        'url': 'https://raw.githubusercontent.com/underthestars-zhy/tubedown/main/tubedown.py',
        'file_name': 'tubedown.py',
        'code_language': 'python',
        'code_language_version': '3.8~3.10',
        'alias': 'tube',
        'version': 1.1,
        'pip': ['pytube'],
        'db_name': 'tubedown_',
        'db_set': [
            ['save_path', ''],
            ['down', []]
            ],
        'update': {
        },
        'readme_cn': '使用tube -d (储存路径) 下载视频并储存\n使用tube -dir <filename>设置默认储存文件夹',
        'readme_en': 'Download and store video using tube -d (store path) \n'
                     'Set the default storage folder using tube -dir <filename>'
    },
    'clip_sync': {
        'type': 'clip',
        'url': 'https://raw.githubusercontent.com/underthestars-zhy/sync_clip/main/sync_clip.py',
    }
}

with open('packet.json', 'w') as f:
    json.dump(packets, f, indent=4)