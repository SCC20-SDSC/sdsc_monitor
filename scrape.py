import re
import sys
import csv
import re

def NC(input):

    filtered = re.sub(';','\n', input)
    filtered = re.sub('`', "", filtered)
    filtered = re.sub(' T ', "_", filtered)
    a = re.findall('(Price=\d+(.|,)\d+)',filtered)
    p = 0;
    for i in range (0,len(a)):
        p += float(re.sub('Price=',"",a[i][0]))
    #b = re.findall('PriceUpdatedTime=/\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}.\d{3}+\d{2}:\d{2}/', filtered)
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
        arr[0] = row_count
        store_value = ",".join(str(v) for v in arr)
        fd.write(store_value)
        fd.write('\n')



if __name__ == "__main__":
    arr = [-1]
    name = [0]
    with open('cluster_names.txt', 'r')as i:
        for line in i:
            line = re.sub('\n', "", line)
            name.append(line)
            print(line)
            with open(line,'r')as f:
                k = NC(f.read())
                arr.append(k)

    print(arr)
    store(arr, name)
