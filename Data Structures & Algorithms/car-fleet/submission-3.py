class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[p, s] for p, s in zip(position, speed)]
        position_speed.sort(key=lambda x: x[0], reverse=True)

        longest_time = 0.0
        fleets = 0
        for pos, sp in position_speed:
            time = (target - pos) / sp
            if time > longest_time:
                fleets += 1
                longest_time = time
        return fleets
