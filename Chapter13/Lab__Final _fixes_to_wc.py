import sys

def count_bytes(file):
    with open(file, 'rb') as f:
        return len(f.read())

def count_chars(file):
    with open(file, 'r') as f:
        return len(f.read())

def process_file(file, option):
    if option == '-c':
        return count_bytes(file)
    elif option == '-m':
        return count_chars(file)
    else:
        print("Invalid option")
        sys.exit(1)

def process_stdin(option):
    if option == '-c':
        return len(sys.stdin.buffer.read())
    elif option == '-m':
        return len(sys.stdin.read())
    else:
        print("Invalid option")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        option = sys.argv
        file = sys.argv
        print(process_file(file, option))
    elif len(sys.argv) == 2:
        option = sys.argv
        print(process_stdin(option))
    else:
        print("Usage: wc [-c|-m] [file]")
        sys.exit(1)