/**
 * LeetCode Problem 0029: Divide Two Integers
 *
 * Problem:
 * Given two integers dividend and divisor, divide two integers without using
 * multiplication, division, and mod operator.
 *
 * Examples:
 * 1. Input: dividend = 10, divisor = 3, Output: 3
 * 2. Input: dividend = 7, divisor = -3, Output: -2
 * 3. Input: dividend = -2147483648, divisor = -1, Output: 2147483647
 */

public class DivideTwoIntegers {

    // Q1: Bit manipulation approach (optimal)
    public static int divide(int dividend, int divisor) {
        final int INT_MAX = Integer.MAX_VALUE;
        final int INT_MIN = Integer.MIN_VALUE;

        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        long quotient = 0;
        long currentDividend = 0;

        for (int i = 31; i >= 0; i--) {
            currentDividend = (currentDividend << 1) | ((dvd >> i) & 1);

            if (currentDividend >= dvs) {
                currentDividend -= dvs;
                quotient |= (1L << i);
            }
        }

        int result = (int) quotient;
        return negative ? -result : result;
    }

    // Q2: Exponential search
    public static int divideExponentialSearch(int dividend, int divisor) {
        final int INT_MAX = Integer.MAX_VALUE;
        final int INT_MIN = Integer.MIN_VALUE;

        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        if (dvd < dvs) {
            return 0;
        }

        long quotient = 0;
        long power = 1;

        while (dvs * power <= dvd) {
            power *= 2;
        }

        power /= 2;

        while (power >= 1) {
            if (dvs * power <= dvd) {
                dvd -= dvs * power;
                quotient += power;
            }
            power /= 2;
        }

        int result = (int) quotient;
        return negative ? -result : result;
    }

    // Q3: Double and subtract approach
    public static int doubleDivide(int dividend, int divisor) {
        final int INT_MAX = Integer.MAX_VALUE;
        final int INT_MIN = Integer.MIN_VALUE;

        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        long quotient = 0;

        while (dvd >= dvs) {
            long tempDivisor = dvs;
            long power = 1;

            while ((tempDivisor << 1) <= dvd) {
                tempDivisor <<= 1;
                power <<= 1;
            }

            dvd -= tempDivisor;
            quotient += power;
        }

        int result = (int) quotient;
        return negative ? -result : result;
    }

    // Q4: Bit shifting with accumulation
    public static int bitShiftDivide(int dividend, int divisor) {
        final int INT_MAX = Integer.MAX_VALUE;
        final int INT_MIN = Integer.MIN_VALUE;

        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }

        boolean negative = (dividend < 0) ^ (divisor < 0);
        long dvd = Math.abs((long) dividend);
        long dvs = Math.abs((long) divisor);

        long quotient = 0;
        int powerOfTwo = 1;

        while ((dvs << powerOfTwo) <= dvd) {
            powerOfTwo++;
        }

        powerOfTwo--;

        for (int i = powerOfTwo; i >= 0; i--) {
            if ((dvs << i) <= dvd) {
                dvd -= (dvs << i);
                quotient += (1L << i);
            }
        }

        int result = (int) quotient;
        return negative ? -result : result;
    }

    public static void main(String[] args) {
        int[][] tests = {
            {10, 3},
            {7, -3},
            {-2147483648, -1},
            {0, 1},
            {2147483647, 1}
        };

        System.out.println("Q1: divide (Bit Manipulation)");
        for (int[] test : tests) {
            System.out.println("  divide(" + test[0] + ", " + test[1] + ") = " +
                divide(test[0], test[1]));
        }

        System.out.println("\nQ2: divide (Exponential Search)");
        System.out.println("  divide(10, 3) = " + divideExponentialSearch(10, 3));

        System.out.println("\nQ3: divide (Double and Subtract)");
        System.out.println("  divide(10, 3) = " + doubleDivide(10, 3));
    }
}
