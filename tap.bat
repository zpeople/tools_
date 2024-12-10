:one
adb shell input tap 90 960
TIMEOUT /T 3
adb shell input swipe 200 300 200 1500 50
adb shell input tap 60 160

::ping -n 0.01 127.0>nul
goto one