def convert_x(str1):
    if str1 == '':
        return ''
    elif str1[0] == 'x':
        return 'y' + convert_x(str1[1:])
    else:
        return str1[0] + convert_x(str1[1:])
        