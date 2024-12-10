:one
adb shell input tap 236 590
TIMEOUT /T 3
adb shell input swipe 200 450 200 1500 50
TIMEOUT /T 1
adb shell input tap 60 130
TIMEOUT /T 2
adb shell input tap 860 590
TIMEOUT /T 3
adb shell input swipe 200 300 200 1500 50
TIMEOUT /T 1
adb shell input tap 60 131
TIMEOUT /T 2
adb shell input tap 236 1500
TIMEOUT /T 3
adb shell input swipe 200 789 200 1500 50
TIMEOUT /T 1
adb shell input tap 60 128
TIMEOUT /T 2
adb shell input tap 860 1500
TIMEOUT /T 3
adb shell input swipe 200 254 200 1500 50
TIMEOUT /T 1
adb shell input tap 60 127
TIMEOUT /T 2

::ping -n 0.01 127.0>nul
goto one