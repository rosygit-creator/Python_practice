# class MyClass:
#
#
#     def my_method(self, value):
#
#
#         print(f"Value: {value}")
# obj1=MyClass()
#
# obj1.my_method(10)


class Li1:


    def merge_lists(self, list1, list2):
        list3 = []
        for i in list1:
            if i not in list3:
                list3.append(i)

        for j in list2:
            if j not in list3:
                list3.append(j)
        list3.sort()
        print(list3)

    def union_lists(self, list1, list2):
        list4 = []
        # list4=list1

        list4=list1+list2

        list4.sort()
        print(f"list 4: {list4}")

obj1 = Li1()
l1 = [4, 5, 3, 4]
l2 = [4, 5, 6, 1, 3]

obj1.merge_lists(l1, l2)

obj1.union_lists(l1,l2)

