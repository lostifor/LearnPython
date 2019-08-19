############## 循环 ##################
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))

#无限循环 CTRL+C退出
# var = 1
# while var == 1 :  # 表达式永远为 true
#    num = int(input("输入一个数字  :"))
#    print ("你输入的数字是: ", num)
# print ("Good bye!")

# while else
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# 简单语句组
# while 1: print ('欢迎!')

#################################   for语句    ################################
languages = ["C","C++","OC","Swift","Python"]
for x in languages:
    print(x)
#  for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
################################## range()  ##################################
for i in range(5):
    print(i)
# 使用range指定区间的值：
for i in range(5,9):
    print(i)
# 使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(10,100,30):
    print(i)
for i in range(-10, -100, -30) :
    print(i)

# emample 结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])

listR(range(5))