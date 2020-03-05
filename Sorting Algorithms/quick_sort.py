# Pick first/last/random/median element as pivot.
# O(n**2) when always picks greatest or smallest element as pivot.
# O(n log(n)) when always picks the middle element as pivot.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        mid = []
        for each in arr:
            if each < pivot:
                left.append(each)
            elif each > pivot:
                right.append(each)
            else:
                mid.append(each)
        return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([3,2,1]))
