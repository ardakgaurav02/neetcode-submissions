class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1

        top_k = [num for num, freq in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)[:k]]
        return top_k