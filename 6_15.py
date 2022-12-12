def check(t, x, y):
    for j in range(x):
        if t[j] == y or t[j] == y-abs(j-x) or t[j] == y+abs(j-x):
            return False
    return True

def hetman(t=[],h=12):
    global counter
    if len(t) == h:
        counter += 1

    for i in range(h):
        if check(t, len(t), i):
            hetman([*t,i], h)

counter = 0
hetman()
print(counter)