# Number-Analyzer
The "Number Analyzer" project aims to analyze a given number from various perspectives, such as parity (even or odd), prime factors, and the list of factors. Below, we present the project's code and its description.

The project consists of three functions:

check_odd_even(number): This function checks whether the given number is even or odd. If the number is even, it displays that it is even; otherwise, it informs that it is odd.

get_factors(number): This function calculates all the factors of the given number. It uses a while loop to iterate from 1 to the given number and adds all the numbers by which the given number is divisible to a list of factors. It then displays the list of factors and returns it as the result.

check_prime(number, factors): This function checks whether the given number is a prime number. If the number has exactly two factors (1 and itself), it is considered a prime number. Otherwise, it is considered a composite number.

The final function, analyze_number(number), calls all three of the above functions to analyze the given number. First, it checks whether the number is even or odd, then it calculates and displays its factors, and finally, it checks whether it is a prime number.

Calling the analyze_number(15) function at the end of the code example will display the analysis result for the number 15, including information about its parity, factors, and whether it is a prime number.
