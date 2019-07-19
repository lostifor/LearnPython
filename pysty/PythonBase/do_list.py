#列表
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
    
# 元组
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组