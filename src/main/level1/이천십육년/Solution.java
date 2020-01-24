package main.level1.이천십육년;

class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int totalData = 0;
        int dayOfMonth = 0;
        String[] week = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};

        for (int i = 1; i < a; i++) {
            if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12)
                dayOfMonth = 31;
            else if (i == 2)
                dayOfMonth = 29;
            else
                dayOfMonth = 30;

            totalData += dayOfMonth;
        }

        totalData += b;
        answer = week[(totalData) % 7];

        return answer;
    }
}
