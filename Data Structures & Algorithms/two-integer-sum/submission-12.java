class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diffMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if(diffMap.containsKey(difference)) {
                int[] result = new int[2];
                result[0] = diffMap.get(difference);
                result[1] = i;
                return result;
            }
            diffMap.put(nums[i], i);
        }
        int[] result = {};
        return result;
    }
}
