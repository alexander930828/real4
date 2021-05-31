n, m = map(int, input().split())
result = 0

while True:
    # (N==K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//m) * m # 만약 target 이 1이라면 마지막 1이 되었을때 result에 1이 더해지게 된다.
    result += (n-target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < m:
        break
    # K로 나누기
    n //= m
    result += 1

# 마지막 남은 수에 대하여 1씩 빼기
# result += (n-1)
print(result)