




def calculate(strTab):
    result = 0;
    if strTab != int:
        return bool(0)
    for i in range(0, len(strTab)):
        result += int(strTab[i])
    return result


test = calculate(230)
print(test)
