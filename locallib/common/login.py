import json

import requests

url = 'http://192.168.4.40:8085/user/login'
data = {
    "username":"wanghui",
    "password":"banxian123",
    "userType":3
}

res = requests.post(url=url,json=data)
print(res.cookies)
my_cookie = res.cookies
data_cookie = json.dumps(my_cookie)
with open(r"../../config/cookie","w") as f:
    f.write(data_cookie)
