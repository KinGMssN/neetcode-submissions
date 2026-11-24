class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        if l1 > l2:
            return False
        

        s1Map = [0] * 26
        s2Map = [0] * 26

        for i in range(l1):
            s1Map[ord(s1[i]) - 97] += 1
            s2Map[ord(s2[i]) - 97] += 1

        for i in range(l2 - l1):
            if self.matches(s1Map, s2Map):
                return True

            s2Map[ord(s2[i + l1]) - 97] += 1

            s2Map[ord(s2[i]) - 97] -= 1

        return self.matches(s1Map, s2Map)

    def matches(self, s1Map, s2Map):
        for i in range(26):
            if s1Map[i] != s2Map[i]:
                return False

        return True