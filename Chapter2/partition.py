class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solve(input):
    head, partition = input
    lower, higher = Node(None), Node(None)
    cur = head
    lhead, hhead = lower, higher
    while cur:
        if cur.data < partition:
            lhead.next = cur
            lhead = lhead.next
        else:
            hhead.next = cur
            hhead = hhead.next
        cur = cur.next
    lhead.next = higher.next
    hhead.next = None
    return lower.next

def generate_input():
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(1)
    return [(head, 5)]

def main():
    input = generate_input()
    for i, v in enumerate(input):
        res = solve(v)
        print(f"Test {i}:")
        while res:
            print(res.data)
            res = res.next

if __name__ == '__main__':
    main()