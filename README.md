相信看这篇文章的人都在做深度学习吧，此数据集是为目标检测做的数据集，有错误处请海涵
我的本篇博客地址
http://blog.csdn.net/gaohuazhao/article/details/60871886
第一步：首先了解VOC2007数据集的格式

1)JPEGImages文件夹

文件夹里包含了训练图片和测试图片，混放在一起

2)Annatations文件夹

文件夹存放的是xml格式的标签文件，每个xml文件都对应于JPEGImages文件夹的一张图片

3)ImageSets文件夹

Action存放的是人的动作，我们暂时不用

Layout存放的人体部位的数据。我们暂时不用

Main存放的是图像物体识别的数据，分为20类，当然我们自己制作就呵呵呵不一定了，如果你有精力，Main里面有test.txt , train.txt, val.txt ,trainval.txt.这四个文件我们后面会生成

Segmentation存放的是可用于分割的数据

4)其他的文件夹不解释了，分割XXX等用的

如果你下载了VOC2007数据集，那么把它解压，把各个文件夹里面的东西删除，保留文件夹名字。如果没下载，那么就仿照他的文件夹格式，自己建好空文件夹就行。


第二步：搞定JPEGSImages文件夹

1)把你的图片放到JPEGSImages里面，在VOC2007里面，人家的图片文件名都是000001.jpg类似这样的，我们也统一格式，把我们的图片名字重命名成这样的，如果你的文件太多怎么办，请看我的另一篇文章http://blog.csdn.NET/gaohuazhao/article/details/60324715 能批量重命名文件

第三步：搞定Annatations文件夹

网上很多教程，但是我觉得都很麻烦，直到我遇到了一位大神做的软件，手动标注，会自动生成图片信息的xml文件

1)本项目中的labelImg-master,执行labelImg.py

2)保存的路径就是我们的Annatations文件夹，别保存别的地方去了，，，

3)一张张的慢慢画框。。。。。。。。。大约过了几个小时，好继续下一步

第四步：搞定ImageSets文件夹中的Main文件夹中的四个文件

直接上一个代码给你：
make_main_txt.py

OK，制作完成，就是这么简单，那么解释一下这四个txt文档是干嘛的，看名字就知道，就是分分多少图片作为训练，多少图片作为测试，，，，


我们将继续填坑
