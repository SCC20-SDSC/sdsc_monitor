import re
import sys
import csv
import re
from datetime import datetime


def NC(input):
    print('enter regex')
    filtered = re.sub(';','\n', input)
    filtered = re.sub('`', "", filtered)
    filtered = re.sub(' T ', "_", filtered)
    a = re.findall('(Price=\d+(.|,)\d+)',filtered)
    p = 0;
    for i in range (0,len(a)):
        p += float(re.sub('Price=',"",a[i][0]))
    return p;
#print(b)
#def store():

def store(arr, name):


    with open('data.csv','r') as fd:
        row_count = sum(1 for row in fd)
        print('row count')
        print(row_count)

    with open('data.csv','r') as fd:
        if(row_count > 0):
            col_count = len(next(fd))
            print('col count')
            print(col_count)
        else:
            col_count = 99999


    with open('data.csv', 'r') as fd:
        if len(arr) >= col_count:
            for item in fd:
                print('------------------')
                print(item)
                for t in range(0,(len(arr) - (col_count-1))):
                    item+=',0'

    with open('data.csv', 'a') as fd:
        if(row_count == 0):
            names = ",".join(str(v) for v in name)
            fd.write(names)
            fd.write('\n')
	now = datetime.now()
	current_time = now.strftime("%D:%H:%M:%S")
        arr[0] = current_time 
        store_value = ",".join(str(v) for v in arr)
        fd.write(store_value)
        fd.write('\n')



if __name__ == "__main__":
    arr = [-1]
    name = [0]
    with open('data.csv', 'r')as i:
	line = next(i)
	line = line.split(",")
	for clname in line:
            clname = re.sub("\n", "", clname)
	    with open(clname,'r')as f:
      	        k = NC(f.read())
                arr.append(k)

    store(arr, name)
