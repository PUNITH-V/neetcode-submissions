class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in seen:
                seen[key].append(i)
            else:
                seen[key] = [i]
        return list(seen.values())


