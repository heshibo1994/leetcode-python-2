class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([i for i in range(len(S)) if S[i] in J ])