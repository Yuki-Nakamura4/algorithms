import sys


# UnionFindの実装
# parent, sizeの2つの配列を持つ。
# parent: それぞれのノードの親ノードを管理する。グループの代表(ルート)の親は自分自身を指す
# size: それぞれのノードがルートの親として管理するノードの数を管理する。
#
# find,same,uniteの3つのメソッドを持つ。
# find: 指定されたノードの親ノードを辿ってルートの親を返す。探す過程で経路圧縮を行う
# same: 指定された2つのノードのルートの親が同一か(同じグループかどうか)を判定する。
# unite: 指定された2つのノードが既に同じグループに属していればFalseを返し、そうでなければ小さい方を大きい方に連結してTrueを返す。
class UnionFind:
    """Union-Find木(経路圧縮＋ランク付き併合)。
    各頂点が属する連結成分を管理し、サイクル判定に使う。
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def same(self, a: int, b: int):
        if self.find(a) == self.find(b):
            return True
        return False

    def unite(self, a: int, b: int):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = self.parent[ra]
        self.size[ra] += self.size[rb]

        return True
