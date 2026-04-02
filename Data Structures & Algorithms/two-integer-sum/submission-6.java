class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> differenceMap = new HashMap();
        for(int idx = 0; idx < nums.length; idx++) {
            int difference = target - nums[idx];
            if(differenceMap.containsKey(nums[idx])) {
                return new int[]{differenceMap.get(nums[idx]), idx};
            }
            differenceMap.put(difference, idx);
        }
        return null;
    }
}
