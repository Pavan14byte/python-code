import sys

def main():
    text = sys.argv[1]
    lst = text.split(' ')
    for word in lst:
        print(word)

if __name__ == "__main__":
    main()