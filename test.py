import collections

class Test:
    def mergeTwo(self, nums1, nums2):
        # @return a sorted nums
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
         
            elif nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
          
            else:
                nums.append(nums2[j])
                i += 1
                j += 1
           
        while i < len(nums1):
            nums.append(nums1[i])
            i += 1
       
        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
       
        return nums

test = Test()
print(test.mergeTwo([1,3,4],[2,3,5]))
        
            

                
                