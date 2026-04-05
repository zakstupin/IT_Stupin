# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, splitter = ','):
    g1 = group1.split(splitter)
    g2 = group2.split(splitter)
    result = []
    for a in range(len(g1)):
        for b in range(len(g2)):
            if g1[a]==g2[b]:
                result.append(g1[a])
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, splitter = '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
