import json

packets = {
    'rename_tools': {
        'url': 'https://raw.githubusercontent.com/underthestars-zhy/MOP-ReName-Tools/main/rename_tools.py',
        'version': 1.0,
        'plugins': [],
        'shortcut_name': 'prm',
        'db_set': [],
        'update': []
    }
}

with open('packet.json','w') as f:
    json.dump(packets, f, indent=4)