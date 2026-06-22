class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diffMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if(diffMap.containsKey(difference)) {
                return new int[] {diffMap.get(difference), i};
            }
            diffMap.put(nums[i], i);
        }
        return new int[] {};
    }
}
