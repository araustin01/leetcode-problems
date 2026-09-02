class Solution {

    private static final Map<Character, Integer> SYMBOL_MAP = new HashMap<Character, Integer> () {{
        put('I', 1);
        put('V', 5);
        put('X', 10);
        put('L', 50);
        put('C', 100);
        put('D', 500);
        put('M', 1000);
    }};

    public int romanToInt(String s) {
        int total = 0;

        for (int i=0, j=1; i < s.length(); i++, j++) {
            int value = SYMBOL_MAP.get(s.charAt(i)); // current roman symbol value
            int sflag = 1; // sign flag

            if (j < s.length()) {
                int next_value = SYMBOL_MAP.get(s.charAt(j)); // next roman symbol value
                if (next_value > value) {
                    sflag = -1;
                }
            }

            total += sflag * value;
        }
        
        return total;
    }
}