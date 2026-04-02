class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> characterMap = new HashMap<>();
        for(char character: s.toCharArray()) {
            if(characterMap.containsKey(character)) {
                int value = characterMap.get(character);
                characterMap.put(character, value + 1);
            } else {
                characterMap.put(character, 1);
            }
        }

        for(char character: t.toCharArray()) {
            if(characterMap.containsKey(character)) {
                int value = characterMap.get(character);
                if(value == 0) {
                    return false;
                }
                characterMap.put(character, value - 1);
            } else {
                return false;
            }
        }

        for(Map.Entry<Character, Integer> entry: characterMap.entrySet()) {
            if(entry.getValue() != 0) {
                return false;
            }
        }
        return true;
    }
}
