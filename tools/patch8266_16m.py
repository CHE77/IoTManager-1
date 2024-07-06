# правим  %USERPROFILE%\.platformio\platforms\espressif8266\builder\main.py 103-115
# для добавления возможности прошивки 16мб модуля esp8266

import os
import shutil
from sys import platform

if platform == "linux" or platform == "linux2":
    # linux
    home_dir = os.environ['HOME']
else:
    # windows
    home_dir = os.environ['USERPROFILE']

# Construct the path using os.path.join for platform independence
mainPyPath = os.path.join(home_dir, '.platformio', 'packages', 'framework-arduinoespressif32', 'libraries', 'WiFi', 'src', 'WiFiClient.cpp')

# print(mainPyPath)

with open(mainPyPath) as fr:
    oldData = fr.read()
    if not 'if _value == -0x6000:' in oldData:
        shutil.copyfile(mainPyPath, mainPyPath+'.bak')
        newData = oldData.replace('_value += 0xE00000  # correction', '_value += 0xE00000  # correction\n\n        if _value == -0x6000:\n            _value = env[k]-0x40200000')
        with open(mainPyPath, 'w') as fw:
            fw.write(newData)
