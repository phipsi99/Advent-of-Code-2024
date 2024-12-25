from collections import defaultdict
from pathlib import Path

def calc(starting_secret, count):
    mod_val = 16777216
    secrets = [starting_secret]
    for _ in range(count):
        secret = secrets[-1]
        secret = (secret ^ (secret * 64)) % mod_val
        secret = (secret ^ (secret // 32)) % mod_val
        secret = (secret ^ (secret * 2048)) % mod_val
        secrets.append(secret)
    return [s % 10 for s in secrets], secrets[-1]

def find_best_sequence(starting_secrets, num_prices):
    all_sequences = defaultdict(int)
    max_b = 0

    for starting_secret in starting_secrets:
        prices, _ = calc(starting_secret, num_prices)
        changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        
        sequences = defaultdict(int)
        for i in range(len(changes) - 3):
            sequence = tuple(changes[i:i+4])
            if sequence not in sequences:
                sequences[sequence] = prices[i+4]
        for sequence, price in sequences.items():
            all_sequences[sequence] += price

    for sequence, b in all_sequences.items():
        if b > max_b:
            max_b = b

    return max_b

def do_main(debug_mode=False):
    with open(Path('22/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('22/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    r = []

    for line_index, line in enumerate(lines):
        r.append(int(line))

    for key in r:
        _, key_a = calc(key, 2000)
        point_sum += key_a
    print(point_sum)
    
    max_bananas = find_best_sequence(r, 2000)
    print(max_bananas)
if __name__ == '__main__':
    do_main(False)