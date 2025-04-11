class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        s = s.lower()
        s_list = [char for char in s if char.isalpha() or char.isdigit()]
        s = "".join(s_list)
        return s == s[::-1] 