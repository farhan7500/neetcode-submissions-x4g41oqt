class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1) - 1

        def check_anagram(p1, p2):
            list1 = [0] * 26
            for c in p1:
                list1[ord(c) - ord('a')] += 1

            list2 = [0] * 26
            for c in p2:
                list2[ord(c) - ord('a')] += 1

            return list1 == list2

        while right < len(s2):
            if check_anagram(s1, s2[left: right + 1]):
                return True
            left += 1
            right += 1
        return False

s = Solution()
s1 = "abc"
s2 = "lecabee"
print(s.checkInclusion(s1, s2))
