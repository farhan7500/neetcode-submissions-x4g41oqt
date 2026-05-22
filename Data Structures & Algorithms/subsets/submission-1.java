class Solution {
    List<Integer> solution = new ArrayList<>();
    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {

        backtrack(0, nums);

        return result;
        
    }

    private void backtrack(int i, int[] nums) {
        int n = nums.length;
        if(i == n) {
            result.add(new ArrayList<>(solution));
            return;
        }
        backtrack(i + 1, nums);

        solution.add(nums[i]);
        backtrack(i + 1, nums);
        solution.remove(solution.size() - 1);
    }
}
