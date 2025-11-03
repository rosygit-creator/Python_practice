

def countprime(s, e):

 flag=False
 l=[]
 d=1

 for i in range(s, e+1):

     flagv=checkprime(i)
     # print(f"i is {i} and flagv is {flagv}")
     if flagv==True:
         l.append(i)
 return l



def checkprime(no):

    flag=True
    for j in range(2, int(no/2+1)):
      # print(f" no is {no} and j is {j}")
      q=no%j
      if q==0 :
          # print(f" q is {q}")
          flag=False
          break
      # else:
      #     flag=True

    return flag

start=20
end = 30
ans=countprime(start, end)
print(ans)