# function 是一個功能, 可以想像成是一種按鈕
# 語法: def 函式名稱():
           #內容

# 筆記: function 是用來｛收納｝程式碼的
# 筆記:寫程式碼的時候, 盡量把程式碼都收納在function裡面, 是最良好的作法
# 筆記:好處在於 1) 讓程式碼有清楚的架構 2) 增加程式碼的重複使用性

# 定義function
def wash(dry=False, water=8):
	print('加水', water, '分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

# 使用function
wash(water=10) 

# 參數parameter的概念
# 1.當function需要外部資料的時候, 我們就設計投幣孔(參數), 把資料投進去function裡面.
# 2.因為讓function伸手出去外面東西不好
# 3.如果function有投幣孔, 就一定要頭東西(除非有預設值)
# 4.投東西的時候自動式按照參數的順序
# 5.參數如果有預設值,那就不一定要投給他
# 6.投東西給參數的時候, 可以明確指定要投到哪一個參數

def add(x=0, y=0): #寫參數的時候, 等號左右不用空格
	print(x + y)

add(3, 4)
add(123, 100)
add(y=1)
add(5)

# return是回傳的意思
# function如果有return,才可以把function執行的結果給{存}下來
# 可以想像為function運行完後{化身}成為return出來的東西

def add(x, y):
	return x + y 
r = add(3, 4)
print(r)	

def average(numbers):
	return sum(numbers) / len(numbers)
print(average([1, 2, 3]))
print(average([23, 32, 6]))
print(average([180, 34, 92]))