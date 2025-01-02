import hashlib
def get_min_count(data_str, part =1):
    i = 1
    count_zero = 5*"0" if part == 1 else 6*"0"
    while True:
        md5_hash = hashlib.md5()
        hash_str = data_str + str(i)
        md5_hash.update(hash_str.encode('utf-8'))
        hex_digest = md5_hash.hexdigest()
        if hex_digest.startswith(count_zero):
            return i
        i += 1
print(f"Решение части 1: {get_min_count('iwrupvqb')}")
print(f"Решение части 2: {get_min_count('iwrupvqb', part=2)}")








