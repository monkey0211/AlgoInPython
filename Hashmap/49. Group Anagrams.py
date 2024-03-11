class Solution:
    # time O(nklogk) space O(nk) k is length of each string
    # sort每一个string 然后放入defaultdict(list) in groups
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        res = []
        if not strs: return [[]]
        dict = collections.defaultdict(list)
        for str in strs:
            dict["".join(sorted(str))].append(str) #sorted() can used for iterable items, string will return a list. 
        
        for k in dict:
            res.append(dict[k])
        return res