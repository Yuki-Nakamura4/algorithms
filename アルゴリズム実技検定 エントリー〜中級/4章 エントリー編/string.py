"""与えられた文字列中に最も多く出現するアルファベット小文字を1つ出力する。"""

from collections import Counter  # 文字の出現回数を数えるための便利なクラスß
from string import ascii_lowercase  # アルファベットの小文字一覧

S = input().lower()
cnt = Counter(S)
# Counterオブジェクトは辞書のように使える
# たとえばcnt['a']は文字列S中に出現する'a'の回数を表す
# もしCounterを使わない場合、以下のように実装する必要がある
# cnt = {}
# for ch in S:
#     if ch in cnt:
#         cnt[ch] += 1
#     else:
#         cnt[ch] = 1

mx = max(
    cnt.get(ch, 0) for ch in ascii_lowercase  # その文字が存在しない場合は0回とする
)  # アルファベットの中で最も多く出現する文字の出現回数

ans = [
    ch for ch in ascii_lowercase if cnt.get(ch, 0) == mx
]  # 複数存在する場合は辞書順最小を選ぶ
print(ans[0])

# 1つだけしか存在しないという条件がある場合は以下
# for ch in ascii_lowercase:
#     if cnt.get(ch, 0) == mx:
#         print(ch)
#         break

# ascii_lowercaseを使わない場合の実装例
# mx = 0
# for c in range(ord('a'), ord('z') + 1):
#     ch = chr(c)
#     if ch in cnt:
#         mx = max(mx, cnt[ch])
# for c in range(ord('a'), ord('z') + 1):
#     ch = chr(c)
#     if ch in cnt and cnt[ch] == mx:
#         print(ch)
#         break

# ordとは、文字を整数に変換する関数で、chrは整数を文字に変換する関数
