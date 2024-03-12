import os
import re


def custom_sort(item):
    if isinstance(item, str) and item.isdigit():
        return int(item), ''
    else:
        numeric_part = re.findall(r'\d+', item)  # 提取字符串中的数字部分
        non_numeric_part = re.findall(r'\D+', item)  # 提取字符串中的非数字部分

        if numeric_part:
            return int(numeric_part[0]), non_numeric_part[0]
        else:
            return (float('inf'), item)



file_list = os.listdir('./refs')  # 11_1_K1(20)_K2(0)_S1(20)
file_list.sort(key=custom_sort)
print(file_list)



html = '''<!DOCTYPE html>
<html>
<head>
<title>supp-outline-based</title>
<style>
  td {
    text-align: center;
  }
</style>
</head>
<body>
'''


for file_name in file_list:
    name = file_name[:-4]
    html += '''
<table border="1" style="table-layout: fixed;">
  <tr>
    <td halign="center" style="word-wrap: break-word;" valign="top">
      <p>
        <a href="{0}">
          <img src="{0}" style="width:256px">
        </a><br>
        <p>{1}</p>
      </p>
    </td>
'''.format(f"refs\\{name}.jpg", f"{name}_reference")
    for index in [1, 2]:
        html += '''
    <td halign="center" style="word-wrap: break-word;" valign="top">
      <p>
        <a href="{0}">
          <img src="{0}" style="width:256px">
        </a><br>
        <p>{1}</p>
      </p>
    </td>
'''.format(f"tgts\\{name}-{index}.jpg", f"{name}-{index}-target")
        html += '''
    <td halign="center" style="word-wrap: break-word;" valign="top">
      <p>
        <a href="{0}">
          <img src="{0}" style="width:256px">
        </a><br>
        <p>{1}</p>
      </p>
    </td>
'''.format(f"results\\{name}-{index}.jpg", f"{name}-{index}-result")


html += '''
</body>
</html>
'''


# 将HTML表格写入文件
with open('image_table.html', 'w') as f:
    f.write(html)
