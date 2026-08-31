class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}

        for ch in s:
            char_map[ch] = char_map.get(ch, 0) +1

        for char in t:
            if char in char_map and char_map[char] != 0:
                char_map[char] -= 1
            else:
                return False
        return True



        
