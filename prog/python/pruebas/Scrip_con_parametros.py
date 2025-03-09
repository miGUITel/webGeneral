import sys

def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return palindromo(palabra[1:-1])
        else:
            return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(palindromo(sys.argv[1]))
    else:
        print("falta palabra")