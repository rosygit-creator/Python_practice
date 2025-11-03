# 3sum


def print_string(input):
   output_s=""
   o=input.split(" ") # rosy is sunday
   a=o[::-1] # sunday is rosy
   for item in o:
       output=item[::-1]
       output_s=output_s+output+ " "
   print(f" output  {output_s}")
    # print(input)
    # print(len(input))
    # for c in (s):
    #     print(c)
    # print(s[::-1])
    #



   return a

s = "rosy is sunday"
ans=print_string(s)

print(ans)

