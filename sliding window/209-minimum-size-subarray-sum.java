import java.util.Arrays;

class Solution {
    public int minSubArrayLen(int target, int[] nums) {

        // edgecase: empty nums array or array sum too small
        if (nums.length == 0 || Arrays.stream(nums).sum() < target)
            return 0;

        int minLenSubArray = nums.length; // minimal length of subarray
        int windowLeftIdx = 0; // index of leftmost element in sliding window
        int windowRightIdx = 0; // index of rightmost element in sliding window
        int windowSum = nums[0]; // sum of elements in sliding window

        // variable size sliding window through nums:
        // while subarray sum < target, add element to right
        // then try to remove element to left
        while (true) {
            // add element to the right until window sum >= target
            while (windowSum < target && ++windowRightIdx < nums.length) {
                windowSum += nums[windowRightIdx];
            }

            // remove element to the left until window sum < target
            while (windowSum >= target && windowLeftIdx < windowRightIdx) {

                // if window size < curr min subarray size, update min subarray size
                if (windowRightIdx - windowLeftIdx + 1 < minLenSubArray)
                    minLenSubArray = windowRightIdx - windowLeftIdx + 1;

                windowLeftIdx++;
                windowSum -= nums[windowLeftIdx - 1];
            }

            if (windowRightIdx == nums.length)
                break;
            if (windowLeftIdx == windowRightIdx) {
                if (nums[windowLeftIdx] >= target)
                    return 1;
                break;
            }
        }

        return minLenSubArray;
    }
}