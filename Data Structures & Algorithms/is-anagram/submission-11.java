class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> characterMap = new HashMap<>();

        for(char c: s.toCharArray()) {
            if(characterMap.containsKey(c)) {
                characterMap.put(c, characterMap.get(c) + 1);
            } else {
                characterMap.put(c, 1);
            }
        }

        for(char c: t.toCharArray()) {
            if(characterMap.containsKey(c)) {
                if(characterMap.get(c) == 0) {
                    return false;
                }
                characterMap.put(c, characterMap.get(c) - 1);
            } else {
                return false;
            }
        }

        for(int value: characterMap.values()) {
            if(value != 0) {
                return false;
            }
        }
        return true;
    }
}
