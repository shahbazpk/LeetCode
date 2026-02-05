class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        count=0
        for ch in s[:k]:
            if ch in vowels:
                count+=1
        maxsum=count

        for i in range(k,len(s)):
            if s[i]in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            maxsum=max(maxsum,count)
        return maxsum