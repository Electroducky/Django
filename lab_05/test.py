# data = {"name": "ИТМО",
#         "address": {
#             "streetAddress": "Kroverksky pr. 49",
#             "city": "Санкт-Петербург",
#             "postalCode": 197101,
#         },
#         "head": {},
#         "unit": {
#             "administrative":
#                 {"head" : {}}
#         }
#         }
#
# def add_person(d, key, position="employees"):
#         d[key] = {"name": 1, "surname": 2, "patronymic": 3}
#
# add_person(data["unit"]["administrative"], "head")
# print(data)
#
#
# def walk(node):
#     for key, item in node.items():
#         if item is dict:
#             walk(item)
#         else:
#             node["head"] = 1
#
# a = {"a": 1}
# a["b"] = 2
# print(a)data = {"name": "ИТМО",
#         "address": {
#             "streetAddress": "Kroverksky pr. 49",
#             "city": "Санкт-Петербург",
#             "postalCode": 197101,
#         },
#         "head": {},
#         "unit": {
#             "administrative":
#                 {"head" : {}}
#         }
#         }
#
# def add_person(d, key, position="employees"):
#         d[key] = {"name": 1, "surname": 2, "patronymic": 3}
#
# add_person(data["unit"]["administrative"], "head")
# print(data)
#
#
# def walk(node):
#     for key, item in node.items():
#         if item is dict:
#             walk(item)
#         else:
#             node["head"] = 1
#
# a = {"a": 1}
# a["b"] = 2
# print(a)

a = list((map(str, range(1, 10))))
print(a)