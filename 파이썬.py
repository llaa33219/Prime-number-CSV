import csv
import math

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 범위별로 소수를 찾고 CSV 파일에 저장하는 함수
def generate_and_save_primes(start, end, step, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for block_start in range(start, end, step):
            block_end = min(block_start + step, end)
            primes = [n for n in range(block_start, block_end) if is_prime(n)]
            for prime in primes:
                writer.writerow([prime])

# 파라미터 설정
start = 2  # 시작 숫자
end = 10000000000  # 끝 숫자 (10억)
step = 20000000  # 한 번에 처리할 범위의 크기 (1천만)
filename = 'primes_up_to_1billion.csv'  # 결과를 저장할 파일 이름

# 소수 생성 및 저장 실행
generate_and_save_primes(start, end, step, filename)
