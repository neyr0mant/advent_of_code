import hashlib


def get_min_count(data_str, count_zero):
    i = 1
    while True:
        md5_hash = hashlib.md5()
        md5_hash.update((data_str + str(i)).encode('utf-8'))
        if md5_hash.hexdigest().startswith(count_zero * "0"):
            return i
        i += 1


print(f"Решение части 1: {get_min_count('iwrupvqb', 5)}")
print(f"Решение части 2: {get_min_count('iwrupvqb', 6)}")
