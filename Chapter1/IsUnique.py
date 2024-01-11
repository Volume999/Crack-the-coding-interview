def solve_ht(input):
    ht = {}
    for i in input:
        if i in ht:
            return False
        ht[i] = 1
    return True

def solve_sort(input):
    input = sorted(input)
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            return False
    return True

def solve(input):
    return solve_sort(input)
    
def generate_input():
    return ["", "a", "abc", "aa", "abca", "abcb"]

def main():
    print("Hello")
    input = generate_input()
    for i, v in enumerate(input):
        print(f"Test {i}: {solve(v)}")

if __name__ == '__main__':
    main()