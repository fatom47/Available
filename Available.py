# Mouse movement to be still available
import pyautogui, sys, time
print('Press Ctrl-C to quit.')
bzzz = 111 #sec (283s)

def timeFormat(duration):
    if duration<60:
        return str(duration) + 's'
    elif duration < 3600:
        return str(duration//60) + 'm ' + str(duration%60) + 's'
    else:
        return str(duration//3600) + 'h ' + str((duration-((duration//3600)*3600))//60) + 'm ' + str(duration%60) + 's'

try:
    start = time.time()
    time.sleep(bzzz)
    while True:
        pyautogui.move(1, 1)
        pyautogui.move(-1, -1)
        pyautogui.scroll(1)
        pyautogui.scroll(-1)
        print('Refreshed')
        print('Duration: ' + timeFormat(int(time.time()-start)))
        time.sleep(bzzz)
except KeyboardInterrupt:
    print('\n')
