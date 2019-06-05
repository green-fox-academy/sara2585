def seperate_char(str3):
    if len(str3) == 1:
        return str3
    else:
        return str3[0] + '*' + seperate_char(str3[1:])


