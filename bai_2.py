
def check_hang(_ban_co, i):
    return sum(_ban_co[i]) < 2

def check_cot(_ban_co, j):
    # for line in _ban_co:
    #     if line[j]:
    #         return False

    k = [x[j] for x in _ban_co]
    return sum(k) < 2

def check_cheo(_ban_co, i, j, _i, _j):
    while True:
        i += _i
        j += _j
        if i>=8 or j>=8 or i<0 or j<0:
            break
        if _ban_co[i][j]:
            return False
    return True

def Try(_ban_co):
    for i in range(0, 8):
        if not check_hang(_ban_co, i):
            return False
    for j in range(0,8):
        if not check_cot(_ban_co, j):
            return False
    for i in range(0, 8):
        for j in range(0, 8):
            if (not check_cheo(_ban_co, i, j, 1, 1)) \
                and (not check_cheo(_ban_co, i, j, 1, -1))\
                and (not check_cheo(_ban_co, i, j, -1, 1))\
                and (not check_cheo(_ban_co, i, j, -1, -1)):
                return False
            else:
                return True

def xep_co(__ban_co, i, j):
    print("Buoc", i)
    for line in __ban_co:
        print(line)
    _ban_co = []
    for line in __ban_co:
        _ban_co.append(line[:])

    if i == 8 and j == 8:
        print('ket qua')
        for line in _ban_co:
            print(line)
        return True
    _ban_co[i][j] = 1

    if Try(_ban_co):
        if xep_co(_ban_co, i + 1, j + 1):
            return True
        else:
            return False
    else:
        return False


ban_co = []
for i in range(0, 8):
    ban_co.append([0,0,0,0,0,0,0,0])
xep_co(ban_co,0, 0)
