import heapq

def HeapSort(list):
    heapq.heapify(list)
    heap = []
    print(list)
    while list:
        heap.append(heapq.heappop(list))
    list[:] = heap
    return list

print(HeapSort([1,3,5,7,9,2,4,6,8,0]))