class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for value in strs:
            data = sorted(value)
            data = "".join(data)

            if data in d:
                d[data].append(value)
            else:
                d[data] = [value]

        return list(d.values())
