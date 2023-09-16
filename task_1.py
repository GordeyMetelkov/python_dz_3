# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей
hike = {
    "Саша": ("вилка", "ложка", "топор"),
    "Маша": ("вилка", "палатка", "ложка", "каша", "веревка"),
    "Олег": ("ложка", "каша", "матрас", "спички")
}

all_things_set = set()
for value in hike.values():
    for item in value:
        all_things_set.add(item)
def pop_things(things_set, hike_dict):
    for value in hike_dict.values():
        things_set = things_set & set(value)
    print(things_set)

def uniq_things(hike_dict):
    uniq_set = set()
    not_uniq_set = set()
    for value in hike_dict.values():
        for item in value:
            if item in uniq_set or item in not_uniq_set:
                uniq_set.discard(item)
                not_uniq_set.add(item)
            else:
                uniq_set.add(item)
    print(uniq_set)
def one_thing(hike_dict):
    things = []
    res_set = []
    for value in hike_dict.values():
        for item in value:
            things.append(item)
    for item in set(things):
        if things.count(item) == len(hike_dict) - 1:
            res_set.append(item)
    for i in range(len(res_set)):
        for key in hike_dict:
            if res_set[i] not in hike_dict[key]:
                print(f"{res_set[i]} есть у всех, кроме {key}")

pop_things(all_things_set, hike)
uniq_things(hike)
one_thing(hike)