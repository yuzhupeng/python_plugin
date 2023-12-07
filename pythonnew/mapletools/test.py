def has_expected_potential_lines(OCR_result, potential, lines: int, True3: bool, above_160: bool):
    count = 0
    temp_sum = 0

    for potential_line in OCR_result:
        if potential in ["STR", "DEX", "INT", "LUK"] and (potential in potential_line or "All Stats" in potential_line):
            if True3:
                value = int(''.join(filter(str.isdigit, potential_line)))
                if above_160 and value in [13, 10, 7] or not above_160 and value in [12, 9, 6]:
                    temp_sum += value
            else:
                count += 1
        elif potential == "ATT" and potential in potential_line and not potential_line.startswith("Magic ATT:") and not potential_line.startswith("ATT: +32"):
            count += 1
        
        elif potential == "Magic ATT:" and potential in potential_line and not potential_line.startswith("Magic ATT: +32"):
            count += 1
        #for meso, drop rate etc...
        elif potential not in ["STR", "DEX", "INT", "LUK", "ATT", "Magic ATT:"] and potential in potential_line:
            count += 1

    if True3:
        return temp_sum >= (33 if above_160 else 30)
    else:
        return count >= lines


test_result = ['STR: 12%', 'INT: 12%', 'All Stats: 6%']
test_desire_potential = 'STR'
test_line = 2
test_True3 = False
above_160 = False
print(has_expected_potential_lines(test_result, test_desire_potential, test_line, test_True3, above_160))
