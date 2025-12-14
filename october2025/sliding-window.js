// SLIDING WINDOW TECHNIQUE - 50 PRACTICE QUESTIONS
// ===============================================

// Q1: Maximum sum subarray of size k
// Input: arr = [2, 1, 5, 1, 3, 2], k = 3
// Output: 9
// Explanation: Maximum sum of any subarray of size 3 is 9 (subarray [5, 1, 3])

let ws = 0;

for (let i=0; i<k; i++){
    ws += arr[i]
}
maxx = ws
for (let i= k; i<arr.length; i++){
    ws = ws + arr[i] - arr[i-k]
    if (maxx<ws){
        maxx = ws
    }
}

console.log(maxx)

// Q2: Minimum size subarray sum
// Input: arr = [2, 3, 1, 2, 4, 3], target = 7
// Output: 2
// Explanation: Minimum length subarray with sum ≥7 is length 2 ([4, 3])

let minLen = Infinity
let sum =0
let j=0
for(let i=0; i<arr.length; i++){
    sum+=arr[i]
    while (sum>=target){
        minLen = Math.min(minLen, i-j+1)
        sum -= arr[j]
        j++
    }
}

console.log(minLen)

// maximum size subarray sum
// arr = [2, 3, 2, 4, 3]
// target = 7

ws=0
minLen =0
j=0
for (let i=0; i<arr.length;i++){
    ws+=arr[i]
    while (ws >=target){
        ws -= arr[j]
        j++
    }
    minLen = Math.max(minLen,i-j+1)
    
}
console.log(minLen)

// Q3: Longest substring without repeating characters
// Input: s = "abcabcbb"
// Output: 3
// Explanation: Longest substring without duplicates is "abc"

let char_set ={}
let sum =0
let j=0
let maxLen =0
for (let i=0; i<sum.length;i++){
    while (char_set[s[i]]){
        char_set[s[j]]-=1
        j++
    }
    char_set[s[i]] = 1
    maxlen = Math.max(maxLen, i-j+1)
}
console.log(maxLen)









// Q4: Permutation in string
// Input: s1 = "ab", s2 = "eidbaooo"
// Output: true
// Explanation: s2 contains a permutation "ba" of s1




// Q5: Binary subarrays with sum
// Input: nums = [1, 0, 1, 0, 1], goal = 2
// Output: 4
// Explanation: Count of subarrays with sum 2



// Q6: Maximum number of fruits in two baskets
// Input: fruits = ["A", "B", "C", "A", "C"]
// Output: 3
// Explanation: Longest subarray with at most 2 distinct fruits is length 3 ("C", "A", "C")



// Q7: Smallest window containing all characters of another string
// Input: s = "ADOBECODEBANC", t = "ABC"
// Output: "BANC"
// Explanation: Minimum window substring containing all chars of t



// Q8: Count distinct elements in every window of size K
// Input: arr = [1, 2, 1, 3, 4, 2, 3], K = 4
// Output: [3, 4, 4, 3]
// Explanation: Distinct counts in each window



// Q9: Longest substring with at most two distinct characters
// Input: s = "eceba"
// Output: 3
// Explanation: "ece" is the longest substring with ≤2 distinct chars

// Q10: Count occurrences of anagrams
// Input: s = "cbaebabacd", p = "abc"
// Output: [0, 6]
// Explanation: Starting indices of p's anagrams in s



// Q11: Longest Repeating Character Replacement
// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Replace 1 char to get longest repeating substring

// Q12: Subarrays product less than k
// Input: nums = [10, 5, 2, 6], k = 100
// Output: 8
// Explanation: Number of subarrays with product < 100

// Q13: Maximum average subarray of length K
// Input: nums = [1,12,-5,-6,50,3], k = 4
// Output: 12.75
// Explanation: Max average sum in subarray of size 4

// Q14: Find all anagrams in a string
// Input: s = "abab", p = "ab"
// Output: [0,1,2]
// Explanation: Starting indices of anagrams

// Q15: Longest substring without repeating characters in a stream
// Input: stream of characters
// Output: length of longest substring encountered

// Q16: Count substrings with exactly K distinct characters
// Input: s = "pqpqs", k = 2
// Output: 7

// Q17: Find kth largest element in a subarray
// Input: nums = [1,5,2,5,3], k varies
// Output: kth largest in subarray

// Q18: Subarray sum equals K
// Input: nums = [1,1,1], k=2
// Output: 2
// Explanation: Number of subarrays summing to 2

// Q19: First negative integer in every window of k
// Input: arr=[-8,2,3,-6,-1], k=3
// Output: [-8,0,-6,-1]

// Q20: Longest substring with k distinct characters
// Input: s = "araaci", k=2
// Output: 4
// Explanation: "araa"

// Q21: Maximum sum of subarray at least size k
// Input: arr = [1,2,3,4,5], k=2
// Output: 14
// Explanation: Max sum subarray with size≥2

// Q22: Longest substring with at most k distinct characters
// Input: s = "eceba", k=2
// Output: 3 ("ece")

// Q23: Smallest window containing all characters of another string
// Input: "this is a test string", t: "tist"
// Output: "t stri"

// Q24: Count distinct numbers on all windows of size k
// Input: [1,2,2,1,3], k=3
// Output: [2, 2, 3]

// Q25: Minimum window substring containing characters of a string
// Input: S = "ADOBECODEBANC", T = "ABC"
// Output: "BANC"

// Q26: Maximum sum of subarray of size k with no duplicates
// Input: arr = [1,2,3,4,5], k=3
// Output: 12

// Q27: Maximum number of vowels in substring of length k
// Input: s = "abciiidef", k=3
// Output: 3

// Q28: Longest substring with repeated characters after replacement
// Input: s = "AABABBA", k=1
// Output: 4

// Q29: Find all anagrams in a string using sliding window
// Input: s = "cbaebabacd", p="abc"
// Output: [0,6]

// Q30: Longest substring with at most k distinct characters
// Input: s="aabbcc", k=2
// Output: 4 ("aabb")

// Q31: Count of subarrays with product less than k
// Input: nums = [10, 5, 2, 6], k=100
// Output: 8

// Q32: Longest alternating subarray
// Input: arr = [9,4,2,10,7,8,8,1,9]
// Output: 5
// Explanation: Max turbulent subarray

// Q33: Longest beautiful substring containing vowels in order
// Input: "aeiaaioaaaaeiiiiouuuooaauuaeiu"
// Output: 13

// Q34: Maximum sum subarray no more than k
// Input: arr = [2,2,-1] k=3
// Output: 3

// Q35: Maximum difference in all subarrays of size k
// Input: arr = [1,3,2,4,5], k=3
// Output: varies

// Q36: Count of subarrays with at most k odd numbers
// Input: arr=[2,2,2,1,2,2,1,2,2,2], k=2
// Output: 16

// Q37: Longest substring with equal number of a's and b's
// Input: s="abba"
// Output: 4

// Q38: Longest substring where you can replace k characters to get all same
// Input: s="AABABBA", k=1
// Output: 4

// Q39: Find all anagrams of p in s
// Input: s="cbaebabacd", p="abc"
// Output: [0,6]

// Q40: Largest sum subarray with at least k elements
// Input: arr=[-2,1,-3,4,-1,2,1,-5,4], k=2
// Output: 6

// Q41: Count distinct elements in every window of size k
// Input: arr=[1,2,1,3,4,2,3], k=4
// Output: [3,4,4,3]

// Q42: Find minimum window substring
// Input: S = "ADOBECODEBANC", T = "ABC"
// Output: "BANC"

// Q43: Smallest window containing all characters of another string
// Input: S="aabbcc", T="abc"
// Output: "abbc"

// Q44: Longest substring of all vowels in order
// Input: "aeiaaioaaaaeiiiiouuuooaauuaeiu"
// Output: 13

// Q45: Maximum sum of size k subarray
// Input: [100, 200, 300, 400], k=2
// Output: 700

// Q46: Longest substring with k distinct
// Input: "araaci", k=2
// Output: 4

// Q47: Count substrings with exactly k distinct chars
// Input: "pqpqs", k=2
// Output: 7

// Q48: Sliding window maximum
// Input: arr=[1,3,-1,-3,5,3,6,7], k=3
// Output: [3,3,5,5,6,7]

// Q49: Longest substring without repeating characters
// Input: "abcabcbb"
// Output: 3

// Q50: Count distinct numbers in windows
// Input: arr=[1,2,2,1,3], k=3
// Output: [2,2,3]

// ===============================================
// END OF QUESTIONS
