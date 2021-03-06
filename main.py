import numpy as np

def min_edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    #记录开销的矩阵
    solutionmatrix = np.zeros((len2, len1))

    #初始化
    for i in range(0, len1):
        solutionmatrix[0][i] = i
    for i in range(0, len2):
        solutionmatrix[i][0] = i

    #记录路径的矩阵,并初始化之前初始化的路径
    recordmatrix1 = np.zeros((len2, len1))
    for i in range(0, len1):
        recordmatrix1[0][i] = 3
    for i in range(0, len2):
        recordmatrix1[i][0] = 4
    recordmatrix1[0][0] = 100  #回溯终止符

    recordmatrix2 = np.zeros((len2, len1))
    for i in range(0, len1):
        recordmatrix2[0][i] = 3
    for i in range(0, len2):
        recordmatrix2[i][0] = 4
    recordmatrix2[0][0] = 100  #回溯终止符

    #判断两个字符串当前位置是否相等
    cost = 0
    for i in range(1, len2):
        for j in range(1, len1):
            if str1[j] == str2[i]:
                cost = 0
            else:
                cost = 1

            #计算开销
            replace = solutionmatrix[i-1][j-1] + cost
            add = solutionmatrix[i][j-1] + 1
            delete = solutionmatrix[i-1][j] +1
            solutionmatrix[i][j] = min(replace, add, delete)

            #记录路径，操作的优先级不同，路径也不同，这里仅拿两种优先级举例
            prior1 = [replace, add, delete]     #替换优于添加
            prior2 = [add, replace, delete]     #添加优于替换
            whichone1 = prior1.index(min(prior1))
            whichone2 = prior2.index(min(prior2))

            #记录【i，j】是怎么变化而来的  2=替换，3=添加，4=删除，5=保留
            if whichone1 == 0 and cost == 1:
                recordmatrix1[i][j] = 2
            elif whichone1 == 0 and cost == 0:
                recordmatrix1[i][j] = 5
            elif whichone1 == 1:
                recordmatrix1[i][j] = 3
            else:
                recordmatrix1[i][j] = 4

            if whichone2 == 0:
                recordmatrix2[i][j] = 3
            if whichone2 == 1 and cost == 1:
                recordmatrix2[i][j] = 2
            elif whichone2 == 1 and cost == 0:
                recordmatrix2[i][j] = 5
            else:
                recordmatrix2[i][j] = 4

    #回溯路径
    i1 = len2-1
    j1 = len1-1
    temp1 = recordmatrix1[i1][j1]
    record1 = []
    while temp1 != 100:
        if temp1 == 2:
            i1=i1-1
            j1=j1-1
            record1.append('replace')
        elif temp1 == 5:
            i1 = i1 - 1
            j1 = j1 - 1
            record1.append('retain')

        elif temp1 == 3:
            j1=j1-1
            record1.append('add')
        elif temp1 ==4:
            i1=i1-1
            record1.append('delete')
        temp1 = recordmatrix1[i1][j1]
    record1.reverse()

    i2 = len2-1
    j2 = len1-1
    temp2 = recordmatrix2[i2][j2]
    record2 = []
    while temp2 != 100:
        if temp2 == 2:
            i2=i2-1
            j2=j2-1
            record2.append('replace')
        elif temp2 == 5:
            i2 = i2 - 1
            j2 = j2 - 1
            record2.append('retain')

        elif temp2 == 3:
            j2=j2-1
            record2.append('add')
        elif temp2 ==4:
            i2=i2-1
            record2.append('delete')
        temp2 = recordmatrix2[i2][j2]
    record2.reverse()

    print('最小编辑距离为：', solutionmatrix[len2-1][len1-1])
    print()
    print('动态规划矩阵为： ')
    print(solutionmatrix)
    print()
    print('当多种操作开销相同时，替换操作优先级最高的记录矩阵：')
    print(recordmatrix1)
    print('该记录矩阵对应的操作序列：')
    print(record1)
    print()
    print('当多种操作开销相同时，添加操作优先级最高的记录矩阵：')
    print(recordmatrix2)
    print('该记录矩阵对应的操作序列：')
    print(record2)




str1 = input("请输入str1： ")
str2 = input("请输入str2： ")
str1 = '#' + str1
str2 = '#' + str2

#str1 = list(str1)
#str2 = list(str2)
print('---------------将str1转化为str2的最小编辑距离--------------------')
min_edit_distance(str2,str1)
print()
print('---------------将str2转化为str1的最小编辑距离--------------------')
min_edit_distance(str1,str2)
