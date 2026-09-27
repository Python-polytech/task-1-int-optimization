flag_pos = False
flag_neg = False

M = None
N = None

var_for_N = 0
var_for_M = -1
while not flag_pos or not flag_neg:
    x_N, y_N = int(str(var_for_N)), int(str(var_for_N))
    x_M, y_M = int(str(var_for_M)), int(str(var_for_M))

    if N is not None:
        pass
    elif id(x_N) != id(y_N):
        flag_pos = True
        N = x_N - 1

    if M is not None:
        pass
    elif id(x_M) != id(y_M):
        flag_neg = True
        M = x_M + 1

    var_for_N += 1
    var_for_M -= 1

print(f"[{M};{N}]")
# [-5;256]