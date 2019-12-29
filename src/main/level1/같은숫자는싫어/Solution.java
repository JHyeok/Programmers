package main.level1.같은숫자는싫어;

import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();

        int pValue = -1;
        for (int value : arr) {
            if (value != pValue) {
                list.add(value);
                pValue = value;
            }
        }

        answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
