import json

data = {}
# 打开文件
with open('data/TIProjectTemplate.chs', 'r',encoding='utf-8') as f:
    # 读取一行
    while True:
        line = f.readline()
        if not line:
            break
        # 判断是否为空行
        if line == '\n':
            continue

        data[line.split('=')[0]] = line.split('=')[1].strip()

# 写入
with open('data/TIProjectTemplate.json', 'w',encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4,ensure_ascii=False))

