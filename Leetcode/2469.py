from typing import List
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [round(celsius+273.15,5), round(celsius*1.80 + 32,5)]

print(Solution().convertTemperature(36.50))
print(Solution().convertTemperature(122.21))
        
