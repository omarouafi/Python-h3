def solution(n):
    binary_result = ""
    
    while n > 0:
        remainder = n % 2
        binary_result = str(remainder) + binary_result
        n //= 2

    return len(binary_result if binary_result else "0") 