import time

def selection_sort(data,drawData,timeTick):
    for i in range(len(data) - 1):
        minIdx = i
        for j in range(i+1,len(data)):
            if data[minIdx] > data[j]:
                minIdx = j
                drawData(data,['green' if x == i or x == minIdx else 'red' for x in range(len(data))])
                time.sleep(timeTick / 100)
        data[i] , data[minIdx] = data[minIdx], data[i]
