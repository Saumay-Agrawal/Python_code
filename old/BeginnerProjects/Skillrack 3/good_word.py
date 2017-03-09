word = input()
flag = True
for ch in word:
    c = 0
    for i in word:
        if ch == i:
            c += 1
    if c > 1:
        flag = False
        break

if flag:
    print('Good')
else:
    print('Bad')
