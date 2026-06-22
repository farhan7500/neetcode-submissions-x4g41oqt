class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        int[] charAppearances = new int[26];
        for(int i = 0; i < s.length(); i++){
            charAppearances[s.charAt(i) - 'a']++;
            charAppearances[t.charAt(i) - 'a']--;
        }

        for(int num: charAppearances) {
            if(num != 0){
                return false;
            }
        }
        return true;
    }
}
