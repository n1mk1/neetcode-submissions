class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = []
        for elem in nums:
            if elem in record:
                return True
            else:
                record.append(elem)
        return False