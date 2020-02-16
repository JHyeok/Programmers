package main.level1.가운데_글자_가져오기;

class Solution {
    public String solution(String s) {
        String answer = "";
        int width = s.length();
        char[] c = null;
        c = s.toCharArray();

        if (width % 2 == 0) {
            // 짝수
            for (int i = 0; i < s.length(); i++) {
                if (s.length() / 2 == i) {
                    answer = answer + Character.toString(c[i - 1]);
                    answer = answer + Character.toString(c[i]);
                }
            }
        } else {
            // 홀수
            for (int i = 0; i < s.length(); i++) {
                if (s.length() / 2 == i) {
                    answer = Character.toString(c[i]);
                }
            }
        }

        return answer;
    }
}