class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = right = 0

        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        curr_freq = [0] * 26

        while right < len(s2):
            # Add incoming
            curr_freq[ord(s2[right]) - ord('a')] += 1

            # Check condition
            if right - left + 1 > len(s1):
                curr_freq[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                if curr_freq == s1_freq:
                    return True
            
            right += 1
        
        return False
        