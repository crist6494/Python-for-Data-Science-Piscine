def all_thing_is_obj(object: any) -> int:
    object_type = str(type(object))
    match object_type:
        case "<class 'list'>":
            print("List : <class 'list'>")
        case "<class 'tuple'>":
            print("Tuple : <class 'tuple'>")
        case "<class 'set'>":
            print("Set : <class 'set'>")
        case "<class 'dict'>":
            print("Dict : <class 'dict'>")
        case "<class 'str'>":
            print("{0} is in the kitchen: <class 'str'>".format(object))
        case _:
            print("Type not found")
    return 42


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
