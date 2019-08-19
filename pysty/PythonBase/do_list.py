    
################################   列表      ##############################
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 变量[头下标:尾下标]

list = ['abcd',786,2.23,'helloworld',70.2]
tinylist = [123,'helloworld']

print(list)             #打印列表
print(list[0])          #打印第0个元素
print(list[1:3])        #打印第1到第3个元素
print(list[2:])         #打印第2个开始所有元素
print(tinylist * 2)     #输出tinylist列表两次
print(list + tinylist)  #连接列表

#运行结果
# appledeiMac:LearnPython apple$ /usr/local/opt/python/bin/python3.7 /Users/apple/Desktop/PyLearn/LearnPython/pysty/PythonBase/do_list.py
# ['abcd', 786, 2.23, 'helloworld', 70.2]
# abcd
# [786, 2.23]
# [2.23, 'helloworld', 70.2]
# [123, 'helloworld', 123, 'helloworld']
# ['abcd', 786, 2.23, 'helloworld', 70.2, 123, 'helloworld']
# appledeiMac:LearnPython apple$ 

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字
a = ['abcd', 786, 2.23, 'helloworld', 70.2, 123, 'helloworld']
print(a[1:4:2])

def reverseWords(input):
    #通过空格分隔字符串，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

if  __name__ == "__main__":
    input = 'I learn Python feel Good!'
    rw = reverseWords(input)
    print(rw)
    
################################   元组      ##############################
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

print(len(tuple))

# 注意：
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。


################################   Set（集合） ##############################
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# example
student = {'Tom','Jim','Mary','Tom','Jack','Rose','Lee'}
print(student) # 输出student集合，重复的元素被自动去除
#成员测试
if 'Rose' in student:
    print('Rose在Student集合中')
else:
    print('Rose不在Student集合中')

student_cn = {'Jane','Jam','Mei','Cheng','Tom','Champ','Lee'}

#集合运算
print(student)
print(student_cn)
print(student - student_cn)     #student 与 student_cn 的差集
print(student | student_cn)     #student 与 student_cn 的并集
print(student & student_cn)     #student 与 student_cn 交集
print(student ^ student_cn)     #student 与 student_cn 并集去除交集（不同时存在的元素）


################################   字典      ##############################
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict = {} #空字典
dict['one'] = '1-index'
dict[2] = "2-Tool"
tinydict = {'name': 'lostifor','code':1, 'site': 'xxx.xx.com'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

# dict([('lostifor',1),('Google',2),('Taobao',3)])
# print(dict1)
# dict(lostifor = 1,google = 2,Taobao = 3)
# print(dict2)
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。

################################ Python数据类型转换 ##############################


# 函数	描述
# int(x [,base]) 将x转换为一个整数

# float(x) 将x转换到一个浮点数

# complex(real [,imag]) 创建一个复数

# str(x) 将对象 x 转换为字符串

# repr(x) 将对象 x 转换为表达式字符串

# eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象

# tuple(s) 将序列 s 转换为一个元组

# list(s) 将序列 s 转换为一个列表

# set(s) 转换为可变集合

# dict(d) 创建一个字典。d 必须是一个 (key, value)元组序列。

# frozenset(s) 转换为不可变集合

# chr(x) 将一个整数转换为一个字符

# ord(x) 将一个字符转换为它的整数值

# hex(x) 将一个整数转换为一个十六进制字符串

# oct(x) 将一个整数转换为一个八进制字符串