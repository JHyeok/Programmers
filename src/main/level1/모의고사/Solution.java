package main.level1.모의고사;

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] pattern1 = {1, 2, 3, 4, 5};
        int[] pattern2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] pattern3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int[] cnt = new int[3];

        int pl1 = pattern1.length;
        int pl2 = pattern2.length;
        int pl3 = pattern3.length;

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == pattern1[i % pl1]) {
                cnt[0]++;
            }
            if (answers[i] == pattern2[i % pl2]) {
                cnt[1]++;
            }
            if (answers[i] == pattern3[i % pl3]) {
                cnt[2]++;
            }
        }

        int max = cnt[0];
        for (int i = 0; i < cnt.length; i++) {
            if (max < cnt[i]) {
                max = cnt[i];
            }
        }

        List<Integer> winners = new ArrayList<>();

        for (int i = 0; i < cnt.length; i++) {
            if (max == cnt[i]) {
                winners.add(i);
            }
        }

        int[] answer = {};
        answer = new int[winners.size()];

        for (int i = 0; i < winners.size(); i++) {
            answer[i] = winners.get(i) + 1;
        }

        return answer;
    }
}
