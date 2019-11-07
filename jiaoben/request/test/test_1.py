import requests
from hashlib import md5

url = "http://wldoperation.58wld.com/go.php/Index/shopRed"
data = "wldf97b74bbf1c678c4"
m = md5()
m.update(data.encode())
str_md5 = m.hexdigest()
data_new = {"acode": str_md5}
res = requests.post(url, json=data_new).content.decode()
print(res)