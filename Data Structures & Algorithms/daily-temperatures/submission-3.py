class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_t = len(temperatures)
        res = [0] * len_t
        stack = []

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((t, idx))

        return res