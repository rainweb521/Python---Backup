# Python---Backup
使用Python编写的文件备份程序
使用Python编写的文件备份程序

## 作为程序员平时需要备份许多东西，生怕有些文件改了就找不回来了，尤其是U盘里的经常会被修改，而我又不能一个文件一个文件的对比着去备份，全复制又太浪费时间，网上关于备份的程序很多，但有很多限制，没有我想要的功能，而且有的还会收费，所以决定自己来造个轮子。

## 平时用PHP比较多，我也有想过用PHP写一个类似的文件游览器，但这个轮子就造的有些大了，我只是想自动备份U盘里的东西，能够自动对比匹配目标文件就可以，不需要太臃肿，而Python简单，快速，连界面都不用写，每次直接运行就行。所以我决定使用Python来编写，原理就是对备份目录进行递归，把找到的文件和本地的文件进行对比，对比时使用文件生成md5码来匹配，如果本地不存在，则创建目录，再复制文件。如果没有Python环境，可以直接下载我编译好的.exe程序直接使用，输入时要注意，由于没有写图形界面，文件夹的地址需要输入，一定要保证文件地址的正确，如果是主盘符如d盘，直接写'd:',\n如果是文件夹，例如d盘下的test文件夹，则输入d:/test。

## 下面是运行的效果图片
![](http://blog-1252406596.costj.myqcloud.com/blog/python40.jpg)

