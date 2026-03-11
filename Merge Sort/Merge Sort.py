def merge_sort(a):
    # Сортировка слиянием (возвращает новый отсортированный список).
    # Делим массив пополам, сортируем половины, затем сливаем.
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)

def merge(left,right):
    # Слияние двух отсортированных списков в один
    res=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i]);i+=1
        else:
            res.append(right[j]);j+=1
    # дописываем “хвост”, если остался
    res.extend(left[i:])
    res.extend(right[j:])
    return res
