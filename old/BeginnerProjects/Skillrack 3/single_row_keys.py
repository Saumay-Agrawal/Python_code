##def check(word, row):
##    flag = True
##    for ch in word:
##        if ch not in row:
##            flag = False
##            break
##    return flag
##
##word = input('Enter a word: ')
##
##if check(word, 'qwertyuiop') \
##   or check(word, 'asdfghjkl') \
##   or check(word, 'zxcvbnm'):
##    print('Yes')
##else:
##    print('No')

"""METHOD 2"""

word = input()
if word[0] in 'qwertyuiop':
    row = 'qwertyuiop'
elif word[0] in 'asdfghjkl':
    row = 'asdfghjkl'
elif word[0] in 'zxcvbnm':
    row = 'zxcvbnm'

flag = True
for ch in word:
    if ch not in row:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')
