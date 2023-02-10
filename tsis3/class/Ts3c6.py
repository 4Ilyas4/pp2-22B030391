n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def isprime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True  
pr = list(filter(lambda x: isprime(x), n))
print(pr)
