class Solution:
    def reverseWords(self, s: str) -> str:
        trim=s.strip()
        words=trim.split()
        i=0
        j=len(words)-1

        while i<j:
            temp=words[i]
            words[i]=words[j]
            words[j]=temp

            i+=1
            j-=1
        return " ".join(words) 