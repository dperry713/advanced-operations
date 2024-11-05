def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    
    return merged_list

#time complexity: O(n)
#space complexity: O(n)