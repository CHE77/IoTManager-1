# правим  %USERPROFILE%\.platformio\packages\framework-arduinoespressif32\libraries\WiFi\src\WiFiClient.cpp 27-28
# для уменьшения тайм-аута ВебСокетов
# #define WIFI_CLIENT_MAX_WRITE_RETRY      (10)
# #define WIFI_CLIENT_SELECT_TIMEOUT_US    (1000000)
# Прописать скрипт в platformio.ini  внутри [env:esp32_4mb3f] написать extra_scripts = pre:tools/patch32_ws.py

import os
import shutil
from sys import platform

if platform == "linux" or platform == "linux2":
    # linux
    mainPyPath = '~/.platformio/packages/framework-arduinoespressif32/libraries/WiFi/src/WiFiClient.cpp'
else:
    # windows
    mainPyPath = os.environ['USERPROFILE'] + '\\.platformio\\packages\\framework-arduinoespressif32\\libraries\\WiFi\\src\\WiFiClient.cpp'

# print(mainPyPath)

with open(mainPyPath) as fr:
    oldData = fr.read()
    if not 'if WIFI_CLIENT_MAX_WRITE_RETRY      (10)' in oldData:
        shutil.copyfile(mainPyPath, mainPyPath+'.bak')
        newData = oldData.replace('#define WIFI_CLIENT_MAX_WRITE_RETRY      (10)', '#define WIFI_CLIENT_MAX_WRITE_RETRY      (2)')
        newData = newData.replace('#define WIFI_CLIENT_SELECT_TIMEOUT_US    (1000000)', '#define WIFI_CLIENT_SELECT_TIMEOUT_US    (500000)')
        with open(mainPyPath, 'w') as fw:
            fw.write(newData)