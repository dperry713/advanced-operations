def count_word_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

#time complexity: O(n)
#space complexity: O(k)