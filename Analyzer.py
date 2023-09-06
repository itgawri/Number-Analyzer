def check_odd_even(number):
  if number%2 == 0:
    return (f'{number} is an even number')
  else:
    return (f'{number} is an odd number')

def get_factors(number):
  factors = []
  iteration_index = 1
  while iteration_index <= number:
    if number%iteration_index == 0:
      factors.append(iteration_index)
    iteration_index += 1
  print(f'The factors of {number} are: {factors}')
  return factors

def check_prime(number, factors):
  if len(factors) == 2:
    return (f'{number} is a prime number')
  else:
    return (f'{number} is not a prime number')

def analyze_number(number):
  print(check_odd_even(number))
  factors = get_factors(number)
  print(check_prime(number, factors))

analyze_number(15)

# PL----------------------------------------------------------------

def sprawdz_parzysta_nieparzysta(liczba):
  if liczba % 2 == 0:
    return(f'{liczba} jest liczbą parzystą')
  else:
    return(f'{liczba} jest liczbą nieparzystą')

def znajdz_dzielniki(liczba):
  dzielniki = []
  indeks_iteracji = 1
  while indeks_iteracji <= liczba:
    if liczba % indeks_iteracji == 0:
      dzielniki.append(indeks_iteracji)
    indeks_iteracji += 1
  print(f'Dzielniki liczby {liczba} to: {dzielniki}')
  return dzielniki

def sprawdz_pierwsza(liczba, dzielniki):
  if len(dzielniki) == 2:
    return(f'{liczba} jest liczbą pierwszą')
  else:
    return(f'{liczba} nie jest liczbą pierwszą')

def analizuj_liczbe(liczba):
  print(sprawdz_parzysta_nieparzysta(liczba))
  dzielniki = znajdz_dzielniki(liczba)
  print(sprawdz_pierwsza(liczba, dzielniki))

analizuj_liczbe(15)

