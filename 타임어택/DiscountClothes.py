def solution(price):
    if price >= 500_000:  # 50만원 이상 20% 할인
        return int(price * 0.8)

    if price >= 300_000:  # 30만원 이상 10% 할인
        return int(price * 0.9)

    if price >= 100_000:  # 10만원 이상 5% 할인
        return int(price * 0.95)

    return price  # 할인 조건 없을 때
