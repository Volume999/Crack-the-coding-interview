class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solve(input):
    head = input
    slow = head 
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.data

def generate_input():
    head = Node('A')
    head.next = Node('B')
    head.next.next = Node('C')
    head.next.next.next = Node('D')
    head.next.next.next.next = Node('E')
    head.next.next.next.next.next = head.next.next
    return [head]

def main():
    input = generate_input()
    for i, v in enumerate(input):
        print(f"Test {i}: {solve(v)}")

if __name__ == '__main__':
    main()