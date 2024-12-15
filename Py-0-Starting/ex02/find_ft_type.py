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
