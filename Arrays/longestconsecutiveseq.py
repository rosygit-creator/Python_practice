


class Li1:


    def merge_lists(self, list1):
        list1.sort()
        c=1
        list3 = []
        for i in range(1, len(list1)):
            diff=list1[i] - list1[i-1]
            if diff==1:
                list3.append(list1[i-1])
                c+=1


        print(c)
        return list3

obj1 = Li1()
l1 = [2, 6, 1, 9, 4, 5, 3, 0,0] # 1,2,3,4,5,6,9

ans=obj1.merge_lists(l1)
print(ans)



