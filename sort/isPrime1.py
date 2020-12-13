import math

def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    # ２ではない偶数は素数ではない
    return False
  
  # nの半分まで計算する範囲を絞る
  m = math.floor(n / 2) + 1
  for p in range(3, m, 2): # 奇数だけ計算する
      if n % p == 0:
        return False
  return True
