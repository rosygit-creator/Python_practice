def transact(transactions):
    parsed = []
    invalid=set()

    for t1 in transactions:
        name, time, amt, city=t1.split(',')
        parsed.append({'name':name, 'time':int(time), 'amt':int(amt), 'city': city})
    # print(parsed)
    # parsed is a list of dictionaries
    for i in range(0, len(parsed)):
        # print(parsed[i])
        if parsed[i]['amt']>1000:
            invalid.add(transactions[i]) # tries to add a dictionary to a set — and dictionaries are unhashable, so Python won’t allow it
            for j in range(i+1, len(parsed)):
                if (parsed[i]['name']==parsed[j]['name'] and
                    parsed[i]['city']!=parsed[j]['city'] and 
                    abs(parsed[i]['time']- parsed[j]['time'])<=60):
                    invalid.add(transactions[i])
    return invalid


t = ["alice,20,8000,mtv","alice,50,100,beijing"]
ans=transact(t)
print(ans)



