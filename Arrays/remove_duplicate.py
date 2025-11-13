



class Li1:


    def merge_lists(self, list1):
        list3 = []
        k=0
        for i in range(1,len(list1)):
            if list1[i] !=list1[k]:
                k=k+1
                list1[k]=list1[i]

        print(k)
        print(list1)

        del list1[k+1:]
        return list1

    def remove_element(self, list1):

    # remove 2
        list1.remove(2) # last item removal: lis1.pop()
    # remove at index 3
        list1.pop(3) # or del lis1[3]
        return list1

obj1 = Li1()
l1 = [5, 2, 4, 4, 1,1]

len1=obj1.merge_lists(l1)
print(len1)

l2 = [5, 2, 4, 4, 1,1]
len2=obj1.remove_element(l2)
print(f"len2 is  {len2}")

