# 全探索で解けそうだが範囲を考えないといけない問題
# 変数が複数ある場合はいくつかを固定してその取りうる範囲を考える

# pypyで提出(cpythonだとTLEになる)

# 入力の受け取り
N = int(input())

# 答えのカウント
ans = 0

# 初期値
A = 1
# A≤(Nの三乗根)⇔A^3≤Nの間
while A**3 <= N:
    # 初期値
    B = A
    # B≤√(N/A)⇔A*B^2≤Nの間
    while A * B**2 <= N:
        # ありうるCの個数=(N/AB)の切り捨て-B+1
        ans += int(N / (A * B)) - B + 1
        # 次のBへ
        B += 1
    # 次のAへ
    A += 1

# 答えの出力
print(ans)
