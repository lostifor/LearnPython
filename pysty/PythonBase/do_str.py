# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# 字符串的截取的语法格式如：变量[头下标:尾下标]


# 'I\'m \"OK\"!'
print('I\'mOk.')

# 用r''表示''内部的字符串默认不转义
# print('\\\t\\\')

# print(r'\\\t\\\')

print(''''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')
#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)
#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
totalA = ['item_one','item_two','item_three',
         'item_four','item_five']
print(totalA)

string = "HelloWorld"
print(string)                              #输出字符串
print(string[0:-1])                        #输出第一个到倒数第二个所有的字符
print(string[0])                           #输出字符串第一个字符
print(string[2:5])                         #输出从第三个开始到第五个的字符
print(string[2:])                          #输出总第三个开始所有字符
print(string * 2)                          #输出字符串两次
print(string + '你好')                      #连接字符串

print('hello\nrunoob')                   #使用反斜杠(\)+n转义特殊字符
print(r'hello\nworld')                   #在字符串前面添加一个 r，表示原始字符串，不会发生转义