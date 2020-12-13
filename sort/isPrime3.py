# 素数のリスト
prime_numbers = [.....]


def isPrime(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  m = math.floor(math.sqrt(n))
  for p in prime_numbers:
      if n % p == 0:
        return False
      if p > m:
        # 素数がnの平方根を超えたら終了
        break
  return True
