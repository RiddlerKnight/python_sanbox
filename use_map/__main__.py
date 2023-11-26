def yell(*word):
    '''
    User map function to iterate each word and passing to string uppercase
    function and return list of str
    This is more pythonic way
    '''
    uppercased =  map(str.upper, word)
    print(*uppercased)

def main():
    yell("This", "is", "My", "Map", "Function")

if __name__ == "__main__":
    main()
