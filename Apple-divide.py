import collections

def distribute_apple():
    amount_paid = {'Ram': 50, 'Shyam': 30, 'Rahim': 20}
    total_amount = 100
    # Calculating the ideal proportion for each person
    ideal_proportion = {p: amount / total_amount for p, amount in amount_paid.items()}

    # Taking the inputs
    apples = []
    while True:
        apple_wei = int(input('Enter apple weight in grams (-1 to stop ): \n'))
        if apple_wei == -1:
            break
        apples.append(apple_wei)
    
    # Sorting the apple weight in descending order
    apples.sort(reverse=True)
    total_apple_weight = sum(apples)
    res = {person: [] for person in amount_paid}

    # Actually distributing the apples
    temp_apple_weight = 0
    for apple in apples:
        ideal_diff = float("inf")
        ideal_person = None
        temp_apple_weight += apple
        for person in amount_paid:
            new_proportion = (sum(res[person]) + apple) / temp_apple_weight
            diff = abs(ideal_proportion[person] - new_proportion)
            if diff < ideal_diff:
                ideal_diff = diff
                ideal_person = person
        res[ideal_person].append(apple)
    

    # Printing the result
    for person, apples in res.items():
        print(f"{person}: {', '.join(map(str, apples))} (total weight: {sum(apples)})")

distribute_apple()
