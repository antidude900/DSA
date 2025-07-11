"""
Approach:
We are given a string and we have to return the length of the longest substring with non repeating characters.
We use a hashmap to keep track of all the characters along with their index. Also we use left and right index for our substring
If we see a character in the hashmap and the index of it in the hashmap is >= left meaning this character still lies in the substring
(If we have a character say a of index 2 in the hashmap but the left of the substring is already 3, then it means it doesn't lie in our substring now),
then we update left of the substring to the repeated character's index at the hashmap + 1 (so that the character now doesnt lie in the substring)
and until we get any repeat, we will be checking if we got the highest length and also put the characters to our hashmap
"""

def lengthOfLongestSubstring(s: str) -> int:
    window = {}
    left = 0
    res = 0
    for right in range(len(s)):
        c = s[right]
        if c in window and window[c]>=left:
            left = window[c]+1
        else:
            res = max(res,right-left+1)
        window[c]=right
    return res

#Alternative (Using hash Set)
def lengthOfLongestSubstring(s: str) -> int:
        window = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])    #here we start removing characters from the left of the substring in the window until we removed the duplicate.
                                       #it runs on the fact that every other characters to the left of the character whose duplicate is found is not needed
                                       #as now we will be taking substring after the character whose duplicate is found
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
        return res
