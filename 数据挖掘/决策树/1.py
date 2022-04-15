from graphviz import Digraph

dot = Digraph(comment='The Round Table')


dot.node('A', 'King Arthur')
dot.view()  #后面这句就注释了，也可以使用这个命令查看效果


dot.node('B', 'Sir Bedevere the Wise')
#dot.view()


dot.node('L', 'Sir Lancelot the Brave')
#dot.view()

#创建一堆边，即连接AB的边，连接AL的边。
dot.edges(['AB', 'AL'])
#dot.view()


dot.edge('B', 'L', constraint='false')
#dot.view()


print(dot.source)
 # doctest: +NORMALIZE_WHITESPACE
#The Round Table
#digraph {
#    A [label="King Arthur"]
#    B [label="Sir Bedevere the Wise"]
#    L [label="Sir Lancelot the Brave"]
#        A -> B
#        A -> L
#        B -> L [constraint=false]
#}


dot.render('test-output/round-table.gv', view=True)