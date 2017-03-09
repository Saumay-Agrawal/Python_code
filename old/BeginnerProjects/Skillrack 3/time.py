time = input()

if (0 <= int(time[0:2]) <= 12) \
   and (0 <= int(time[3:5]) < 60) \
   and (0 <= int(time[6:8]) < 60) \
   and (time[-2:]=='AM' or time[-2:]=='PM'):
    if time[-2:]=='AM':
        print(time[:-2])
    else:
        print(str(int(time[0:2])+12) + time[2:-2])
else:
    print('Invalid input')

