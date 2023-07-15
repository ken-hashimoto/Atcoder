def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if data[i][0] * data[j][1] < data[i][1] * data[j][0]:
            data_temp.append(data[i])
            i = i + 1
        else:
            data_temp.append(data[j])
            j = j + 1

    while i <= mid:
        data_temp.append(data[i])
        i = i + 1

    while j <= end:
        data_temp.append(data[j])
        j = j + 1

    k = start
    for val in data_temp:
        data[k] = val
        k = k + 1  

def merge_sort(data, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid + 1, end)
    merge(data, start, mid, end)



N = int(input())
data = []
for i in range(N):
    A,B = map(int,input().split())
    data.append((A,B,i+1))
end = len(data) - 1
merge_sort(data, 0, end)
print(data)
    