import requests
from hashlib import md5
url = "https://mapi.58wld.com/weleadin-web-mapi/robot/queryByContent.do"
data = {"100201809281045605043941670912", "订单"}
m = md5()
for i in data:
    m.update(i.encode())
    str_md5 = m.hexdigest()
    data_new = {"ucode": str_md5, "content": str_md5}
    res = requests.post(url, json=data_new).content.decode()
    print(i, res)


