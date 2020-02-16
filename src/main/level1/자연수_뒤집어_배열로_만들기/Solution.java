package main.level1.자연수_뒤집어_배열로_만들기;

import java.util.*;

public class Solution {
    public int[] solution(long n) {
        String str = String.valueOf(n);
        String[] strArray = str.split("");

        int[] answer = new int[strArray.length];
        int j = 0;
        for (int i = strArray.length - 1; i >= 0; i--) {
            answer[j] = Integer.parseInt(strArray[i]);
            j++;
        }

        return answer;
    }
}