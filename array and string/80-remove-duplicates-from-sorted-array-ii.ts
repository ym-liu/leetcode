function removeDuplicates(nums: number[]): number {

    if (nums.length <= 1) return nums.length; // edgecase: if 0 or 1 element in nums array

    let switchIdx: number = 0; // index of next element to switch with
    let finalNumsLength: number = 2; // length of nums array after removing duplicates

    // iterate through nums array
    for (let i: number = 2; i < nums.length; i++) {

        // if no more elements to switch with, break
        if (switchIdx >= nums.length) break;

        // if curr element <= prev element AND prev element === prev prev element,
        // or if curr element < prev element,
        // find next element to switch with
        if (
            (nums[i] <= nums[i - 1] && nums[i - 1] === nums[i - 2]) ||
            nums[i] < nums[i - 1]
        ) {
            // if prev element === prev prev element, increment switchIdx until UNIQUE element
            // if curr element < prev element, increment switchIdx until element that has appeared AT MOST ONCE
            while (
                switchIdx < nums.length &&
                ((nums[i - 1] === nums[i - 2] && nums[i - 1] >= nums[switchIdx]) ||
                 (nums[i] < nums[i - 1] && (nums[i - 1] > nums[switchIdx] || nums[i - 2] >= nums[switchIdx])))
            ) {
                switchIdx++;
            }

            // if no more elements to switch with
            if (switchIdx >= nums.length) break;

            // switch in-place
            nums[i] = nums[switchIdx];
            nums[switchIdx] = Number.NEGATIVE_INFINITY; // remove element at switchIdx
        }

        // increment final nums array length and switch index
        finalNumsLength++;
        switchIdx++;
    }

    return finalNumsLength;
}