#-*- coding=utf8 -*-
#使用函数对指定目录进行深层次遍历，先列出来所有的文件和目录
#再去指定的目录里再次查找文件和目录，一直深入下去
# 如果是文件，就不再深入下去，而去判断路径是否存在于电脑中，
# 不存在则将其复制
import hashlib
import os
import shutil
#用于判断两个文件是否相同，提取每个文件中的前4字节的内容然后输出md5码进行比较
def md5check(fname):
    m = hashlib.md5()
    with open(fname) as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
#文件复制的函数
def copy(path):
    new_path = path
    new_path = new_path.replace(old_scoure, new_scoure) #将原盘符替换为我所要存放的目标盘符
    print path + "---copy---" + new_path
    if os.path.isfile(new_path): #如果目标文件存在
        old_md = md5check(path)  #提取源文件的md5
        new_md = md5check(new_path)  #提取目标文件的md5
        if old_md != new_md:  #如果不相等，说明源文件有修改
            shutil.copy(path, new_path) #因为已经判断了目标文件的存在，所以不需要创建目录，直接复制就可以
    else: #如果目标文件不存在
        dirname = os.path.dirname(new_path) # 提取目标的目录
        if os.path.exists(dirname): #目录存在
            shutil.copy(path, new_path) #直接复制文件
        else: #目录不存在
            try:
                os.makedirs(dirname) #使用多级目录创建函数创建目录
                shutil.copy(path, new_path) #直接复制文件
            except WindowsError: #错误反馈，而不会停止操作
                print "创建目录出错"
# 查找所有目录文件的递归函数
def lsdir(forder):
    path = os.listdir(forder) #分离出来的文件列表
    # print forder
    # print path
    for line in path: #逐个判断
        line = forder + "/" + line #没有使用join函数，因为会出现 \
        if (os.path.isdir(line)): #是目录就继续进行递归
            lsdir(line)
        else:
            # path = os.path.join(forder,line)
            # print 'l:'+line
            copy(line) #将文件的地址传到copy函数中去复制
        # break
def test():
    print new_scoure
if __name__=='__main__':
    # lsdir('e:/test')
    global old_scoure
    global new_scoure #设置为全局变量
    concent = "请保证地址的正确性，如果是主盘符如d盘，直接写'd:',\n如果是文件夹，例如d盘下的test文件夹，则输入d:/test"
    c_unicode = concent.decode("utf-8") #为了在cmd显示中文，需要进行转码
    # c_gbk = c_unicode.encode("gbk")
    print c_unicode
    concent = "输入要备份的文件地址："
    c_unicode = concent.decode("utf-8")
    print c_unicode
    old_scoure = raw_input()
    concent = "输入备份文件要存放的地址,请保证地址存在："
    c_unicode = concent.decode("utf-8")
    print c_unicode
    new_scoure = raw_input()
    # path = 'e:/Markdown'
    lsdir(old_scoure)
    concent = "输入任意键关闭"
    c_unicode = concent.decode("utf-8")
    print c_unicode
    raw_input()
    # print md5check(path)
    # path = path.replace('e:', 'f:')
    # print md5check(path)
    # copy(path)
    # print path[0]
    # path = path.replace('e:','f:')
    # print path
    # dirname = 'f:/test/1'
    # print os.path.dirname(path)
    # # try:
    # if os.path.exists(dirname):
    #     print "12"
    # else:
    #     os.makedirs(dirname)
    # except WindowsError :
    #     print "23"
        # shutil.copy(path, 'f:/test/1/1.txt')
    # f = open(path,'w')
    # f.close()
    # os.mknod(path)
# path = 'e:/test'
# path_list = os.listdir('e:/test')
# print path_list
# for line in path_list:
#     line = path + "/" + line
#     if(os.path.isdir(line)):
#         print os.listdir(line)
#     else:
#         print os.path.basename(line)
#         # shutil.copy(line,'f:/test/1.txt')