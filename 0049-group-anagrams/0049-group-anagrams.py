class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use sorted on each string as a key for the deafultdict then add the relveant word to the deafult list as a value 
        output=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            output[key].append(word)
        return list(output.values())
    
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
# where n is the number of strings in the input list and k is the maximum length of a string