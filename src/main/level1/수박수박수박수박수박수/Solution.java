package main.level1.수박수박수박수박수박수;

public class Solution {
    public String solution(int n) {
        String[] pattern = {"수", "박"};

        StringBuffer sf = new StringBuffer();
        for (int i = 0; i < n; i++) {
            sf.append(pattern[i % 2]);
        }

        return sf.toString();
    }
}
