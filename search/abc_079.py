n = input()
op_cnt = len(n) - 1  # すき間の個数
for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"  # フラグが立っていた箇所を "+" で上書き

    formula = ""
    for p_n, p_o in zip(n, op + [""]):  # 少々モヤッとする
        formula += (p_n + p_o)
    if eval(formula) == 7:
        print(formula + "=7")
        break
