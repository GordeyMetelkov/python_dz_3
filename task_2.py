# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list = [1, 2, 2, 3, 1, 4, 5, 5, 5, 6, 7, 8]
res_list = []
for item in set(list):
    if list.count(item) > 1:
        res_list.append(item)
print(res_list)