class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_at_position = [0] * target

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            time_at_position[position[i]] = time

        fleets = 0
        slowest_time = 0

        for pos in range(target - 1, -1, -1):
            if time_at_position[pos] == 0:
                continue

            time = time_at_position[pos]

            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets