def bill_division(bill, ana_index):
    total=sum(bill) #22
    ana_temp=0
    shared_bill=0
    ana_final=0
    bob_final=0
    shared_bill=total
    for i in range(0,len(ana_index)):
        ana_temp=ana_temp+bill[ana_index[i]] #14
        
        print("bill[ana_index[i]", bill[ana_index[i]])
        # shared_bill=shared_bill-bill[ana_index[i]] #8
        print("shared_bill", shared_bill)

    print("ana _t", ana_temp)
    print("shared_bill", shared_bill)
    ana_final=ana_temp+(shared_bill/2) 
    print("ana _f", ana_final)
    print(ana_final)
    bob_final=total-ana_final
    


    return bob_final


bill=[2,4,6,10]
ana_index=[1,3]

ans=bill_division(bill, ana_index)
print(ans)



