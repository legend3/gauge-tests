——Specifications (spec)
一个Specification是业务测试用例，描述了需要测试的应用程序的特定功能。
Gauge specifications支持.spec或.md文件格式，并且这些specifications以类似于Markdown的语法编写。

——Specs目录
创建并初始化Gauge项目时，会在<project_root>中自动创建一个带有示例文件example.spec的specs目录。
此样本文件可帮助您了解如何编写Specification。
可以通过使用项目的env\default\default.properties文件中的键值对来更改specs目录的路径和名称,gauge_specs_dir = "xxx"。

——Specification的组成部分
Specification由不同部分组成。
其中一些是强制性的，而很少是可选的。
Specification的组件如下所示：
    Specification heading
    Scenario
    Step
    Parameters
    Tags
    Comments



# Specification Heading
这是一个可执行的Specification文件，该文件遵循markdown语法，该文件中的每个标题都代表一个方案，每个项目符号都代表一个步骤。
要执行此Specification，请运行：gauge run specs

——Concepts
concept提供了将可重复使用的逻辑步骤组合并为一个单元的能力。
一个concept通过组合step的逻辑组来呈现业务意图的摘要*
concept遵循使用Specification中的步骤所需的相同规则或准则。
Specification中可以使用多个concept，也可以嵌套concept！
运行Specification时，所有concept及其步骤均按定义的顺序执行

concept的定义：
    concept以.cpt文件格式在<project_root>/specs中定义，其中<project_root>是创建Gauge项目的位置。
    concept也可以位于specs目录内的嵌套目录内。
    可以从一个concept定义中调用多个concept定义。concept定义由concept标题和concept步骤组成。

使用concept步骤的方式类似于使用Specification中的step，这些遵循concept头。
如果从concept-head使用参数，则必须用<>括起来这些参数。concept-step中的参数也可以具有静态值，该值用双引号“”编写！！！


* Vowels in English language are "aeiou".
"setup"：
这些Context step使您可以指定执行Specification中的方案所需的一组条件。
如果存在多个Scenario，则Context step将在Specification中的每个Scenario之前执行。
Context step必须以*开头，并按定义的顺序执行。

## Vowel counts in single word
每个Scenario代表特定Specification中的单个工作流程,Specification必须包含至少一个Scenario。
Scenario在Scenario标题或Scenario名称之后开始。
用Markdown <H2>语法以下列方式之一编写Scenario标题

tags: single word
用于标记（"取个别名"）相关联specifications或scenario,tag有助于搜索或过滤Specification或Scenario。
只能将一组tag添加到单个Specification或scenario中。
Specification和Scenario可以存在多行tag(当使用的标签数量更多时，可以在多行中定义标签以增强可读性),多行写入时，标签必须缩进。
应用于Specification的tag也将自动应用于scenario


* The word "gauge" has "3" vowels.
scenario中包含一个或多个step
双引号括起来的是将被传入step实现代码中的参数
以下字符保留用于参数，不能在step文本中使用：
”
<
>
根据安装Gauge时所使用的语言插件，每个step的实现都有一个等效的代码!!!
执行specifications中的step时运行此(等效)代码


## Vowel counts in multiple word

这是这个specification中的第二个scenario

Here's a step that takes a table
Gauge >= 1.0.3添加了一项实验功能，以提供scenario级别的表格
Gauge将遍历表并针对每一行运行该特定scenario。

在/env/default/default.properties中将allow_scenario_datatable变量设置为true以启用此功能
由于这是一项实验性功能，因此目前有些无法使用的情况：
    (对应使用的)IDE插件不支持此功能。
    CSV文件不能用作scenario的表。
    (对应使用的)报告插件不支持此功能。

* Almost all words have vowels
     |Word  |Vowel Count|
     |------|-----------|
     |Gauge |3          |
     |Mingle|2          |
     |Snap  |1          |
     |GoCD  |1          |
     |Rhythm|0          |
     

## Step with table
当步骤将内联表作为参数时，步骤实现必须具有适当("hobbit"、"table")的参数。
* Create following "hobbit" characters
  |id |name   | 
  |---|-------|
  |123|frodo  |
  |456|bilbo  |
  |789|samwise|


## Multiple Users
当一个复合step中的某个参数是为同一个功能性的各step使用时，（一个）实现方法可通过参数列表实现各(使用此参数)step。
* Create a user "user1"
* Create another user "user2"

## User Creation
在两种情况下发送电子邮件的功场景是相同的。但是，步骤的表达方式有所不同。——welcome
* A "welcome" email is sent to the user

## Shopping Cart
在两种情况下发送电子邮件的功场景是相同的。但是，步骤的表达方式有所不同。——order
* An email confirming the "order" is sent


## Vowel counts in singleword
* The word "gauge" has "3" vowels
使用gauge refactor命令重构step与step实现,命令执行：gauge refactor "The word <word> has <number> vowels" "The word <word> has <number> vowels and \"2\"" consonants"




____________________
"Teardown":

* Logout user "mike"
* Delete user "mike"

