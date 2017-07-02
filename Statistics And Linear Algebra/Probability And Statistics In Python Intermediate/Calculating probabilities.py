## Calculating The Probability Of One Combination

prob_combination_3 = None

prob_combination_3 = .7 * .7 * .7 *.3 *.3


## Function To Calculate The Probability Of A Single Combination

p = .6
q = .4

def find_combination_probability(N, k, p, q):
    # Take p to the power k, and get the first term.
    term_1 = p ** k
    # Take q to the power N-k, and get the second term.
    term_2 = q ** (N-k)
    # Multiply the terms out.
    return term_1 * term_2

prob_8 = find_outcome_combinations(10, 8) * find_combination_probability(10, 8, p, q)

prob_9 = find_outcome_combinations(10, 9) * find_combination_probability(10, 9, p, q)


## END
