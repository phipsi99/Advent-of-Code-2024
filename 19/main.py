from pathlib import Path


def count_combinations(patterns, curr_design, memo):
    if curr_design in memo:
        return memo[curr_design]
    if len(curr_design) == 0:
        return 1
    total_count = 0
    for p in patterns:
        if curr_design.startswith(p):
            total_count += count_combinations(patterns, curr_design[len(p):], memo)
    memo[curr_design] = total_count
    return total_count


# this is ai gen after solution to understand dp
def count_combinations_dp(patterns, design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to match an empty design

    for i in range(1, n + 1):
        for p in patterns:
            if i >= len(p) and design[i - len(p):i] == p:
                dp[i] += dp[i - len(p)]
    return dp[n]


def do_main(debug_mode=False):
    with open(Path('19/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('19/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    patterns = set(lines[0].split(", "))
    todo = lines[2:]


    point_sum = 0
    point_sum2 = 0
    for t in todo:
        comb = count_combinations(patterns, t, {})
        if comb > 0:
            point_sum += 1
        point_sum2 += comb
    print(point_sum)
    print(point_sum2)


if __name__ == '__main__':
    do_main(False)