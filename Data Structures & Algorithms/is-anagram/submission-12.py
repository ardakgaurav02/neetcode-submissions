class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = dict(Counter(s))

        for char in t:
            if char in char_count and char_count[char]!= 0:
                char_count[char] -= 1
        
        if sum(char_count.values()) == 0:
            return True
        return False