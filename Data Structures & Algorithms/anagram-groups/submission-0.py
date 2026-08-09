class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in ana:
                ana[key] = []
            ana[key].append(s)
        return list(ana.values())