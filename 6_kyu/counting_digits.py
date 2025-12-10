def count_digits(num, rounds):
    num = str(num)
    for _ in range(rounds):
        result = []
        see = set()
        for n in num:
            if n not in see:
                see.add(n)
                count = num.count(n)
                result.append(str(count) + n)
        num = "".join(result)
    return [int(i) for i in result]
