class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # [(s_temp, s_idx)]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                s_temp, s_idx = stack.pop()
                res[s_idx] = idx - s_idx
            stack.append((temp, idx))
        return res
