from typing import List


def get_result(code: List[int], noun: int, verb: int):
    intcode = code.copy()
    intcode[1] = noun
    intcode[2] = verb

    pos = 0
    while True:
        if intcode[pos] == 1:
            intcode[intcode[pos + 3]] = (
                intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
            )
        elif intcode[pos] == 2:
            intcode[intcode[pos + 3]] = (
                intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
            )
        elif intcode[pos] == 99:
            break
        else:
            print(f"ERROR, code: {intcode[pos]}")
            break
        pos += 4
    return intcode[0]
