nums1=[3,5,9,0,0,0]
nums2=[2,7,11]
def mergeSortedArray(nums1,nums2):
    m=0
    for i in nums1:
        if i!=0:
            m+=1
        else:
            break
    n=len(nums2)
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if nums1[i]>=nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    while j>=0:
        nums1[k]=nums2[j]
        j-=1
        k-=1
    return nums1
print(mergeSortedArray(nums1,nums2))
        
        
    