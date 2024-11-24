def findSubstring(s, words) :
    if not s or not words:
        return []

    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count

    # Create a frequency map for the words
    word_map = {}
    for word in words:
        word_map[word] = word_map.get(word, 0) + 1

    result = []

    # Traverse through the string
    for i in range(word_length):
        start = i
        current_count = {}
        count = 0

        for j in range(i, len(s) - word_length + 1, word_length):
            word = s[j:j + word_length]
            # If the word is part of the words array
            if word in word_map:
                current_count[word] = current_count.get(word, 0) + 1
                count += 1

                # If the word's count exceeds the required count, shrink the window
                while current_count[word] > word_map[word]:
                    left_word = s[start:start + word_length]
                    current_count[left_word] -= 1
                    count -= 1
                    start += word_length

                # If the current window matches the total word count, add the start index
                if count == word_count:
                    result.append(start)
            else:
                # Reset the window if the word is not in the word_map
                current_count.clear()
                count = 0
                start = j + word_length

    return result
    
s = "barfoothefoobarman" 
words = ["foo","bar"]

print(findSubstring(s, words))    