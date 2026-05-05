# 3sum


def print_string(input):
   output_s=""
   o=input.split(" ")[::-1] #  sunday is rosy

   # a=o[::-1] # sunday is rosy
   # print(f"a is {a}") #sunday is rosy
   for item in o:  # for item in a: will print yadnus si ysor
       output=item[::-1]
       output_s=output_s+output+ " "

   # print(f" output  {output_s}") # ysor si yadnus


    # print(input)
    # print(len(input))
    # for c in (s):
    #     print(c)
    # print(s[::-1])
    #



   return output_s

s = "rosy is sunday"
ans=print_string(s)

print(ans)

