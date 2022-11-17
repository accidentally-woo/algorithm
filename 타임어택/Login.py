def solution(id_pw, db):
    for row in db:
        if row[0] == id_pw[0]:
            if row[1] == id_pw[1]:
                return "login"
            return "wrong pw"
    return "fail"


def solution2(id_pw, db):
    for id, password in db:
        if id == id_pw[0]:
            if password == id_pw[1]:
                return "login"
            return "wrong pw"
    return "fail"


print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))

print(solution2(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution2(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution2(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))
