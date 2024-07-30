1. 基于 [Sphinx+gitee+Read the Docs] 搭建的在线wiki系统, 参考: https://blog.csdn.net/hbsyaaa/article/details/118530934

2. 编译 html 命令:
1) 普通编译 : make.bat html
2) 本地编译且构建http server :  sphinx-autobuild source build/html



## 3. 支持Markdown

- markdown 语法:

  - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple recommonmark

- markdown 表格:

  - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx_markdown_tables

    ```
    #extensions = [
    #]
    extensions = ['recommonmark','sphinx_markdown_tables']
    ```

    

