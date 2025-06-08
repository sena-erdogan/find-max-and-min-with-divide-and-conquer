def worst_best(a):
    print("best: ", best(a, 0, len(a)))
    print("worst: ", worst(a, 0, len(a)))
    
def best(a, index, length):
    if index >= length - 2:
        if a[index] > a[index + 1]:
            return a[index]
        else:
            return a[index + 1]
            
    max = best(a, index + 1, length)
    
    if(a[index] > max):
        return a[index]
    else:
        return max
        
def worst(a, index, length):
    if index >= length - 2:
        if a[index] < a[index + 1]:
            return a[index]
        else:
            return a[index + 1]
    
    min = worst(a, index + 1, length)

    if a[index] < min:
        return a[index]
    else:
        return min

worst_best([4,2,4,6,34,6])