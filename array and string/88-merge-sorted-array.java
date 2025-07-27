class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        // if either array is empty, soln is the other array
        if (m == 0) {
            System.arraycopy(nums2, 0, nums1, 0, n);
            return;
        } else if (n == 0)
            return;

        // iterate through soln array backward, adding next largest integer one-by-one
        int nums1Index = m - 1;
        int nums2Index = n - 1;
        for (int i = m + n - 1; i >= 0; i--) {
            if (nums2Index < 0 || (nums1Index >= 0 && nums1[nums1Index] >= nums2[nums2Index])) {
                nums1[i] = nums1[nums1Index];
                nums1Index--;
            } else {
                nums1[i] = nums2[nums2Index];
                nums2Index--;
            }
        }
    }
}