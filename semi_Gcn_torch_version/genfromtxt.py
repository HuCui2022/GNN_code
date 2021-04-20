
# author: cuihu
# time : 2021/4/19 20:08
# task: 
__author__ = 'tum'

import numpy as np

# 一个最简单的例子
f = open('test.csv', 'w')
f.write("1,1.2,1.3\n2,2.2,2.3")
f.close()
a = np.genfromtxt('test.csv', dtype=[('myint', 'i8'), ('myfloat', 'f8'), ('mystring', 'U5')], delimiter=",",
                  comments='#')
print(a)


# 字段中有中文,成功！
def conv_str_chs(x):
    # print(x)
    return x.decode('gb2312')


f = open('test.csv', 'w')
f.write("1,1.2,今123天\n2,2.2,789天")
f.close()
a = np.genfromtxt('test.csv', dtype=[('myint', 'i8'), ('myfloat', 'f8'), ('mystring', 'U5')], delimiter=",",
                  comments='#',
                  converters={2: conv_str_chs})
print(a)

# 空缺部分字段, 使用默认填充。文档中描述：
# Expected type Default
# bool False
# int -1
# float np.nan
# complex np.nan+0j
# string '???'

f = open('test.csv', 'w')
f.write(",,")
f.close()
a = np.genfromtxt('test.csv', dtype=[('myint', 'i8'), ('myfloat', 'f8'), ('mystring', 'U5')], delimiter=",",
                  comments='#',
                  filling_values={0: 9, 1: 9.9, 2: 'abc'})
print(a)



