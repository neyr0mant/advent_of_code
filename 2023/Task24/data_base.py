# LinkedList или связный список – это структура данных,
# которая в общем случае обеспечивает возможность создать направленную очередь из элементов.
# Каждый элемент такого списка считается узлом.
# В узле указаны его значение и ссылки на предыдущий и/или последующий узлы.
# В линейном связном списке последний элемент списка указывает на NULL
# Разновидностью связных списков является кольцевой (или замкнутый) список.
# Последний элемент кольцевого списка указыавет на первый


# Реализация однонаправленного связного списка с указателем на предыдущий элемент
class LinkedList:

    def __init__(self, value, prev):
        self.value = value
        self.prev = prev

# Задача: написать метод, проверяющий связный список на закольцованность/замкнутость
# В параметры метода передается один любой элемент связного списка
# Метод должен возвращать результат выполнения True/False

def generate_list_item(count, circle=0):
    list_item = []
    for i in range(count):
        prev = list_item[-1] if list_item else None
        elem = LinkedList(i, prev)
        list_item.append(elem)
    if circle:
        list_item[0].prev = list_item[circle-1]
    return list_item


list_id_all = []
list_path_iter = []
def assert_circle(item):
    global list_path_iter
    global list_id_all
    prev_item, cur_id = item.prev, id(item)
    msg_path = f"Список пройденных ID --> ID_PREV:\n" + "".join(list_path_iter)
    if not prev_item:
        print(msg_path + f"{cur_id} --> None")
        list_id_all, list_path_iter = [], []
        return False
    next_id = id(prev_item)
    if cur_id in list_id_all:
        assert cur_id == list_id_all[0], f"Список замкнутый но не в полное кольцо!\n{msg_path}"
        print(msg_path, end="")
        list_id_all, list_path_iter = [], []
        return True
    list_id_all.append(cur_id)
    path_iter = f"{cur_id} --> {next_id}\n"
    list_path_iter.append(path_iter)
    return assert_circle(prev_item)

list_item_line = generate_list_item(10)
list_item_circle = generate_list_item(10, circle=5)

print('Список замкнутый' if assert_circle(list_item_line[5]) else 'Список линейный')
print('Список замкнутый' if assert_circle(list_item_circle[4]) else 'Список линейный')


def count_primes_less_than(n):
    list_prime = [1,2]
    for i in range(3, n+1):
        is_prime = True
        for j in list_prime[1:]:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            list_prime.append(i)
    return list_prime
import time
import numpy
def get_primes_numpy(n):
    sieve = numpy.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*len(sieve[i*i::2*i])
    return len(numpy.r_[2, 2 * numpy.nonzero(sieve)[0][1::] + 1])
time_s = time.time()
print(get_primes_numpy(10**8))
time_f = time.time()
print(time_f-time_s)
