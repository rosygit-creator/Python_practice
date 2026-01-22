# find longest length between 2 arrays where the order is increasing order

def creat_teams(team_a, team_b):
    maxlen=0

    for i in range(0, len(team_a)):
        for j in range(0, len(team_b)):
            if team_b[j]>team_a[i]:
                result=is_increasing(j, len(team_b), team_b)
                maxlen=max(maxlen, result)


    return maxlen

def is_increasing(j1, len2, team_b):
    count=1 # for 1 elemnet of team_a

    for k in range(j1, len2-1):
        if team_b[j1]>team_b[j1+1]:
            count+=1
        else:
            break


    return count

ans=creat_teams([2,7,3],[4,2,6,8])
#2,2,6,8    3,6
print(ans)