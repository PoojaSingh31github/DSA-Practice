def minWindow(s,t):
    target_count = [0] * 256
    for char in t:
        target_count[ord(char)] += 1

    # Sliding window variables
    start = 0
    matched_count = 0
    min_length = float("inf")
    min_start = 0

    # Frequency map for the current window
    window_count = [0] * 256

    for end in range(len(s)):
        char_end = ord(s[end])
        window_count[char_end] += 1

        # Check if the current character satisfies the condition
        if target_count[char_end] > 0 and window_count[char_end] <= target_count[char_end]:
            matched_count += 1

        # Shrink the window from the start if all characters are matched
        while matched_count == len(t):
            window_length = end - start + 1
            if window_length < min_length:
                min_length = window_length
                min_start = start

            # Shrink the window
            char_start = ord(s[start])
            window_count[char_start] -= 1
            if target_count[char_start] > 0 and window_count[char_start] < target_count[char_start]:
                matched_count -= 1
            start += 1

    # Return the result
    return "" if min_length == float("inf") else s[min_start:min_start + min_length]

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))