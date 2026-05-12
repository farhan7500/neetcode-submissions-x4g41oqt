class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int columns = matrix[0].length;

        int i = 0;
        int j = (rows * columns) - 1;

        while(i <= j) {
            int mid = (i + j) / 2;
            int midValue = matrix[mid / columns][mid % columns];

            if(midValue == target) {
                return true;
            } else if(midValue > target) {
                j = mid - 1;
            } else {
                i = mid + 1;
            }
        }
        return false;
    }
}
