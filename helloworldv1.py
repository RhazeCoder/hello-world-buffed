import time

hw = ""
alpha = " abcdefghijklmnopqrstuvwxyz!"

def process(index):
    global hw
    i = 0
    while i < index:
        alphabet = list(alpha)
        hw += alphabet[i]
        print(hw)
        if i != index - 1:
            hw = hw[:-1]
        i += 1
        time.sleep(0.1)

process(9)
process(6)
process(13)
process(13)
process(16)
process(1)
process(24)
process(16)
process(19)
process(13)
process(5)
process(28)
