class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) +  1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




        # hash_map = {}

        # for n in nums:
        #     if n in hash_map:
        #         hash_map[n] += 1
        #     else:
        #         hash_map[n] = 1

        # top_k = [num for num, freq in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)[:k]]
        # return top_k