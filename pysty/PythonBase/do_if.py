############################    条件控制    ###########################
x = int(input('请输入第一个数字x:')) 
y = int(input('请输入第二个数字y:'))

if x >= y:
    print('第一个数字大：',x)
else:
    print('第二个数字大：',y)
#注意缩进空格数保持一致
# 注意：
# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句。

var1 = 100
if var1:
    print ('1 - if 表达式条件为 true')
    print (var1)

var2 = 0
if var2:
    print ('2 - if 表达式条件为 true')
    print (var2)

#example
age = int(input("请输入你家狗的年龄:"))
print("")
if age < 0:
    print ("未出生！")
elif age == 1:
    print ("相当于 14 岁的人类")
elif age == 2:
    print ("相当于 22 岁的人类")
elif age > 2:
    human = 22 + (age -2)*5
    print ("对应人类年龄:",human)
#退出
input ("点击 Enter 退出")


#操作运算符 与 if嵌套 与OC相同