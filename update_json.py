import json

update = {
    'README': '''-全新的版本更新功能
-BugFix''',
    1.1: {
        'db_set': [['json_url', 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/packet.json'],
                   ['update_url', 'https://raw.githubusercontent.com/underthestars-zhy/MacOS-Plugins/main/update.json']]
    },
}

with open('update.json', 'w') as f:
    json.dump(update, f, indent=4)
