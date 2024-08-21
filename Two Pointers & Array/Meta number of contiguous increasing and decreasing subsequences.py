'''
https://leetcode.com/discuss/interview-experience/1833775/meta-london-9th-march
For a given distinct integer sequence of size N, 
the task is to count the number of contiguous increasing subsequence 
and contiguous decreasing subsequence in this sequence.

Examples: 
Input: arr[] = { 80, 50, 60, 70, 40 } 
Output: 1 2 
Explanation: 
The only one increasing subsequence is (50, 60, 70) and 
two decreasing subsequences are (80, 50) and (70, 40).
Input: arr[] = { 10, 20, 23, 12, 5, 4, 61, 67, 87, 9 } 
Output: 2 2 
Explanation: 
The increasing subsequences are (10, 20, 23) and (4, 61, 67, 87) 
whereas the decreasing subsequences are (23, 12, 5, 4) and (87, 9). 

Approach: The idea behind solving this problem is to use two arrays 
which keeps the track of increasing or decreasing indices based on next elements. 
 
Define two arrays max and min, such that the index of an element of the array is stored. 
For the first element of the array, if it is greater than its next element, it's index is stored in the max array, 
else it is stored in the min array and so on.
For the last element of the array, if it is greater than the previous element, it's index is stored in the max array, 
else it is stored in min array.

After this, all the maximal contiguous increasing subsequences are matched from (min to max), 
while all the maximal contiguous decreasing subsequences are matched from (max to min).

Finally, if the index of the first element of array is stored in the first index of min array, 
then the number of maximal contiguous increasing subsequence possible is size of min array,
and maximal contiguous decreasing subsequences possible is (size of max array - 1).

If the index of the first element of the array is stored in the first index of the max array, 
then the number of maximal contiguous increasing subsequence possible is(size of the max array -1),
and maximal contiguous decreasing subsequences possible is the size of min array.
时间O(n)  空间O(n)
'''
def numOfSubseq(arr):
    i, inc_count, dec_count = 0, 0, 0
    n = len(arr)
    max = [0]*n
    min = [0]*n
 
    # k2, k1 are used to store the
    # count of max and min array
    k1 = 0
    k2 = 0
 
    # Comparison to store the index of
    # first element of array
    if (arr[0] < arr[1]):
        min[k1] = 0
        k1 += 1
    else:
        max[k2] = 0
        k2 += 1
 
    # Comparison to store the index
    # from second to second last
    # index of array
    for i in range(1, n-1):
        if (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
            min[k1] = i
            k1 += 1
 
        if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
            max[k2] = i
            k2 += 1
 
    # Comparison to store the index
    # of last element of array
    if (arr[n - 1] < arr[n - 2]):
        min[k1] = n - 1
        k1 += 1
    else:
        max[k2] = n - 1
        k2 += 1
 
    # Count of number of maximal contiguous
    # increasing and decreasing subsequences
    if (min[0] == 0):
        inc_count = k2
        dec_count = k1 - 1
    else:
        inc_count = k2 - 1
        dec_count = k1
    
    #print("Increasing Subsequence Count: ", inc_count)
    #print("Decreasing Subsequence Count: ", dec_count)

    return inc_count + dec_count

# unit test
arr1 = [7, 4, 2, 2, 2, 1] # 1
arr2 = [5, 5, 5, 8, 19, 14, 4, 1] # 2
print(numOfSubseq(arr1))
print(numOfSubseq(arr2))


'''
假设输入数组为 arr[] = {10, 20, 15, 25, 5}。我们按照解法的步骤进行分析：

输入数组分析
arr[] = {10, 20, 15, 25, 5}
步骤 1: 初始化
max = [0, 0, 0, 0, 0]
min = [0, 0, 0, 0, 0]
k1 = 0 (用于递减子序列)
k2 = 0 (用于递增子序列)
步骤 2: 处理数组第一个元素
比较 arr[0] 和 arr[1]:

arr[0] = 10，arr[1] = 20，10 < 20，这是一个递增的开端，因此 min[0] = 0，k1 = 1。
步骤 3: 遍历数组中间元素
i = 1 (arr[1] = 20)

arr[1] > arr[0] 且 arr[1] > arr[2]，20 是一个局部波峰。
存储 max[0] = 1，k2 = 1。
i = 2 (arr[2] = 15)

arr[2] < arr[1] 且 arr[2] < arr[3]，15 是一个局部波谷。
存储 min[1] = 2，k1 = 2。
i = 3 (arr[3] = 25)

arr[3] > arr[2] 且 arr[3] > arr[4]，25 是一个局部波峰。
存储 max[1] = 3，k2 = 2。
步骤 4: 处理数组最后一个元素
比较 arr[4] 和 arr[3]:

arr[4] = 5，arr[3] = 25，5 < 25，5 是递减的终点。
存储 min[2] = 4，k1 = 3。
步骤 5: 计算递增和递减子序列的数量
根据 min[] 和 max[] 的情况：

min[0] = 0，说明数组以递增子序列开始。
递增子序列数量 inc_count = k2 = 2。
递减子序列数量 dec_count = k1 - 1 = 2。
输出
因此，结果为:

递增子序列的数量: 2
递减子序列的数量: 2
递增和递减子序列
在这个例子中：

递增子序列: (10, 20) 和 (15, 25)
递减子序列: (20, 15) 和 (25, 5)
'''