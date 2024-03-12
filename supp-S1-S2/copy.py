import os
import shutil

dir_list = os.listdir('./6')
for cur in dir_list:
    shutil.copyfile(
        os.path.join('./6', cur, 'result_02.jpg'),
        os.path.join('./images', cur + '.jpg')
    )
