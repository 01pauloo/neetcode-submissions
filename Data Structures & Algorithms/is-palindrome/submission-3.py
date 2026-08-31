class Solution:
    def isPalindrome(self, s: str) -> bool:
        convention = str.maketrans("", "", " :',!?." )
        s1 = s.lower().replace(" ", "").translate(convention)
        if s1 == s1[::-1]:
            return True
        else:
            return False