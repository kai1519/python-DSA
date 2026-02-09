class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        f = s = None

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                count += 1
                s = f
                f = i

            if count > 2:
                return False

        if f is None and s is None:
            return True
        if s is None or f is None:
            return False

        if s1[f] == s2[s] and s1[s] == s2[f]:
            return True

        return False
