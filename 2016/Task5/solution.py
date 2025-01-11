import hashlib
from functions import execution_time

@execution_time
def get_solve(data_str, count_zero, part =1):
    i = 0
    password = "" if part ==1 else "."*8
    while True:
        if len(password) == 8 and part == 1:
            break
        if len([i for i in password if i != "."]) == 8:
            break
        md5_hash = hashlib.md5()
        str_in = data_str + str(i)
        md5_hash.update(str_in.encode('utf-8'))
        hex_str = md5_hash.hexdigest()
        if part == 1:
            if hex_str.startswith(count_zero * "0"):
                password += hex_str[5]
        else:
            position = hex_str[5]
            if position.isdigit():
                int_p = int(position)
                if 0 <= int_p < 8:
                    if hex_str.startswith(count_zero * "0"):
                        if password[int_p] == ".":
                            password = password[:int_p] + hex_str[6] + password[int_p +1:]
        i += 1
    return password

print(f"Решение части 1: {get_solve('wtnhxymk', 5)}")
print(f"Решение части 2: {get_solve('wtnhxymk', 5, part=2)}")
