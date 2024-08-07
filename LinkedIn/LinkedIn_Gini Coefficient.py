# given the number of connections of each linekdin member, calculate the gini coefficient


# 先构建一个dict: connection-># of members,
# 画图 % of connections->% of members
# 计算area的面积, 累加 -> 计算梯形面积
#input: connections: list of connection counts(index is memberId)

def gini_coefficient(connections): 
    connectionMap = collections.defaultdict(int) # connection个数->memberCnt
    memberTotal = 0
    connectionTotal = 0
    
    for i in range(len(connections)):
        memberTotal += 1 # member total总数
        connectionTotal += connections[i] # connection总数
        connectionMap[connections[i]] += 1 # connection数->memberCnt
    
    prevConnection = 0
    area = 0
    for connection, memberCnt in sorted(connectionMap.items()):
        curMemberP = memberCnt/memberTotal #这个就是incremental的横轴的差
        area += 0.5*curMemberP*(connection + prevConnection)/connectionTotal #梯形面积
        
        prevConnection += connection # connection需要累加(prevConnection就是上底)
    return 1 - 2*area # 面积

connections1 = [0,0,1,1,1,2,3,3,4,5]
connections = [0,0,0,1,0,0,1,0,0,0,0,0,0,0]
print(gini_coefficient(connections))