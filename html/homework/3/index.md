#Home Work3:最小生成树#

*翻译* Qi

[原始网页](http://shtech.org/course/ds/homework/3/)

**Hand out**

参考程序:[spantree]("http://shtech.org/course/ds/homework/3/spantree")

翻译的家伙写的[**测试工具集**](haha.html)哦

###背景知识###

在很久远的年代，有一个国家马富汗斯坦。这个国家有n个城市和m条陈旧的路，其中每条陈旧的路呢，都链接着两座城市。
并且，因为高危山脉的缘故，有些城市之间是没有路或者小道的。（也就是说有的城市是不能到答另外的某座城的）。
在传播民主之花的名为自由马富汗斯坦的运动如野火一般在这个国家的城市Santa Barbara传播的期间，马国军队销毁了这个国家所有的道路。
你作为马军的指挥官啊，急需要指挥军队修建新的道路，其中，你需要遵守以下的规则：

1. 因为高危山脉的缘故，你只能在原来联通的城市之间修建道路
2. 你必须建造充足的道路，使得原来可以互相到达的两座城市，在新的道路网中也是联通的。
3. 你所新建的道路的长度总和必须最小

用区域这个名词来表示所有可以通过新的道路网与其它城市连接的城市的结合。找到所有的可以在渐进时间类生成的区域。

（Prof.Chen 你的题很多敏感词汇啊）



###输入###

从cin读取输入（不过，翻译者劝告各位用getchar吧，如果用cin你的代码超时的可能性很大）。
输入中包括如下三个部分：

1.城市的数目，假设n个，整数类型。（单独一行）
2.原来的道路的数目，假设m个，整数类型。（单独一行）
3.原来的道路组成的序列。其中，原来的道路由两个部分组成，它所连接的两个城市（以城市的代号，从0到n-1），和它自己的长度。都是整数类型。（每条路一行）（中间由空格和‘\t’隔开）

	Prof 陈 在这里 给的 是 用 扩展巴科斯范式表示的输入
	为了方便各位读者的阅读，翻译的家伙直接给出来正式的input。

[扩展巴科斯范式](https://zh.wikipedia.org/wiki/%E6%89%A9%E5%B1%95%E5%B7%B4%E7%A7%91%E6%96%AF%E8%8C%83%E5%BC%8F)

举个例子：4个城市，3条路(长度分别位 3,4,5)

		4
		3
		0 1 3
		1 2 4
		2 3 5


###输出###
用<a src="https://en.wikipedia.org/wiki/JSON">json</a>格式输出，json格式一种使用很普遍的信息传输格式。

<ul>
<li>在第一行的开始，打印出<br>
<code>[</code>
</li>
<li>对每个区域，依（城市序号）降序打出次区域内的城市。

具体来说，对每个区域
<ul>
<li>在第一行的开始，打印出<br>
<code>[</code>
</li>
<li>然后，按照长度的降序打出新建的路，每条路一行.  对每条路。按照序号小的城市先打出的规则，打出两端的城市 。as in the following example:<br>
  <code>[0 10 20]</code><br>
 除非是最后一条路 <code>,</code> 在打出<code>]</code> 马上打出<b>,</b>
</li>
<li>在最后一行打出<br>
  <code>]</code><br>
除非是最后一个区域<code>,</code> 马上在 <code>]</code> 后（同一行）打出 ,
</ul></li> 
<li>最后一行<br>
<code>]</code>
</li>
</ul>

####来自翻译者的补充####
json格式是一个嵌套格式，形如

		[
		command1,
		command2,
		command3
		]

其中的command可以一个json结构，也可以是普通的语句。

####INPUT的例子的OUTPUT####
		[
		[
		[2,3,5],
		[1,2,4],
		[0,1,2]
		]
		]

**更多的例子在[这里](haha.html)**


##积分相等时决胜法##
当两条路，比方说e1=(s1, t1) and e2=(s2, t2) ,有着相同的长度时，当且仅当满足下面的条件时，我们认为，e1比e2短

		1. min(s1,t1) < min(s2,t2)  或者

		2. min(s1,t1) == min(s2, t2) 和 max(s1,t1) < max(s2,t2)

**注意**：s 和 t 在这 代表的是 城市


同理可得，如果是两块区域，比如说是r1={...} and r2={...}，有着相同的城市数目，满足下面的条件时我们认为r1有着r2少的城市
		
		min(r1) < min(r2)

**注意**：
		
		min(s)返回的是s的最小成员

**注解**:
		
		regions are disjoint sets of citie

##将输出结果形象化##
为了方便同学们debug，Prof.Chen 写了一个工具 [json2dot](http://shtech.org/course/ds/homework/3/json2dot) 将输出转化为dot文件[源代码](http://shtech.org/course/ds/homework/3/json2dot.go)

1. 		
		json2dot < program_output > foo.dot
2. 		
		dot -Tps -o foo.ps foo.dot

如果你不能执行，那么是因为你没有装graphviz，装一个。
		sudo apt-get install graphviz

**翻译者的注释**

为了更加的方便同学们的debug，我提供了了一个在线将输出文件转化为jpg，并在网页上显示的工具，[点击这里](haha.html)，开始使用。


##对于资源的限定##

gradebot的服务器，将对程序的资源进行限定，如果超过限定的程序将被杀死。

可以通过下面的命令来测试你的程序是否超时

		bash -c 'ulimit -c 0 -d 500000 -f 100000 -m 100000 -n 50 -s 50000 -t 60 -v 500000; spantree < input_file > output_file'

	如果你的代码超时了，你会看到它被干掉了

如果你想了解更多的关于 ulimit的资料，点[这里](http://ss64.com/bash/ulimit.html)

**如果你是Zsh或其它，点击[Shell Builtin Commands](http://bolyai.cs.elte.hu/zsh-manual/zsh_17.html)获得帮助。**

同样地，我们提供了在线的查看是否超时的，在线工具，并且我们可以给出程序在不同的部分的具体时间与资源消耗。[Click me](haha.html)</a>

##提示##

1. 你有可能需要自己实现 disjoint sets, min head , minimum spanning trees,和一个复杂度是 O(n log n) sorting algorithm (e.g., Heap Sort)
2. 使用g++编译的时候，添加参数 -O3 可以 提高你的程序的性能
		
		g++ -o spantree spantree.cpp 

替换为

		g++ -O3 -o spantree spantree.cpp 

[这里有个理由](http://blog.csdn.net/lanmanck/article/details/5776173)

<hr>
	<p align="center">&copy Dengqi @2015</p>