def isNullValue(value: any) -> bool:
    if isinstance(value, float) and value != value:
        return True
    null_values = [None, 0, '', False]
    return value in null_values


def NULL_not_found(object: any) -> int:
    if not isNullValue(object):
        print("Type not found")
        return 1

    object_type = str(type(object))
    match object_type:
        case "<class 'NoneType'>":
            print("Nothing: None <class 'NoneType'>")
        case "<class 'float'>":
            print("Cheese: nan <class 'float'>")
        case "<class 'int'>":
            print("Zero: 0 <class 'int'>")
        case "<class 'str'>":
            print("Empty: <class 'str'>")
        case "<class 'bool'>":
            print("Fake: False <class 'bool'>")
    return 0

