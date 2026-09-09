class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paris = list(zip(position,speed))
        stack =[]
        for p, s in sorted(paris, reverse=True):
            time = (target - p)/s

            if not stack or time > stack [-1]:
                stack.append(time)
        return len(stack)