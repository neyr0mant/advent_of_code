#https://adventofcode.com/2024/day/2
list_data = [[int(j) for j in i.strip("\n ").split()] for i in open("input.txt")]


def get_good_report(report, part=1):
    last_good_diff, len_report = 0, len(report)
    for idx in range(len_report-1):
        cur_num, next_num = report[idx], report[idx + 1]
        diff = next_num - cur_num
        if any([diff > 3, diff < -3, diff == 0, diff > 0 > last_good_diff, diff < 0 < last_good_diff]):
            if part == 1:
                return False
            else:
                if idx == len_report-1:
                    return True
                elif idx == 0:
                    return get_good_report(report[1:], part=1)
                else:
                    new_report_1 = report[:idx-1] + report[idx:]
                    new_report_2 = report[:idx] + report[idx+1:]
                    new_report_3 = report[:idx+1] + report[idx+2:]
                    return any([get_good_report(new_report_1, part=1),
                                get_good_report(new_report_2, part=1),
                                get_good_report(new_report_3, part=1)])
        last_good_diff = diff
    return True


print(f"Решение части 1: {len([i for i in list_data if get_good_report(i)])}")
print(f"Решение части 2: {len([i for i in list_data if get_good_report(i, part=2)])}")








