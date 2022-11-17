def solution(order):
    match = ["3", "6", "9"]
    count = 0
    for o in str(order):
        if o in match:
            count += 1
    return count


print(solution(29423))
print(solution(369))
print(solution(121143))
