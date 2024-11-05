def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

#time complexity: O(n+m)
#space complexity: O(n+m)