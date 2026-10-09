def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
def secend_digit_sum(m):
   sum2 = digit_sum(m)
   sum2 = digit_sum(sum2)
   return sum2
print(secend_digit_sum(567))  