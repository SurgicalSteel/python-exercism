def latest(scores):
    if len(scores) == 0:
        return None
    index = len(scores)-1
    return scores[index]


def personal_best(scores):
    if len(scores) == 0:
        return None

    return max(scores)

def personal_top_three(scores):
    if len(scores) == 0:
        return None

    scores = sorted(scores, reverse=True)
    maxi = min(len(scores),3)

    return scores[0:maxi]


