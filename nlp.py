# 00. 文字列の逆順

strings = 'stressed'
string_reverse = strings[::-1]
print(string_reverse)

# 01. 「パタトクカシー」
# 1,3,5,7文字目を取り出して連結

a = 'パタトクカシー'
print(a[0] + a[2] + a[4] + a[6])

# 「パトカー」と「タクシー」の文字列を先頭から交互に連結して表示

a = 'パトカー'
b = 'タクシー'
print(a[0] + b[0] + a[1] + b[1] + a[2] + b[2] + a[3] + b[3])
