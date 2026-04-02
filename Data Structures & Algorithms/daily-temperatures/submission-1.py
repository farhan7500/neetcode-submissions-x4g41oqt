class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                s_idx, s_temp = stack.pop()
                res[s_idx] = idx - s_idx
            stack.append((idx, temperature))
        return res
        