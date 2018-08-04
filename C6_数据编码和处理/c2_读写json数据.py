
import json

data = {
    'name':'ACE',
    'shares':100,
    'price':542.23
}
# 处理字符串用 dumps 和 loads
json_str = json.dumps(data)
print(json_str, type(json_str))

data = json.loads(json_str)
print(data, type(data))

# 处理文件用 dump 和 load
with open('data_custom.json', 'wt') as f:
    json.dump(json_str, f)
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data, type(data))