from tabulate import tabulate
from random import shuffle

reviewers = ["Luca", "Dyllan", "Max", "Milan", "Jordy"]


def checkResults(_round1, _round2):
    for i in range(len(reviewers)):
        rv = reviewers[i]
        r1 = _round1[i]
        r2 = _round2[i]

        if rv is r1 or r1 is r2 or rv is r2:
            return False

    return True


if __name__ == '__main__':
    data = []
    round1 = reviewers.copy()
    round2 = reviewers.copy()

    while not checkResults(round1, round2):
        shuffle(round1)
        shuffle(round2)

    for i in range(len(reviewers)):
        rv = reviewers[i]
        r1 = round1[i]
        r2 = round2[i]
        data.append([rv, r1, r2])

    print(tabulate(data, headers=["Naam", "Reviewer 1", "Reviewer 2"]))
