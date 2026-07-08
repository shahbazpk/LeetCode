class Solution:
    def checkInclusion(self, s: str, t: str) -> bool:
        return (c:=Counter(s))==(z:=Counter(t[:len(s)])) or any(z.update({p:-1,q:1}) or c==z for p,q in zip(t,t[len(s):]) if p!=q)