def board1(b):
    input="ABCCED"
    flag=False
    for c in input:
        flag=False
        for i in range(0,len(b)):
            # print(f"rows is {len(b)}")
            # print(f"cols is {len(b[0])}")

            for j in range(0, len(b[0])):
                if c==b[i][j]:
                    flag=True
                    b[i][j]=-1
                    # print(b)
                    break # break inner for
                # print(b[i])
            if flag==True:
                break # break outer for
        if flag==False:
            return flag



    return flag

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
ans=board1(board)
print(ans)