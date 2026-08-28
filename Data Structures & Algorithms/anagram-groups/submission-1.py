class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicos ={i: {} for i in range(len(strs))}
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                c = strs[i][j]
                if c not in dicos[i]:
                    dicos[i][c] = 1
                else:
                    dicos[i][c] = dicos[i].get(c, 0) + 1
        groupes = {}
        for i in range(len(strs)):
            cle = tuple(sorted(dicos[i].items()))
            if cle not in groupes:
                groupes[cle] = []
            groupes[cle].append(strs[i])
        L = list(groupes.values())
        return L

 