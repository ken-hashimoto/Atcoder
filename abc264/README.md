# [A - "atcoder".substr()](https://atcoder.jp/contests/abc264/tasks/abc264_a)
やるだけ

# [B - Nice Grid](https://atcoder.jp/contests/abc264/tasks/abc264_b)
お絵かきした、チェビシェフ距離とかいうのを使えばお絵かきしなくてもいいらしい。でも本番でそんなことをする勇気はない。

# [C - Matrix Reducing](https://atcoder.jp/contests/abc264/tasks/abc264_c)
削除する行と列をbit全探索で列挙する。計算量はO($2^{H1+W1}H1W1$)なのでpythonだとちょっとキツキツ

# [D - "redocta".swap(i,i+1)](https://atcoder.jp/contests/abc264/tasks/abc264_d)

状態をノードにもったBFSで解いた。これが茶下位なのおかしいだろ。インフレが過ぎる……
転倒数を使っても解けるがすぐには思いつかなかった。