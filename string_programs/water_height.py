def water_height(a):
    left=0
    right=len(h)-1
    final_area=0

    while left<right:
        curr_ht=min(a[left], a[right])
        curr_width=right-left
        curr_area=curr_ht * curr_width

        final_area=max(final_area, curr_area)

        if a[left]<a[right]:
            left+=1
        else:
            right-=1


    return final_area

h=[1,8,6,2,5,4,8,3,7]
ans=water_height(h)
print(ans)