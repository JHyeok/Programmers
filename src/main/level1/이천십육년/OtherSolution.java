package main.level1.이천십육년;

import java.util.*;

class OtherSolution {
    public String getDayName(int month, int day) {
        Calendar cal = new Calendar.Builder().setCalendarType("iso8601")
                .setDate(2016, month - 1, day).build();
        return cal.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.SHORT, new Locale("ko-KR")).toUpperCase();
    }

    public static void main(String[] args) {
        OtherSolution test = new OtherSolution();
        int a = 5, b = 24;
        System.out.println(test.getDayName(a, b));
    }
}
