#pyinstaller -F demo.py    只在dist中生产一个demo.exe文件；
#pyinstaller -D demo.py    默认选项，除了demo.exe外，还会在在dist中生成很多依赖文件，推荐使用；
#pyinstaller -c demo.py    默认选项，只对windows有效，使用控制台，就像编译运行C程序后的黑色弹窗；
#pyinstaller -w demo.py   只对windows有效，不使用控制台；
#pyinstaller -i G:\Projectfile\wordtopdf.ico demo.py  将wordtopdf.icon设置为exe文件的图标。
