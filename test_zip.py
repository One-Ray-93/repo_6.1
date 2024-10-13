from zipfile import ZipFile
import os

path = '/TMP'
file_dir = os.listdir(path)

with zipfile.ZipFile('test_zip.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(path, file)
        zf.write(add_file)

>>> os.system('file test.zip')