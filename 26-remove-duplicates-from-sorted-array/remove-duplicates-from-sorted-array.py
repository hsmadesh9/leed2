class Solution(object):
    def removeDuplicates(self, num):
        if len(num)==0:
            return 0
        j=0
        for i in range(1,len(num)):
           if num[i]!=num[j]:
            j+=1
            num[j]=num[i]
        return j+1
        