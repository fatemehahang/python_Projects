from functools import reduce

lesson_list = [
    {"name":"math", "unit":3, "teacher":"yalda"},
    {"name":"math", "unit":3, "teacher":"mona"},
    {"name":"python", "unit":3, "teacher":"fatemeh"},
    {"name":"python", "unit":3, "teacher":"alireza"},
    {"name":"python", "unit":3, "teacher":"reza"},
    {"name":"geo", "unit":2, "teacher":"erfan"},
    {"name":"geo", "unit":2, "teacher":"ali"},
    {"name":"geo", "unit":2, "teacher":"ida"},
    {"name":"c++", "unit":2, "teacher":"reza"},
]

def teacher(names):
    return names["teacher"]
result = sorted(lesson_list, key=teacher)
print(result)

def total_unit(unit, teacher):
    return unit + teacher["unit"]
unit = reduce(total_unit, lesson_list, 0)

for lesson in lesson_list:
    print(lesson["teacher"], lesson["unit"])

print("-" * 30)
print(unit)