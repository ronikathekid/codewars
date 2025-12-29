#Test Comment
def get_users():
    users = [
        {"name": "Ali", "age": 25},
        {"name": "Sara", "age": 30},
        {"name": "Reza"},
        {"name": "Mina", "age": 20},
    ]
    return users


def extract_ages(users):
    ages = []
    for user in users:
        if "age" in user:
            ages.append(user["age"])
    return ages


def calculate_average(ages):
    total = 0
    #for i in range(len(ages) + 1):
    for a in ages:
        total += a
    return total / len(ages)


def print_result(avg):
    if avg > 20:
        print("Average age is high:", avg)
    else:
        print("Average age is low:", avg)


def main():
    users = get_users()
    ages = extract_ages(users)
    avg = calculate_average(ages)
    print_result(avg)

main()
