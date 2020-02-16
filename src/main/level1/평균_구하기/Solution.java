package main.level1.평균_구하기;

public class Solution {
    public double solution(int[] arr) {
        double answer = 0;

        for (double item : arr) {
            answer += item;
        }

        answer = answer / arr.length;

        return answer;
    }
}