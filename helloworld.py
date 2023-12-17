mport time

alpha = " abcdefghijklmnopqrstuvwxyz!"

def process(index):
    hw = "".join(alpha[i] for i in range(index))
    result = []
    for i in range(index):
        result.append(hw[:i + 1])
        time.sleep(0.1)
    return result

indices = [9, 6, 13, 13, 16, 1, 24, 16, 19, 13, 5, 28]

for i in indices:
    result = process(i)
    print(result)
