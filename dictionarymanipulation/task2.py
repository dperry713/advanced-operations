def intersect_dictionaries(dict1, dict2):
    return {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}

#time complexity: O(n)
#space complexity: O(k)