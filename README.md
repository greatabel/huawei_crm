1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
命令行底下运行: 
python3 i6wsgi.py


<!-- 开启另一个命令行运行，运行：
jupyter notebook i5ml_spark_anlysis.ipynb -->

可以运行可视化部分、查看分析结果部分



6.
浏览器访问：

http://localhost:5000/home

默认账号 greatabel1@126.com ps:abel
自己也可以正常注册

7.
（可选）
i0pyspark_analysis.ipynb 是利用java/spark/pyspark 进行处理和数据统计分析的部分 （已经缓存，属于可选部分，可以不用关系）
如果需要查看pyspark分析部分，可以命令行运行：
jupyter notebook i0pyspark_analysis.ipynb
然后浏览器访问：
http://localhost:8888/notebooks/i0pyspark_analysis.ipynb


# --------------------
工程说明部分：




可视化和分析部分主要用到啦这些python库：
NumPy 
	NumPy 是使用 Python 进行科学计算的基础软件包。它可用来存储和处理大型矩阵，比使用 Python 本身处理要高效的多，支持高维度数组与矩阵的运算，此外也针对数组提供了大量的数学函数库
Pandas
	为Python 编程语言提供高性能，易于使用的数据结构和数据分析工具，和numpy打配合的
Matplotlib和Seaborn
	Seaborn是用户把自己常用到的可视化绘图过程进行了函数封装，形成的一个“快捷方式”，他相比Matplotlib的好处是代码更简洁，可以用一行代码实现一个清晰好看的可视化输出。主要的缺点则是定制化能力会比较差，只能实现固化的一些可视化模板类型；而Matplotlib是可以实现高度定制化绘图的，高度定制化可以让你获得最符合心意的可视化输出结果，但也因此需要设置更多的参数，因而代码更加复杂一些

我们的展示整个结果的网站是flask，前端部分是jinja+vue+echart+js



