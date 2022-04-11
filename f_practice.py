# 題目:
# 寫一個function判斷是不是閏年(二月會多一天的年)
# 
# 定義: 
# 1. 公元年份除以4不可整除, 為平年
# 2. 公元年份除以4可以整除但除以100不可整除, 為閏年
# 3. 公元年份除以100可整除但除以400不可整除, 為平年
# 4. 公元年份除以400可整除但除以3200不可整除, 為閏年
#
# 提示:
# 1. function要有個參數讓使用者投入(傳遞進去)年分
# 2. funtion的回傳值(return)應該是布林值, 如果是閏年就return True, 不適就return False
# 3. 請把function命名為is_leap, 這樣才可以執行測試 (PS is_leap就是"是不是閏年"的意思)
# 4. 要用到%這個符號來求餘數

# 嘗試1:
# year = input('請輸入年份: ')
# year = int(year)
# def is_leap():
# 	if year % 4 != int:
# 		return print('平年')
# 	elif year % 4 == 0 and year/100 != 0:
# 		return print('閏年')
# 	elif year % 100 == 0 and year % 400 != 0:
# 		return print('平年')
# 	elif year % 400 == 0 and year % 3200 != 0:
# 		return print('閏年')
# r = is_leap(year)
# print(r)

# 嘗試2:
year = input('請輸入年份: ')
year = int(year)
def is_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	elif year % 3200 != 0:
		return True
	else:
		return False
print(is_leap(year))