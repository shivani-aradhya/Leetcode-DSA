class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)

        for i in range(len(strs)):
            key = sorted(strs[i])
            key = ''.join(key)
            anagram[key].append(strs[i])

        output = []
        for i in anagram.values():
            output.append(i)

        return output