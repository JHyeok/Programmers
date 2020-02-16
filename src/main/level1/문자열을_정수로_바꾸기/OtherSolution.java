package main.level1.문자열을_정수로_바꾸기;

class OtherSolution {
    public int getStrToInt(String str) {
        boolean Sign = true;
        int result = 0;

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == '-')
                Sign = false;
            else if (ch != '+')
                result = result * 10 + (ch - '0');
        }
        return Sign ? 1 : -1 * result;
    }

    //아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String args[]) {
        OtherSolution strToInt = new OtherSolution();
        System.out.println(strToInt.getStrToInt("-1234"));
    }
}
