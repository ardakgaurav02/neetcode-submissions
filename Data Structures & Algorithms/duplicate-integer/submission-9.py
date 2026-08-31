class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m_set = set()

        for n in nums:
            if n in m_set:
                return True
            m_set.add(n)
        return False