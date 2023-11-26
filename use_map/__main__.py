def yell(*words):
    '''
    User map function to iterate each word and passing to string uppercase
    function and return list of str
    This is more pythonic way
    '''
    uppercased =  map(str.upper, words)
    print(*uppercased)

def yell_v2(*words):
    uppercased = [word.upper() for word in words ]
    print(*uppercased)

def main():
    yell("This", "is", "My", "Map", "Function")
    yell_v2("This", "is", "My", "Map", "Function V2")

if __name__ == "__main__":
    main()
