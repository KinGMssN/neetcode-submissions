class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=''.join(c for c in s if c.isalnum())
        return ns.lower()==ns[::-1].lower()