class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Map of difference/index
        Map<Integer, Integer> seen = new HashMap<>();

        for(int idx = 0; idx < nums.length; idx++) {
            int diff = target - nums[idx];
            if(seen.containsKey(diff)) {
                int[] result =  {
                    seen.get(diff),
                    idx};
                return result;
            }
            seen.put(nums[idx], idx);
        }
        return null;
    }
}
