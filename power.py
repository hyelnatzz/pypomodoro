def get_power(num):
    pow = 0
    while num >= 10:
        pow += 1
        num //= 10
        print(num)
    return pow

def check_palindrome(num):
    orig_num = num
    pal = 0
    pow = get_power(num)
    while num >= 10:
        rem = num % 10
        num //= 10
        val = rem * 10**pow
        pow -= 1
        pal += val
       
    pal += num
    print(pal)
    return pal == orig_num

print(check_palindrome(100001))