# nlp-practice

# question 00. 文字列の逆順
# 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

strings = 'stressed'
string_reverse = strings[::-1]
print(string_reverse)

# question 01. 「パタトクカシー」
# 1,3,5,7文字目を取り出して連結

a = 'パタトクカシー'
print(a[0] + a[2] + a[4] + a[6])

# 「パトカー」と「タクシー」の文字列を先頭から交互に連結して表示

a = 'パトカー'
b = 'タクシー'
print(a[0] + b[0] + a[1] + b[1] + a[2] + b[2] + a[3] + b[3])

# question 03. 円周率

# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = sentence.replace(",", "").replace(".", "").split(" ")

# リストの中に繰り返し構文で数字を列挙

result = [len(word) for word in words]
print(result)


# question 04. 元素記号
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．



