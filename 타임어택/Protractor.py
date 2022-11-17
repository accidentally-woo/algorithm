def solution(angle):
    if angle >= 180:
        return 4

    if angle > 90:
        return 3

    if angle == 90:
        return 2

    if angle < 90:
        return 1


print(solution(70))
print(solution(91))
print(solution(180))