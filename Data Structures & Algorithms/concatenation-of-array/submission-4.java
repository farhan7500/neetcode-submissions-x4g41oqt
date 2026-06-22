class Solution {
    public int[] getConcatenation(int[] nums) {
        int numsLength = nums.length;
        int[] newNums = new int[2 * numsLength];
        for(int i = 0; i < numsLength; i++) {
            newNums[i] = nums[i];
            newNums[i + numsLength] = nums[i];
        }
        return newNums;
    }
}