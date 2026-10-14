def is_cached(n: int) -> bool:
    return id(eval(str(n))) == id(eval(str(n)))

M = None
N = None

var_for_N = 0
var_for_M = -1
while N is None or M is None:
    if N is None and not is_cached(var_for_N):
        N = var_for_N - 1
    if M is None and not is_cached(var_for_M):
        M = var_for_M + 1

    var_for_N += 1
    var_for_M -= 1

print(f"[{M};{N}]")
# [-5;256]