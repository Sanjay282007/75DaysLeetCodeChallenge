class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)//2
        if sum(nums)%2==0:
            dp=[[-1] * (target + 1) for _ in range(len(nums) + 1)]
            return self.fun(nums, len(nums), target,dp)
        else:
            return False
    def fun(self,nums,n,target,dp):
        if target==0:
            return True
        if n==0:
            return False
        if dp[n][target] != -1:
            return dp[n][target]
        if nums[n-1]>target:
            dp[n][target]=self.fun(nums,n-1,target,dp)
            return dp[n][target]
        left=self.fun(nums,n-1,target-nums[n-1],dp)
        right=self.fun(nums,n-1,target,dp)
        dp[n][target]= left or right
        return dp[n][target]