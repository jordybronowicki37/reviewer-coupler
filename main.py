from tabulate import tabulate
from random import shuffle


def checkResults():
    for i in range(len(reviewers)):
        line = [reviewers[i]]

        # Add the relevant reviewers for each person
        for j in range(amountOfReviews):
            line.append(rounds[j][i])

        # Return false if all the items in the list are not unique
        if len(set(line)) != len(line):
            return False
    return True


if __name__ == '__main__':
    reviewers = input("Name all of the reviewers separated by a ',': ").split(",")
    amountOfReviews = int(input("How many reviews does everyone get? "))

    if len(reviewers) < 2:
        raise Exception("Not enough reviewers were given! The minimum is 2.")
    if amountOfReviews <= 0:
        raise Exception("The amount of reviews must me higher than 0!")
    if len(reviewers) <= amountOfReviews:
        raise Exception("It's not possible to give this many reviews given the amount of reviewers!")

    rounds = [reviewers.copy() for i in range(amountOfReviews)]

    # Keep shuffling until a solution is found
    while not checkResults():
        for r in rounds:
            shuffle(r)

    # Generate table data
    tableData = []
    for i in range(len(reviewers)):
        tableLine = [reviewers[i]]
        for j in range(amountOfReviews):
            tableLine.append(rounds[j][i])
        tableData.append(tableLine)

    headers = [f"Reviewer #{r+1}" for r in range(amountOfReviews)]
    headers.insert(0, "Name")
    print(tabulate(tableData, headers=headers))
