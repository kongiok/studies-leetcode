from typing import List


class Solution:
    def two_sum(self, nums:List[int], target: int)-> List[int]:
        """
        Assumption Detect
        """
        if not (len(nums) <= 10**4 and len(nums) >= 2):
            raise ValueError("Length of Given numbers should between 2 and 10^4")
        for num in nums:
            if not (num >= -(10**9) and num <= 10**9):
                raise ValueError("Given Number should between 10^9 and -(10^9)")
        if not (target >= -(10**9) and target <= 10**9):
            raise ValueError("Given Target should between 10^9 and -(10^9)")
        """
        Logic Part
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] != target:
                    continue;
                return [i,j];
        return [];

if __name__ == '__main__':
    two_sum = Solution().two_sum([2, 7, 11, 15], 9);
    print(f"Result of two_sum: {two_sum}");
