class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = collections.defaultdict(list)

        for s in strs:
            # Tuples are hashable and avoid intermediate string reconstruction
            sorted_key = tuple(sorted(s))
            anagram_map[sorted_key].append(s)

        return list(anagram_map.values())