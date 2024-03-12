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


html = '''<!DOCTYPE html>
<html>
<head>
<title>test</title>
<style>
  td {
    text-align: center;
  }
</style>
</head>
<body>
'''


name = '6'
P1 = 0
P2 = 0
# S1 = 20
# S2 = 4


html += f"<p>P1={P1}, P2={P2}</p>"


html+= '''<table border="1" style="table-layout: fixed;">
'''

for S1 in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:

    html += '''
  <tr>'''
    html += '''
    <td halign="center" style="word-wrap: break-word;" valign="top">
      <p>
        <a href="{0}">
          <img src="{0}" style="width:256px">
        </a><br>
        <p>{1}</p>
      </p>
    </td>
    '''.format(f"./images/refs.jpg", f"refs")
    html += '''
    <td halign="center" style="word-wrap: break-word;" valign="top">
      <p>
        <a href="{0}">
          <img src="{0}" style="width:256px">
        </a><br>
        <p>{1}</p>
      </p>
    </td>
    '''.format(f"./images/target.jpg", f"target")

    for S2 in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
        html += '''
    <td halign="center" style="word-wrap: break-word;" valign="top">
      <p>
        <a href="{0}">
          <img src="{0}" style="width:256px">
        </a><br>
        <p>{1}</p>
      </p>
    </td>
'''.format(f"./images/P1({P1})_P2({P2})_S1({S1})_S2({S2}).jpg", f"S1({S1})_S2({S2})")
    html += ''' </tr>'''




html += '''
</body>
</html>
'''


# 将HTML表格写入文件
with open(f'{name}.html', 'w') as f:
    f.write(html)
