class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_list = [n for n in zip(position, speed)]
        position_speed_list.sort(reverse=True) # O(nlogn)
        print(position_speed_list)
        stack = []
        for position, speed in position_speed_list:
            time = (target - position) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)