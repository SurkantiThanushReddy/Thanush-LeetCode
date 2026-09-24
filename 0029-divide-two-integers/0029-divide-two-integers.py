class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        sign = 1

        if dividend < 0:
            dividend = -dividend
            sign = -sign

        if divisor < 0:
            divisor = -divisor
            sign = -sign

        count = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            count = count + multiple

        if sign == -1:
            return -count

        return count