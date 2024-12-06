from pathlib import Path


def do_main(debug_mode=False):
    l = {}
    updates = []
    with open(Path("05/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("05/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    corr_ordered = []
    incorr_ordered = []

    update_index = 0
    for line_index, line in enumerate(lines):
        if line.strip() == "":
            update_index = line_index + 1
            break
        ll, rr = [int(i) for i in line.split("|")]
        if ll not in l:
            l[ll] = []
        l[ll].append(rr)

    for line in lines[update_index:]:
        updates.append([int(i) for i in line.split(",")])

    for update in updates:
        all_ordered = True
        for index, page in enumerate(update):
            if page not in l:
                continue
            for prev_page in update[:index]:
                if prev_page in l[page]:
                    all_ordered = False
                    break
            update_w = update[index + 1 :]
            for next_page in update_w:
                if next_page not in l[page]:
                    all_ordered = False
                    break
            if not all_ordered:
                break
        if all_ordered:
            corr_ordered.append(update)
        else:
            incorr_ordered.append(update)

    for corr in corr_ordered:
        mid_index = len(corr) // 2
        point_sum += corr[mid_index]
    print(point_sum)
    point_sum = 0

    new_l = {}
    for rule, pages in l.items():
        if rule not in new_l:
            new_l[rule] = []
        new_l[rule].extend(pages)
        new_l[rule] = list(set(new_l[rule]))

    incorr_sorted = []
    for update in incorr_ordered:
        corrected_update = update[:]
        for index, page in enumerate(update):
            if page not in l:
                continue
            for index_prev, prev_page in enumerate(corrected_update[:index]):
                if prev_page in new_l[page]:
                    corrected_update.remove(page)
                    corrected_update.insert(index_prev, page)
                    break
        incorr_sorted.append(corrected_update)

    for corrected_update in incorr_sorted:
        mid_index = len(corrected_update) // 2
        point_sum += corrected_update[mid_index]

    print(point_sum)


if __name__ == "__main__":
    do_main(False)
