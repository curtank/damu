from urllib.request import urlopen
from urllib.parse import unquote
import re
import json
from .douyu_danmu_manager import DouyuDanmuManager

def valid_json(my_json):
    """ 验证是否为 json 数据格式"""
    try:
        json_object = json.loads(my_json)
    except ValueError as e:
        print(e)
        return False
    return json_object


url= "http://www.douyu.com/3484"
html=urlopen(url).read().decode()
#print (html)
room_info_json = re.search('var\s\$ROOM\s=\s({.*});', html).group(1)
#print(room_info_json)
auth_server_json = re.search('\$ROOM\.args\s=\s({.*});', html).group(1)
#print(auth_server_json)
room_info_json_format = valid_json(room_info_json)
#print (room_info_json_format)
auth_server_json_format = valid_json(auth_server_json)
#print(auth_server_json_format)
if room_info_json_format != False and auth_server_json_format != False:
    auth_servers = valid_json(unquote(auth_server_json_format["server_config"]))
    auth_server_ip = auth_servers[0]["ip"]
    auth_server_port = auth_servers[0]["port"]
    print (auth_servers)
    client=DouyuDanmuManager(auth_server_ip,auth_server_port)
    client.start()
