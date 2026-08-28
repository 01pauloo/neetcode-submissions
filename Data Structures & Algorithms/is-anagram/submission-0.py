class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = dict()
        for i in range(len(s)):
            if s[i] not in d1 :
                d1[s[i]] = 1
            else:
                d1[s[i]] = d1.get(s[i],d1[s[i]]) + 1

        d2 = dict()
        for j in range(len(t)):
            if t[j] not in d2 :
                d2[t[j]] = 1
            else:
                d2[t[j]] = d2.get(t[j],0) + 1
        '''
        diff =  {k: d1[k] - d2.get(k, 0) for k in d1}
        if all(v == 0 for v in diff.values()) is True:
            return True
        else:
            return False
        '''
        if d1 == d2:
            return True
        else:
            return False

