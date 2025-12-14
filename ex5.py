# 輸入三個正整數,分別代表三角形的三個邊長,請判斷它們是否能構成一個三角形。
# 一組邊長能構成三角形的條件是:任意兩邊的和必須大於第三邊

a = int(input("請輸入第一邊長: "))
b = int(input("請輸入第二邊長: "))
c = int(input("請輸入第三邊長: "))

if a + b > c and b + c > a and a + c > b:
    print("可以構成三角形")
else:
    print("無法構成三角形")

# 輸入年齡,若年齡>=65歲則輸出「老年」,若45<=年齡<65歲間則輸出「中年」,
# 若25<=年齡<45間歲則輸出「壯年」,其他則輸出「年輕族群」

age = int(input("請輸入年齡: "))

if age >= 65:
    print("老年")
elif age >= 45:
    print("中年")
elif age >= 25:
    print("壯年")
else:
    print("年輕族群")

#輸 入 一 個 分 數 ( 整 數 , 範 圍 0–100),請根據以下規則輸出對應的等第:
# 90 分以上:A
# 80–89 分:B
# 70–79 分:C
# 60–69 分:D
# 60 分以下:F

score = int(input("請輸入分數: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")