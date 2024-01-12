class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime)%24
print(Solution().findDelayedArrivalTime(15,5))
print(Solution().findDelayedArrivalTime(13,11))
print(Solution().findDelayedArrivalTime(13,12))
