# print(188)
# print('100 + 200 =',100+200)

name = input('请输入访问者姓名？')
print('hello,',name)
firstNum = int(input('请输入第一个数字：'))
secondNum = int(input('请输入第二个数字：'))
# print('计算结果',%,'+',secondNum,'=',firstNum+secondNum)
# 显示计算结果
print('数字 {0} 和 {1} 相加结果为：{2}'.format(firstNum, secondNum, firstNum+secondNum))