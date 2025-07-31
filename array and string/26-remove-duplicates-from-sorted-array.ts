function removeDuplicates(nums: number[]): number {

    if (nums.length === 0) return 0; // edgecase: if empty nums array

    let switchIdx: number = 0; // index of next unique element to switch with
    let numUniqueElements: number = 1; // number of unique elements

    // iterate through nums array
    for (let i: number = 1; i < nums.length; i++) {

        // if curr element === prev element, find next unique element to switch with
        if (nums[i] <= nums[i - 1]) {

            // if next element not unique, increment switchIdx until unique
            while (switchIdx < nums.length && (nums[i] >= nums[switchIdx] || nums[i - 1] >= nums[switchIdx])) {
                switchIdx++;
            }

            // if no more unique elements to switch with
            if (switchIdx >= nums.length) break;

            // switch in-place
            nums[i] = nums[switchIdx];
        }

        // increment num of unique elements
        numUniqueElements++;
    }

    return numUniqueElements;
}