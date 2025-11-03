
#Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
# If no such two words exist, return 0.

# Example 1:
#
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

def distinct_product(input):
   if len(input)==0:
        return 0
   prod=1
   res=0
   l=[]
   for i in range(0,len(input)-1):
       prod=1

       for j in range(i+1,len(input)):
           set1=set(input[i])
           set2=set(input[j])
           if len(set1.intersection(set2))==0:
               prod=len(input[i])*len(input[j])
               if prod>res:
                   res=prod
                   l.clear()
                   l.append([input[i],input[j]])
   print(l)



   return res





s = ["abcw","baz","foo","bar","xtfn","abcdef"]
s=["aa", "ab"]

ans=distinct_product(s)

print(ans)

