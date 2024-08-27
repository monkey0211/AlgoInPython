import random
# quick_select 函数通过递归方式找到第 k 小的元素。每次选择一个随机的 pivot，将数组分为比 pivot 小的和比 pivot 大的两个部分，递归查找所需的部分。
# partition 函数是分区操作，用于将 pivot 放到它的正确位置。
# find_median 函数首先判断数组长度，如果是奇数则直接找中间元素；如果是偶数则找中间两个元素的平均值。
# time amortized o(n) space o(1)
def quick_select(arr, left, right, k):
    """在arr的[left, right]区间内，使用快速选择找到第k小的元素"""
    if left == right:
        return arr[left]
    
    # 随机选择一个pivot来避免最坏的时间复杂度
    pivot_index = random.randint(left, right)
    
    # 把pivot放到它正确的位置
    pivot_index = partition(arr, left, right, pivot_index)
    
    # 如果找到的是第k小的元素，返回该元素
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        # 在左边区间继续寻找
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        # 在右边区间继续寻找
        return quick_select(arr, pivot_index + 1, right, k)

def partition(arr, left, right, pivot_index):
    """对arr进行分区操作，把比pivot小的元素移到左边，比pivot大的移到右边"""
    pivot_value = arr[pivot_index]
    
    # 把pivot移动到末尾
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    # 把pivot移回到正确的位置
    arr[right], arr[store_index] = arr[store_index], arr[right]
    
    return store_index

def find_median(arr):
    """找到未排序数组的中位数"""
    n = len(arr)
    
    if n % 2 == 1:
        # 数组长度为奇数，直接找到中间元素
        return quick_select(arr, 0, n - 1, n // 2)
    else:
        # 数组长度为偶数，找到中间两个元素并取平均值
        left_median = quick_select(arr, 0, n - 1, n // 2 - 1)
        right_median = quick_select(arr, 0, n - 1, n // 2)
        return (left_median + right_median) / 2.0

# 示例：
arr = [3, 6, 2, 8, 1, 9, 4]
median = find_median(arr)
print("中位数是:", median)
