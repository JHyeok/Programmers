package main.level2.탑;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public int[] solution(int[] heights) {
        int[] answer = new int[heights.length];

        List<Integer> answerList = new ArrayList<Integer>();
        boolean isBottom = true;
        for (int i = heights.length - 1; i >= 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                if (heights[j] > heights[i]) {
                    answerList.add(j + 1);
                    isBottom = false;
                    break;
                }
            }
            if (isBottom) {
                answerList.add(0);
            }
            isBottom = true;
        }

        Collections.reverse(answerList);
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
