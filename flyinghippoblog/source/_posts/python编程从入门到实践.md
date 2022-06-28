---
title: python编程从入门到实践
date: 2020-11-2
tags:
mathjax: true

---



《Python编程：从入门到实践》，作者Eric Matthes，译者袁国忠，由人民邮电出版社于2016年7月出版。



PS：

- 前十章内容简单，好多东西都没总结进来
- 第十一章测试程序以后可以写一下
- 项目一：外星人入侵先不完整的看，第十二、十三、十四章略
- 项目二数据的可视化要认真地理解json和csv的应用和matplotlib，以后用处比较大

知识点复习复习

<!-- more -->

# 第1章　起步

## 1.1　搭建编程环境　

略

# 第2章　变量和简单数据类型

## 2.1　运行hello_world.py时发生的情况

略

## 2.2　变量　16

- 变量命名规则：
  - 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
  - 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
  - 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print（请参见附录A.4）。
  - 变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
  - 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
  - 在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意。

## 2.3　字符串　18

- 在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号
- 方法：title()、upper()、lower()
- 删除空格：rstrip()、lstrip()、strip()  这种删除只是暂时的，要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中

## 2.4　数字　24

- str()

## 2.5　注释　27

- 在Python中，注释用井号（#）标识。井号后面的内容都会被Python解释器忽略

## 2.6　Python之禅　28

- import this

## 2.7　小结　30

# 第3章　列表简介　31

## 3.1　列表是什么　31

- 列表、索引

## 3.2　修改、添加和删除元素　33

- 修改：直接赋值
- 添加(方法)：append()、insert()
- 删除（方法）：del()、pop()、remove()

## 3.3　组织列表　39

- 方法sort：永久性改变
- sorted()：临时性排序
- 方法reverse()永久性地修改列表元素的排列顺序
- 函数len()可快速获悉列表的长度

## 3.4　使用列表时避免索引错误　42

略

## 3.5　小结　43

略

# 第4章　操作列表　44

## 4.1　遍历整个列表　44

- for循环

## 4.2　避免缩进错误　47

略

## 4.3　创建数值列表　51

- range() 

- 列表解析

  　　[expression for iter_val in iterable]

    　　[expression for iter_val in iterable if cond_expr]

## 4.4　使用列表的一部分　54

- 列表切片
- 列表变量名直接赋值是浅复制，如果需要建立一个独立的副本，可使用包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）

## 4.5　元组　59

- 元组不能单个修改某一个变量的值，但是可以整体赋值

## 4.6　设置代码格式　61

- pep8

## 4.7　小结　63

# 第5章　if语句　64

## 5.1　一个简单示例　64

## 5.2　条件测试　65



## 5.3　if语句　70



## 5.4　使用if语句处理列表　76



## 5.5　设置if语句的格式　80

## 5.6　小结　80

第6章　字典　81

6.1　一个简单的字典　81

6.2　使用字典　82



6.3　遍历字典　87

- for key, value in user_0.items():
- 

6.4　嵌套　93



6.5　小结　99

第7章　用户输入和while循环　100

7.1　函数input()的工作原理　100



7.2　while循环简介　104



7.3　使用while循环来处理列表和字典　110



7.4　小结　113

# 第8章　函数　114

## 8.1　定义函数　114



## 8.2　传递实参　116



## 8.3　返回值　121



## 8.4　传递列表　126



## 8.5　传递任意数量的实参　130



## 8.6　将函数存储在模块中　133



## 8.7　函数编写指南　136

## 8.8　小结　137

# 第9章　类　138

## 9.1　创建和使用类　138



## 9.2　使用类和实例　142



## 9.3　继承　147



## 9.4　导入类　153



## 9.5　Python标准库　159

## 9.6　类编码风格　161

## 9.7　小结　161

# 第10章　文件和异常　162

## 10.1　从文件中读取数据　162



## 10.2　写入文件　169

- Python只能将字符串写入文本文件。

- 函数write()不会在你写入的文本末尾添加换行符

## 10.3　异常　172



## 10.4　存储数据　180



## 10.5　小结　186









# 第11章　测试代码　187

## 11.1　测试函数　187

- Python标准库中的模块unittest提供了代码测试工具

- 要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。

- ```python
  name_function.py
  ---
  def get_formatted_name(first, last):
      """Generate a neatly formatted full name."""
      full_name = first + ' ' + last
      return full_name.title()
  ---
  
  test_name_ function.py # 样例
  ---
  import unittest
  from name_function import get_formatted_name
  
  class NamesTestCase(unittest.TestCase):
  	"""测试name_function.py"""
  	def test_first_last_name(self):
  		"""能够正确地处理像Janis Joplin这样的姓名吗？"""
  		formatted_name = get_formatted_name('janis', 'joplin')
  		self.assertEqual(formatted_name, 'Janis Joplin')
  unittest.main()
  ```

- 注意的点：

  - 导入模块unittest
  - 创建一个类，这个类必须继承unittest.TestCase类
  - 运行test_name_function.py时，所有以test_打头的方法都将自动运行。

## 11.2　测试类　193

- unittest Module中的断言方法

- 方 法           用 途
  assertEqual(a, b)     核实a == b
  assertNotEqual(a, b)     核实a != b
  assertTrue(x)     核实x为True
  assertFalse(x)     核实x为False
  assertIn(item, list)     核实item在list中
  assertNotIn(item, list)     核实item不在list中

- unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们。

- 样例：

  - ```python
    class AnonymousSurvey():
    	"""收集匿名调查问卷的答案"""
        def __init__(self, question):
            """存储一个问题，并为存储答案做准备"""
            self.question = question
            self.responses = []
            
        def show_question(self):
            """显示调查问卷"""
            print(question)
            
        def store_response(self, new_response):
            """存储单份调查答卷"""
            self.responses.append(new_response)
            
        def show_results(self):
            """显示收集到的所有答卷"""
            print("Survey results:")
            for response in responses:
            	print('- ' + response)
    ```

    

  - ```python
    import unittest
    from survey import AnonymousSurvey
    
    class TestAnonymousSurvey(unittest.TestCase):
        """针对AnonymousSurvey类的测试"""
        def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
        def test_store_single_response(self):
            """测试单个答案会被妥善地存储"""
            self.my_survey.store_response(self.responses[0])
            self.assertIn(self.responses[0], self.my_survey.responses)
            
        def test_store_three_responses(self):
            """测试三个答案会被妥善地存储"""
            for response in self.responses:
            	self.my_survey.store_response(response)
            for response in self.responses:
            	self.assertIn(response, self.my_survey.responses)
                
                
    unittest.main()
    ```

    

## 11.3　小结　199





# 项目1 外星人入侵　202

第12章　武装飞船　203

12.1　规划项目　203

12.2　安装Pygame　204



12.3　开始游戏项目　207



12.4　添加飞船图像　211



12.5　重构：模块game_functions　214



12.6　驾驶飞船　216



12.7　简单回顾　223



12.8　射击　224



12.9　小结　231

第13章　外星人　232

13.1　回顾项目　232

13.2　创建第一个外星人　233



13.3　创建一群外星人　236



13.4　让外星人群移动　242



13.5　射杀外星人　246



13.6　结束游戏　250



13.7　确定应运行游戏的哪些部分　255

13.8　小结　256

第14章　记分　257

14.1　添加Play 按钮　257

14.1.1　创建Button类　258

14.1.2　在屏幕上绘制按钮　259

14.1.3　开始游戏　261

14.1.4　重置游戏　261

14.1.5　将Play 按钮切换到非活动状态　263

14.1.6　隐藏光标　263

14.2　提高等级　264

14.2.1　修改速度设置　264

14.2.2　重置速度　266

14.3　记分　267

14.3.1　显示得分　267

14.3.2　创建记分牌　268

14.3.3　在外星人被消灭时更新得分　270

14.3.4　将消灭的每个外星人的点数都计入得分　271

14.3.5　提高点数　271

14.3.6　将得分圆整　272

14.3.7　最高得分　274

14.3.8　显示等级　276

14.3.9　显示余下的飞船数　279

14.4　小结　283





# 项目2 数据可视化　284

## 第15章　生成数据　285

## 15.1　安装matplotlib　285

略

## 15.2　绘制简单的折线图　287

- ```python
  import matplotlib.pyplot as plt
  ```

  模块pyplot包含很多用于生成图表的函数。

- plt.plot()：这个函数尝试根据这些数字绘制出有意义的图形

- plt.show()：打开matplotlib查看器，并显示绘制的图形

- eg：plt.plot(squares, linewidth=5)  参数linewidth决定了plot()绘制的线条的粗细。

- 函数plt.title()给图表指定标题。参数fontsize指定了图表中文字的大小。

- 函数xlabel()和ylabel()让你能够为每条轴设置标题

- 函数tick_params()设置刻度的样式，其中指定的实参将影响x轴和y轴上的刻度（axes='both'），并将刻度标记的字号设置为14（labelsize=14）



- 要绘制单个点，可使用函数scatter()，并向它传递一对x和y坐标，它将在指定位置绘制一个点：plt.scatter(2, 4)
- 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
- 函数axis()指定了每个坐标轴的取值范围。要求提供四个值：x和y坐标轴的最小值和最大值。
- matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，要删除数据点的轮廓，可在调用scatter()时传递实参edgecolor='none'。
- 要修改数据点的颜色，可向scatter()传递参数c，并将其设置为要使用的颜色的名称。还可以使用RGB颜色模式自定义颜色。要指定自定义颜色，可传递参数c，并将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。



- 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。

  ```python
  plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=40)
  ```

  将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。

- 要让程序**自动将图表保存**到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用

- ```python
  # 隐藏坐标轴
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)
  ```



- 函数figure()用于指定图表的宽度、高度、分辨率和背景色。形参figsize指定一个元组，向matplotlib指出绘图窗口的尺寸，单位为英寸。可使用形参dpi向figure()传递该分辨率。



## 15.3　随机漫步　295

略

## 15.4　使用Pygal模拟掷骰子　303

- Python可视化包Pygal来生成可缩放的矢量图形文件
- http://www.pygal.org/en/stable/



## 15.5　小结　311

略

# 第16章　下载数据　312

## 16.1　CSV文件格式　312

- 数据作为一系列以逗号分隔的值（CSV）写入文件。这样的文件称为CSV文件。
- csv模块包含在Python标准库中，可用于分析CSV文件中的数据行
- csv.reader()，将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader）对象



- 方法fill_between()，它接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间。实参alpha指定颜色的透明度。Alpha值为0表示完全透明，1（默认设置）表示完全不透明。

## 16.2　制作世界人口地图：JSON格式　324



## 16.3　小结　337

# 第17章　使用API　338

## 17.1　使用Web API　338

- requests包让Python程序能够轻松地向网站请求信息以及检查返回的响应

- ```python
  import requests
  
  url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
  r = requests.get(url)
  print("Status code:", r.status_code)
  # 将API响应存储在一个变量中
  response_dict = r.json()
  # 处理结果
  print(response_dict.keys())
  ```

  

## 17.2　使用Pygal可视化仓库　344



## 17.3　Hacker News API　350

## 17.4　小结　353

# 项目3 Web 应用程序　354

第18章　Django入门　355

18.1　建立项目　355

18.1.1　制定规范　355

18.1.2　建立虚拟环境　356

18.1.3　安装virtualenv　356

18.1.4　激活虚拟环境　357

18.1.5　安装Django　357

18.1.6　在Django中创建项目　357

18.1.7　创建数据库　358

18.1.8　查看项目　359

18.2　创建应用程序　360

18.2.1　定义模型　360

18.2.2　激活模型　362

18.2.3　Django管理网站　363

18.2.4　定义模型Entry　365

18.2.5　迁移模型Entry　366

18.2.6　向管理网站注册Entry　366

18.2.7　Django shell　367

18.3　创建网页：学习笔记主页　369

18.3.1　映射URL　369

18.3.2　编写视图　371

18.3.3　编写模板　372

18.4　创建其他网页　373

18.4.1　模板继承　373

18.4.2　显示所有主题的页面　375

18.4.3　显示特定主题的页面　378

18.5　小结　381

第19章　用户账户　382

19.1　让用户能够输入数据　382

19.1.1　添加新主题　382

19.1.2　添加新条目　386

19.1.3　编辑条目　390

19.2　创建用户账户　392

19.2.1　应用程序users　393

19.2.2　登录页面　394

19.2.3　注销　396

19.2.4　注册页面　397

19.3　让用户拥有自己的数据　400

19.3.1　使用@login_required限制访问　400

19.3.2　将数据关联到用户　402

19.3.3　只允许用户访问自己的主题　405

19.3.4　保护用户的主题　405

19.3.5　保护页面edit_entry　406

19.3.6　将新主题关联到当前用户　406

19.4　小结　408

第20章　设置应用程序的样式并对其进行部署　409

20.1　设置项目“学习笔记”的样式　409

20.1.1　应用程序django-bootstrap3　410

20.1.2　使用Bootstrap来设置项目“学习笔记”的样式　411

20.1.3　修改base.html　411

20.1.4　使用jumbotron设置主页的样式　414

20.1.5　设置登录页面的样式　415

20.1.6　设置new_topic页面的样式　416

20.1.7　设置topics页面的样式　417

20.1.8　设置topic页面中条目的样式　417

20.2　部署“学习笔记”　419

20.2.1　建立Heroku账户　420

20.2.2　安装Heroku Toolbelt　420

20.2.3　安装必要的包　420

20.2.4　创建包含包列表的文件requirements.txt　421

20.2.5　指定Python版本　422

20.2.6　为部署到Herohu而修改settings.py　422

20.2.7　创建启动进程的Procfile　423

20.2.8　为部署到Herohu而修改wsgi.py　423

20.2.9　创建用于存储静态文件的目录　424

20.2.10　在本地使用gunicorn服务器　424

20.2.11　使用Git跟踪项目文件　425

20.2.12　推送到Heroku　426

20.2.13　在Heroku上建立数据库　427

20.2.14　改进Heroku部署　428

20.2.15　确保项目的安全　429

20.2.16　提交并推送修改　430

20.2.17　创建自定义错误页面　431

20.2.18　继续开发　434

20.2.19　设置SECRET_KEY　434

20.2.20　将项目从Heroku删除　434

20.3　小结　435

附录A　安装Python　436

附录B　文本编辑器　441

附录C　寻求帮助　447

附录D　使用Git进行版本控制　451

后记　460 [1]