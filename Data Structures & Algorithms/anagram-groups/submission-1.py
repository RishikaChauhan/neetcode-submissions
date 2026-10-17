class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for str in strs:
            if ''.join(sorted(str)) in d.keys():
                d[''.join(sorted(str))].append(str)
            else:
                d[''.join(sorted(str))] = [str]
        return list(d.values())