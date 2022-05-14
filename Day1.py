

def calculate():
    raw_lines = read_input()
    lines = clean_input(raw_lines)
    increases = count_increase(lines)

    return increases


def count_increase_window(lines):
    return


def calculate_window():
    raw_lines = read_input()
    lines = clean_input(raw_lines)
    increases = count_increase_window(lines)

    return increases


def count_increase(lines):
    length = len(lines)
    index = 0
    increases = 0

    while index < length:
        previous = lines[index - 1]
        current = lines[index]
        index += 1

        if previous < current:
            increases += 1

    return increases


def clean_input(raw_lines):
    lines = []
    for line in raw_lines:
        int_line = int(line)
        lines.append(int_line)
    return lines


def read_input():
    with open('Day1.txt') as f:
        raw_lines = f.readlines()
    return raw_lines


answer = calculate()

print(answer)


def test_increase():
    lines = [5, 6, 3, 8]
    increases = count_increase(lines)

    if increases != 2:
        print("broke!")
    else:
        print("ok")


def test_window():
    return


test_increase()
test_window()
