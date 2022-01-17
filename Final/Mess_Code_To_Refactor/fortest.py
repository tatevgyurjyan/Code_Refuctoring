import json

# with open('cred.json', 'w+') as f:
#     data = json.load(f)
#     data['login']['email'] = "test125@gmail.com"
#     data['login']['password'] = "123456789"
#     f.write(json.dumps(data))

import json
with open('cred.json') as f:
    data = json.load(f)
data['email'] = 'by'
with open('cred.json', 'w') as f:
    json.dump(data, f)

# {

#     "login" : {"email":"", "password":""}
# }
