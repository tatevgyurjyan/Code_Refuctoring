import json
with open('cred.json') as f:
    data = json.load(f)
data['example1'] = 'bye'
with open('cred.json', 'w') as f:
    json.dump(data, f)
