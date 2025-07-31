function majorityElement(nums: number[]): number {
    // if i sort the array and take the median value,
    // i'm guaranteed it's always the majority element
    nums.sort();
    return nums[Math.floor(nums.length / 2)];
};