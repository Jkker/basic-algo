from doubly_linked_list import DoublyLinkedList


def exp_eval(op, x, y):
    if op == '+':
        res = x + y
    elif op == '—':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y
    else:
        raise Exception("Illegal Operator: ", op)
    print('Eval: ', x, op, y, '=', res)
    return res


def stack_eval(stack):
    x = stack.pop()
    if isinstance(x, int):
        return x
    else:
        return exp_eval(x, stack_eval(stack), stack_eval(stack))


# Create global variable num_stack for temporary storage
num_stack = []


def stack_eval_reversed(L):
    global num_stack
    while L:  # L is not empty
        x = L.pop()
        if isinstance(x, int):
            num_stack.append(x)
        else:
            # Pop the two immediate numbers to perform an eval
            num_stack.append(
                exp_eval(x, num_stack.pop(), num_stack.pop()))
    return num_stack.pop()


def stack_eval_reversed_2(L):
    while L.head.next:
        x = L.pop_head().val
        # Check if the next two elements are not numbers (integers)
        if not isinstance(L.head.val, int) \
                or not isinstance(L.head.next.val, int):
            L.add_tail(x)
        else:
            # Evaluate the triplet and append its result to the back
            L.add_tail(exp_eval(x, L.pop_head().val, L.pop_head().val))
    return L.pop_head()


# Eval:  9 * 7 = 63
# Eval:  63 — 4 = 59
# Eval:  2 — 6 = -4
# Eval:  -4 + 3 = -1
# Eval:  -1 * 59 = -59
# Eval:  -59 + 3 = -56
if __name__ == '__main__':
    stack = ['+', '*', '+', '—', 2, 6, 3, '—', '*', 9, 7, 4, 3]
    # stack = ['+', 9, '*', 2, 6]
    l = DoublyLinkedList()
    for i in stack:
        l.add_tail(i)
    # print(stack_eval_reversed(stack))
    l.displayforward()
    print(stack_eval_reversed_2(l).val)
