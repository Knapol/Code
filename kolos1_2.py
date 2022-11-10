from math import sqrt

def uniq(num):
    div = 2
    counter = 0
    
    while div <= sqrt(num):
        if num%div == 0:
            counter += 1
            while num%div==0:
                num //= div
        else:
            div += 1

    if num > 1:
        counter += 1
    
    if counter == 2:
        return True

    return False

def square(T):
    x, y = 0, 0
    bok = 1
    d = len(T)
    while bok < d-1:
        while x + bok < d:
            while y + bok < d:
                #print(T[x][y], T[x][y+bok])
                #print(T[x+bok][y], T[x+bok][y+bok])
                #print("------")

                product = T[x][y]*T[x][y+bok]*T[x+bok][y]*T[x+bok][y+bok]
                if uniq(product):
                    return bok

                y += 1
            x += 1
            y = 0
        bok += 1
        x, y = 0, 0
    
    return 0

T =[[2,2,2,4],[2,2,2,8],[2,2,2,2],[2,2,30,3]]

print(square(T))

