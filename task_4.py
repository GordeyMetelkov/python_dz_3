# Создайте словарь со списком вещей для похода в качестве ключа и их
# массой в качестве значения. Определите какие вещи влезут в рюкзак передав
# его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things = {
    "Сменная одежда": 2,
    "Палатка": 3,
    "Посуда": 2,
    "Еда": 2,
    "Веревки": 1,
    "Аптечка": 1,
    "Спальник": 2,
}
MAX_WEIGHT = 10
backpack = []
variations = []
actual_weight = 0
def fill_packback(actual_weight, backpack,variations, things):
    for key in things:
        if key not in backpack and actual_weight + things[key] <= MAX_WEIGHT:
            backpack.append(key)
            actual_weight += things[key]
    variations.append((backpack, actual_weight))
fill_packback(actual_weight, backpack,variations, things)
print(variations)
# Код ниже - попытка сделать вариации, но не получается
# def change_thing(actual_weight, backpack,variations, things):
#     for key in things:
#         change_thing = backpack[0]
#         if (key not in backpack
#                 and key != change_thing
#                 and actual_weight - things[change_thing] + things[key] <= MAX_WEIGHT):
#             backpack.pop(0)
#             actual_weight -= things[change_thing]
#             backpack.append(key)
#             actual_weight += things[key]
#             if actual_weight < MAX_WEIGHT:
#                 fill_packback(actual_weight, backpack,variations, things)
#             else:
#                 variations.append((backpack, actual_weight))
