array = []
for i in range(3):
	array.append([])
	for j in range(4):
		array[i].append([])
		for k in range(6):
			array[i][j].append('*')

for i in range(3):
        for j in range(4):
                print(array[i][j])
        print()
