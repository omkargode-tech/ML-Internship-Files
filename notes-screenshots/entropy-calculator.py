import math

def calculate_probabilities(counts):
    total = sum(counts)
    
    if total == 0:
        return [0] * len(counts)
    
    return [count / total for count in counts]


def entropy(counts):
    probabilities = calculate_probabilities(counts)
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


print(entropy([1,6]))
