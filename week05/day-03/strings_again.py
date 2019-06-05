def remove_x(str2):
    if str2 == '':
        return ''
    elif str2[0] == 'x':
        return ''+ remove_x(str2[1:])
    else:
        return str2[0] + remove_x(str2[1:])