def solve(input):
    n = len(input)
    r = n - 1
    l = n - 1
    found = False
    while l > -1:
        if input[l] == ' ':
            if not found:
                l -= 1
                continue
            else:
                assert r - l >= 2
                input[r] = '0'
                input[r-1] = '2'
                input[r-2] = '%'
                r -= 3
        else:
            found = True
            input[r] = input[l]
            r -= 1
        l -= 1
    return input

def generate_input():
    return [list("Mr John Smith    "), list(" Hello world    ")]

def main():
    input = generate_input()
    for i, v in enumerate(input):
        print(f"Test {i}: {''.join(solve(v))}")

if __name__ == '__main__':
    main()