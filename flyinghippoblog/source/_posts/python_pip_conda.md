---
title: pip conda
date: 2021-3-18
tags:
mathjax: true


---



注释前言

未排版

··

<!-- more -->

[python的文本介绍](https://docs.python.org/3.9/using/windows.html#windows-embeddable)



- python 是一种语言，可以在很多平台上应用。
- python可以从官网下载，有3.0/2.0两个大版本，官网有几个不同的文件：
  - web-based--需要联网安装。它将在安装过程中，根据需要自动下载所需的组件
  - executable--可执行文件（.exe），本地安装。
  - embeddable zip--嵌入式版本，可以集成到其它应用中。是一个包含最小Python环境的ZIP文件
- 安装官网安装包时会让选是否安装pip、idle等
- pycharm是一种ide，有很多开发的动能，但是要自己下载python才能使用。
- 运行python的三种方式：
  - 交互式解释器：通过命令行进入python，然后在里边写python。
  - 命令行脚本：通过引入解释器可以在命令行中执行Python脚本。
  - 集成开发环境（IDE）：pycharm vscode
- CPython特指用C语言实现的python，就是常说的python。当说CPython时是为了把他和其他的python实现方式区分开，比如Java版本的JPython、PyPy等
- 当有一个Python代码以.py为扩展名，要运行代码，就需要Python解释器去执行.py文件。事实上存在多种python解释器。CPython是使用最广的python解释器。
- IPython：IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的。
- 除了标准CPython发行版本外，还有一些包含拓展包的版本：ActivePython、Anaconda、Canopy、WinPython。这些包文件可能不包含最新的Python版本，并且不由核心Python团队维护。
- Python Launcher（[参考](https://www.cnblogs.com/Neeo/p/8393805.html)）
  - 在[PEP 397](https://www.python.org/dev/peps/pep-0397/)中正式出现并伴随Python3.3版本发布
  - 是用于Windows中的一个实用程序，可帮助我们定位和执行不同版本的Python解释器。
  - Python launcher有两个版本，一个是控制台程序，另一个是‘windows’(即GUI)程序。这两个程序对应我们Python安装目录中的‘python.exe’和‘pythonw.exe’这两个可执行文件。
- python环境变量
  - PYTHONPATH：PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。
  - PYTHONSTARTUP：Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此变量指定的文件中的代码。
  - PYTHONCASEOK：加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写.
  - PYTHONHOME：另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。
  - 一般安装完python需要将两个东西添加到环境变量里边：
    - python的安装路径，对应python.exe，保证cmd时能找到python解释器，python文件的运行、
    - python的安装路径下的script文件夹，下面有pip文件等， pip 用于包安装程序
- python的卸载也需要用安装包
- Anaconda（[官方网站](https://link.jianshu.com/?t=https%3A%2F%2Fwww.anaconda.com%2Fdownload%2F%23macos)）可以便捷获取包且对包能够进行管理，同时对环境可以统一管理的发行版本。Anaconda包含了conda、Python在内的超过180个科学包及其依赖项。
- anaconda的环境变量：
  - E:\Anaconda（Python需要）
  - E:\Anaconda\Scripts（conda自带脚本）
  - E:\Anaconda\Library\mingw-w64\bin（使用C with python的时候）
  -  E:\Anaconda\Library\usr\bin
  - E:\Anaconda\Library\bin（jupyter notebook动态库）
- conda：是包及其依赖项和环境的管理工具。conda为Python项目而创造，但可适用于上述的多种语言。conda包和环境管理器包含于Anaconda的所有版本当中
- pip是用于安装和管理软件包的包管理器。
- virtualenv：用于创建一个**独立的**Python环境的工具。virtualenv将会为它自己的安装目录创建一个环境，这并**不与**其他virtualenv环境共享库；同时也可以**选择性**地不连接已安装的全局库。
























































