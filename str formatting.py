def print_formatted(number):
    for i in range (1, number + 1 ):
        hexa = str( hex(i) )[2:]
        octa = str( oct(i) )[2:]
        bina = str( bin(i) )[2:]
        deca = str( i )
        width = len(str( bin(number) )[2:])
        print(f"{deca.rjust(width)} {octa.rjust(width)} {hexa.rjust(width)} {bina.rjust(width)}")
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)