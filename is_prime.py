n=int(input('Sayı giriniz: '))
is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
if is_prime:
    print(f"{n} bir asal sayıdır.")
else:
    print(f"{n} bir asal sayıd değildir.")