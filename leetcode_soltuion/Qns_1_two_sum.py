class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                sum = nums[i] + nums[j]
                print(sum)
                if sum == target:
                    return [i , j]
        
if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.twoSum(nums=[2, 7, 11, 15], target=9)
    print(ans)