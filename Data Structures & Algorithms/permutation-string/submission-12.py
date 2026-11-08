class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1) - 1

        # Build initial list

        s1_list = [0] * 26
        subset_list = [0] * 26
        for c in s1:
            s1_list[ord(c) - ord('a')] += 1

        for c in s2[:right + 1]:
            subset_list[ord(c) - ord('a')] += 1

        if s1_list == subset_list:
            return True

        left += 1
        right += 1

        while right < len(s2):
            subset_list[ord(s2[right]) - ord('a')] += 1
            subset_list[ord(s2[left - 1]) - ord('a')] -= 1

            if s1_list == subset_list:
                return True

            left += 1
            right += 1

        return False

