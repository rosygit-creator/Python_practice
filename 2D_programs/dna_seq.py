# https://leetcode.com/problems/repeated-dna-sequences/

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# return all the 10-letter-long sequences

def dna_seq(s1, k):
    l=[]
    for i in range(0, len(s1)-k+1):
            temp=s1[i:i+k]
            # print(temp)
            if temp not in l:
                l.append(temp)
            else:
                # if temp in l:
                print(temp)











    return


def dna_seq1(s1, k):
    l=[]
    for i in range(0, len(s1)-k+1):
            temp=s1[i:i+k]
            # print(temp)


ans=dna_seq("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", 10)
print(ans)



# print(len(ans))