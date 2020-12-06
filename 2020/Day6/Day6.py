groups = [x.split('\n') for x in open("input.txt").read()[:-1].split("\n\n")]

def count_silver(groups):
    votes = 0
    for group in groups:
        votes += len(set("".join(group)))
    return votes

def count_gold(groups):
    votes = 0
    for group in groups:
        all_votes = set(group[0])
        for person in group:
            all_votes = all_votes.intersection(set(person))
        votes += len(all_votes)
    return votes

print("silver:", count_silver(groups))
print("gold:", count_gold(groups))
