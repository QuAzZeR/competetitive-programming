class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s = set(nums)
        if len(s) == 1:
            return "equilateral"
        
        if (nums[0] + nums[1] > nums[2]) and (nums[0] + nums[2] > nums[1]) and (nums[2] + nums[1] > nums[0]):
            if len(s) == 2:
                return "isosceles"
            else:
                return "scalene"
        return "none"
