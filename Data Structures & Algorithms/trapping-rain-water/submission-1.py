class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_list = []
        max_right_list = []
        current = 0
        for element in height:
            if len(max_left_list) == 0:
                max_left_list.append(0)
                current = element
            else:
                if element > current:
                    max_left_list.append(current)
                    current = element
                else:
                    max_left_list.append(current)

        for element in height[::-1]:
            if len(max_right_list) == 0:
                max_right_list.append(0)
                current = element
            else:
                if element > current:
                    max_right_list.append(current)
                    current = element
                else:
                    max_right_list.append(current)

        total = 0
        for i in range(len(max_left_list)):
            if min(max_left_list[i], max_right_list[0-i]) - height[i] > 0:
                total += min(max_left_list[i], max_right_list[0-i]) - height[i]

        return total
        