def reverse_sublist(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

#time complexity: O(n)
#space complexity: O(1)