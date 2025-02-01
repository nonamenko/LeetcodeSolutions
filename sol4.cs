public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        var l = nums1.Length + nums2.Length;
        var merged = new int[l];
        var i = 0;
        var j = 0;
        for (var k = 0; k < l / 2 + 1; k++) {
            if (i >= nums1.Length) {
                merged[k] = nums2[j++];
                continue;
            }
            if (j >= nums2.Length) {
                merged[k] = nums1[i++];
                continue;
            }
            
            if (nums1[i] < nums2[j]) {
                merged[k] = nums1[i++];
            }
            else {
                merged[k] = nums2[j++];
            }
        }
        
        if (l % 2 == 1) {
            return merged[l / 2];
        }
        
        return (merged[l / 2 - 1] + merged[l / 2]) / 2.0f;
    }
}