# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

def count_1_substring(count):
    i=0
    ht=1

    while i<count:
        if i%2==0:
            ht=ht*2
        else:
            ht+=1
        i+=1

    return ht

ans=count_1_substring(5)
print(ans)

