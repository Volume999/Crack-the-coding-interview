# Three in One: Describe how you could use a single array to implement three stacks.
array_length = 20
array = [None] * array_length

p1 = 0
p2_beg = array_length // 2
p2_end = p2_beg
p3 = array_length - 1

def shift(diff):
    global p2_beg, p2_end
    print("Shift")
    if diff > 0:
        for i in range(p2_end, p2_beg - 1, -1):
            array[i + diff] = array[i]
        p2_beg += diff
        p2_end += diff
    elif diff < 0:
        for i in range(p2_beg, p2_end + 1):
            array[i + diff] = array[i]
        p2_end += diff
        p2_beg += diff
        

def push(stack, value):
    global p1, p2_beg, p2_end, p3
    print(stack, p1, p2_beg, p2_end, p3)
    if p1 == p2_beg - 1 and p2_end + 1 == p3:
        print("Stack is full")
        return
    if stack == 1:
        p1 += 1
        if p1 == p2_beg:
            shift(1)
        array[p1] = value
    elif stack == 2:
        p2_end += 1
        if p2_end == p3:
            shift(-1)
        array[p2_end] = value
    elif stack == 3:
        p3 -= 1
        if p3 == p2_end:
            shift(-1)
        array[p3] = value

def pop(stack):
    global p1, p2_beg, p2_end, p3
    if stack == 1:
        val = array[p1]
        array[p1] = None
        p1 -= 1
        return val
    elif stack == 2:
        val = array[p2_end]
        array[p2_end] = None
        p2_end -= 1
        return val
    elif stack == 3:
        val = array[p3]
        array[p3] = None
        p3 += 1
        return val

def peek(stack):
    global p1, p2_end, p2_beg, p3
    if stack == 1:
        pass
    elif stack == 2:
        pass
    elif stack == 3:
        pass

def is_empty(stack):
    global p1, p2_beg, p2_end, p3
    if stack == 1:
        pass
    elif stack == 2:
        pass
    elif stack == 3:
        pass

def main():
    for i in range(20):
        print("Push")
        push(1, i)
        push(2, i)
        push(3, i)
    for i in range(5):
        print("Pop")
        print(pop(1))


if __name__ == '__main__':
    main()