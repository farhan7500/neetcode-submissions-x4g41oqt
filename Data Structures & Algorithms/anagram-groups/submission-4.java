class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> gaMap = new HashMap<>();
        for(String inputStr: strs) {
            List<Integer> immutableList = getImmutableList(inputStr);
            if(gaMap.get(immutableList) == null) {
                List<String> newList = new ArrayList<>();
                newList.add(inputStr);
                gaMap.put(immutableList, newList);
            } else {
                List<String> currentList = gaMap.get(immutableList);
                currentList.add(inputStr);
                gaMap.put(immutableList, currentList);
            }
        }
        List<List<String>> resultList = new ArrayList<>();
        for(Map.Entry<List<Integer>, List<String>> gaMapEntries: gaMap.entrySet()) {
            resultList.add(gaMapEntries.getValue());
        }
        return resultList;
    }

    private List<Integer> getImmutableList(String inputString) {
        List<Integer> characterCountList = new ArrayList<>();
        for(int i = 0; i < 26; i++) {
            characterCountList.add(0);
        }
        for(char c: inputString.toCharArray()) {
            characterCountList.set(c - 'a', characterCountList.get(c - 'a') + 1);
        }
        return characterCountList;
    }
}
