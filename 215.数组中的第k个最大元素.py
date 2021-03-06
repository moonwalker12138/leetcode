#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (60.15%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    67.2K
# Total Submissions: 111.7K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
def swap(array:list, i:int, j:int):
    array[i], array[j] = array[j], array[i]

def partition_one_way_scanning(array:list, left:int, right:int):
    pivot = array[left]
    # * index: postion of the last number smaller than pivot
    index = left
    for i in range(left+1, right+1):
        if array[i] < pivot:
            index += 1
            swap(array, index, i)
    swap(array, index, left)
    return index

def partition_two_way_scanning(array:list, left:int, right:int):
    pivot = array[left]
    while left < right:
        while left < right and array[right] >= pivot: 
            right -= 1
        # * Now if left < right, then right is index of the rightmost number smaller than pivot
        if left < right: array[left] = array[right]
        while left < right and array[left] <= pivot:
            left += 1
        # * Now if left < right, then left is index of the leftmost number greater than pivot
        if left < right: array[right] = array[left]
    array[left] = pivot
    return left

def quick_sort(array:list, left:int, right:int, partition:callable):
    """ quick sort with two partition strategy （one_way_scanning and two_way_scanning) """
    if left < right:
        pivot_index = partition(array, left, right)
        quick_sort(array, left, pivot_index-1, partition)
        quick_sort(array, pivot_index+1, right, partition)
    return array

def quick_select(array:list, left:int, right:int, k_smallest:int, partition:callable):
    """ select the k smallest number of array[left, right] 
    和 quick_sort 类似，但是通过判断 pivot_index 和 k_smallest 的大小每次只需处理一个分支（quick_sort 需处理全部两个分支），
    因此平均复杂度由 O(NlogN) 降低为 O(N), 但是该算法只能获取第k小的数，不能保证k两边的数组有序
    """
    if left == right: return array[left]
    pivot_index = partition(array, left, right)
    if pivot_index == k_smallest:
        return array[pivot_index]
    elif pivot_index > k_smallest:
        return quick_select(array, left, pivot_index-1, k_smallest, partition)
    else:
        return quick_select(array, pivot_index+1, right, k_smallest, partition)

def sort(array:list, left:int, right:int):
    for i in range(left, right+1):
        for j in range(i+1, right+1):
            if array[j] < array[i]:
                swap(array, j, i)
    return array

def findMedian(array:list, left:int, right:int):
    """ 将array按照五个一组分组，求出每个分组的中位数，再将这些中位数按照五个一组分组，递归求解直至
    最终只剩一个数，即为所求中位数
    """
    n_groups = 0
    for i in range(left, right+1, 5):
        if i + 4 <= right:
            quick_sort(array, i, i+4, partition_two_way_scanning)
            swap(array, left+n_groups, i+2)
        else:
            # 最后一组可能不足五个
            quick_sort(array, i, right, partition_two_way_scanning)
            swap(array, left+n_groups, i+(right-i+1)//2)
        n_groups += 1
    # * 返回值不重要，array[0]即为所求中位数
    if n_groups == 1:
        return array[0]
    else:
        return findMedian(array, left, left+n_groups-1)

def BFPRT(array:list, left:int, right:int, k_smallest:int, partition:callable):
    """ 和 quick_select 大体相同，仅仅改变了pivot的选择方式，每次选择五分中位数的中位数作为pivot，
    该算法最差情况复杂度为 O(N)
    """
    if left == right: return array[left]
    # findMedian 执行结束后 array[0] 即为所求中位数
    findMedian(array, left, right)
    pivot_index = partition(array, left, right)
    if pivot_index == k_smallest:
        return array[pivot_index]
    elif pivot_index > k_smallest:
        return BFPRT(array, left, pivot_index-1, k_smallest, partition)
    else:
        return BFPRT(array, pivot_index+1, right, k_smallest, partition)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return BFPRT(nums, 0, len(nums)-1, len(nums)-k, partition_two_way_scanning)
# @lc code=end

