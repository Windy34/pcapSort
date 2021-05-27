import sys
data = ''
pkt1 = []
pkt2 = []
delim = '+---------+---------------+----------+'
inputf = sys.argv[1]
with open(inputf, 'r') as f:
	data = f.readlines()
i = 0
data += '@'
line = 1
while data[line] != '@':
	if data[line] == '@':
		break
	#print (data[line])
	pkt1.append(data[line])
	line += 1
	if line >= len(data):
                break
	pkt2.append(data[line])
	line += 3
	if line >= len(data):
                break
#print (data)
#print (pkt1)
#print (pkt2)
#=====SORTING BY FIRST 18 SYMBOLS=====
def sort1():
	shift1 = 5
	shift2 = 23
	lst = []

	for i in pkt2:
		lst.append(i[shift1:shift2+1])
	print ("Sorted ranges are: \n", *lst)
	for i in range(len(pkt1)-1):
		tmp1 = pkt1[i]
		tmp2 = pkt2[i]
		for j in range(i, len(pkt1)):
			if lst[i] < lst[j]:
				pkt1[i], pkt1[j] = pkt1[j], pkt1[i]
				pkt2[i], pkt2[j] = pkt2[j], pkt2[i]
				lst[i], lst[j] = lst[j], lst[i]

#=====SORTING BY SECOND 18 SYMBOLS=====
def sort2():
        shift1 = 23
        shift2 = 41
        lst = []

        for i in pkt2:
                lst.append(i[shift1:shift2+1])
        print ('Sorted ranges are: \n', *lst)
        for i in range(len(pkt1)-1):
                tmp1 = pkt1[i]
                tmp2 = pkt2[i]
                for j in range(i, len(pkt1)):
                        if lst[i] < lst[j]:
                                pkt1[i], pkt1[j] = pkt1[j], pkt1[i]
                                pkt2[i], pkt2[j] = pkt2[j], pkt2[i]
                                lst[i], lst[j] = lst[j], lst[i]
#=====SORTING BY FIRST 36 SYMBOLS=====
def sort3():
    shift1 = 5
    shift2 = 41
    lst = []
    for i in pkt2:
        lst.append(i[shift1:shift2+1])
    print ('Sorted ranges are: \n', *lst)
    for i in range(len(pkt1)-1):
        for j in range(i, len(pkt1)):
            if lst[i] < lst[j]:
                pkt1[i], pkt1[j] = pkt1[j], pkt1[i]
                pkt2[i], pkt2[j] = pkt2[j], pkt2[i]
                lst[i], lst[j] = lst[j], lst[i]
                
if sys.argv[2] == '1':
    sort1()
    print('File was sorted by first 18 symbols')
elif sys.argv[2] == '2':
    sort2()
    print('File was sorted by second 18 symbols')
elif sys.argv[2] == '3':
    sort3()
    print('File was sorted by first 32 symbols')

with open('output.txt', 'w') as f:
    for i in range(len(pkt1)):
        f.write(delim)
        f.write('\n')
        f.write(pkt1[i])
        f.write(pkt2[i])
        f.write('\n')
