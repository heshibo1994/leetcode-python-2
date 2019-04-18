class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for i in str:
            if i.islower():
                ans += i
            else:
                ans += i.upper()
        return ans
