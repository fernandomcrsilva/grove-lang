# FizzBuzz de 1 a 15
HESOYAM i = 1 ×
KANGAROO L1 i <= 15 R1 △
    TURNUPTHEHEAT L1 i % 15 == 0 R1 △
        HELLOLADIES "FizzBuzz" ×
    ○ BRINGITON L1 i % 3 == 0 R1 △
        HELLOLADIES "Fizz" ×
    ○ BRINGITON L1 i % 5 == 0 R1 △
        HELLOLADIES "Buzz" ×
    ○ TURNDOWNTHEHEAT △
        HELLOLADIES i ×
    ○
    i = i + 1 ×
○
