class Solution:
    def checkInclusion(self, s: str, t: str) -> bool:
        return (c:=Counter(s))==(z:=Counter(t[:len(s)])) or any(z.update(q) or z.subtract(p) or c==z for p,q in zip(t,t[len(s):]))