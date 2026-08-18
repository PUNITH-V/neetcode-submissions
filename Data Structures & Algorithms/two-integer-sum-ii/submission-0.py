class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = numbers
        n = len(s)
        left = 0
        right = n -1
        while left < right:
            while s[left] + s[right] > target:
                right -=1
            while s[left] +s[right] < target:
                left +=1
            if s[left] + s[right] == target:
                return [left+1, right+1]
        return []