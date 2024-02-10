a, m, l, r = map(int, input().split())

# まずは問題を単純化するため、 L と R から A を引き、クリスマスツリーは座標が M の倍数である各地点に立っているものとします。
l -= a
r -= a

# 座標が kM である地点に立っているクリスマスツリーの番号を k とします。「座標が L 未満の地点にあるクリスマスツリーのうち一番東にあるものの番号」および「座標が R 以下の地点にあるクリスマスツリーのうち一番東にあるものの番号」をそれぞれ l,r とすると、答えは r−l になります。
# あとは、ある x に対して「座標が x 以下の地点にあるクリスマスツリーのうち一番東にあるものの番号」が求められればよいですが、これは「x/M⌋ という簡単な式で表されます。
print(r // m - (l - 1) // m)

# l // m は「座標が l 以下の地点にあるクリスマスツリーのうち一番東にあるものの番号」を求めます。しかし、この問題では「座標が l 未満の地点にあるクリスマスツリーのうち一番東にあるものの番号」が必要です。

# したがって、l // m から 1 を引くのではなく、l - 1 を m で割ることで、「座標が l 未満の地点にあるクリスマスツリーのうち一番東にあるものの番号」を求めることができます。

# 例えば、m が 3 で l が 6 の場合、l // m は 2 になりますが、これは座標 6 にあるクリスマスツリーの番号です。しかし、座標が 6 未満の地点にあるクリスマスツリーのうち一番東にあるものの番号を求めるためには、l - 1 すなわち 5 を m で割る必要があり、その結果は 1 となります。
