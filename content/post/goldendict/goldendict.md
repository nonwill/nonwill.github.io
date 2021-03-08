---
title: "GoldenDict++OCR 「划词版」"
date: 2019-03-03T00:20:53+08:00
draft: false
tags: ['GoldenDict','OCR',划词]
categories: [辞书,学习,划词,Qt]
---
{{< notice tip Built-in-OCR.Stable.Efficient.鼠标划词.稳定极速 >}}
![ocr划词](https://s3.ax1x.com/2020/11/12/BvhzOP.gif) 
Demos·演示: [OCR·划词](https://www.bilibili.com/video/av96718018/)  [macOS](https://www.bilibili.com/video/bv1b54y1d7SU)  [Starting·启动](https://www.bilibili.com/video/BV1CK411W7Du/)  [Gif·动画](https://s1.ax1x.com/2020/04/18/Jn3Um9.gif)  
***Greetings to [GoldenDict](http://www.goldendict.org/)**, features special*：
* **并发索引**辞书**加速启动**，信息全程可视
* **全文搜索**结果可**导入导出**，一次搜索，随时使用
* **功能模块**化，插件**按需加载**，降低内存占用
* 多个**音频引擎**插件，**随切随用**
* 多引擎**OCR划词**，支持**自动切屏**、**动态划屏**
* **依辞书根目录**的自动群组，**一键分组**
* 文章切换，**恢复**群组/关键字/候选词等**上下文信息**
* 增强的**阅读模式**，沉浸于**边阅边查**的读书体验
* **全局js脚本**，给您自主**优化查询性能**的空间
* 支持**字典别名**，支持**按目录+文件名排序**辞书
* 优化**mdx**格式，支持**flash**播放和**tif格式**图片
* 文章历史总量可控，**低配电脑也能顺畅运行**
* **全优化**，**加速查询**，解决内存泄露、崩溃等问题  

This is **improved** build over the **[official](https://github.com/goldendict/goldendict)**. If you find it useful, please consider [donating to help maintain it](https://paypal.me/nullwill?locale.x=zh_XC).「如本程序对您有所帮助，请考虑[捐赠以帮助维护她](/donate/)，您的支持将予我以动力」  
{{< /notice >}}
 
{{< notice note Deployment.安装部署 >}}
声明：GoldenDict++OCR划词版不以任何售卖形式分发，仅在**非盈利**、**非商用**及**帮学助教**的前提下您可以下载**使用与分享**本程序；下载或使用本程序将视同您已知晓并同意本声明所示内容。
#### Last updated date: ***4 March 2021***
1. Download a **Package** from the following links「按需选取并下载**程序包**」
* [md5](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/checksum.md5) [sha256](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/checksum.sha256) [Dictionary](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/Dictionary.tar.bz2)「校验码，共享的辞书、样式表和字体文件」  
* [macOS 64-bit: Qt 5.9.9, no 32-bit support, OS X 10.13 High Sierra or later recommended](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/GoldenDict++OCR-2A27-macOS-10.13.6-x64-20210223.dmg)「适用于macOS 10.13 High Sierra及与之兼容的macOS系统」  
* [Linux 64-bit: Qt 5.15.2, Portable build, Manjaro 20.1 x64 or later recommended](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/GoldenDict++OCR-2A26-manjaro-20.1-x64-20210223.tar.gz)「适用于64位Manjaro 20.1及与之兼容的Linux系统」  
* [Linux 64-bit: Qt 4.8.7, Portable build, Debian 10.8 x64 or later recommended](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/GoldenDict++OCR-2A26-debian-10.8-x64-20210223.tar.gz)「适用于64位Debian 10.8及与之兼容的Linux系统」  
* [Windows 64-bit: Qt 5.9.9, msvc2019, Portable build, Windows 7 sp1 x64 or later recommended](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/GoldenDict++OCR-2A26-Qt-5.9.9-msvc-16.8.5-x64-20210223.tar.bz2)「适用于Windows 7 sp1 x64及以上版本」  
* [Windows 32-bit: Qt 5.9.9, mingw32-gcc10, Portable build, Windows 7 sp1 or later recommended](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/GoldenDict++OCR-2A26-Qt-5.9.9-mingw-gcc10-x86-20210223.tar.bz2)「适用于Windows 7 sp1及以上版本」  
* [Windows 32-bit: Qt 4.8.7, msvc2019, Portable build, Windows 7 sp1 or later recommended](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/GoldenDict++OCR-2A26-Qt-4.8.7-msvc-16.8.5-x86-20210223.tar.bz2)「适用于Windows 7 sp1及以上版本」  

2. Install or unpack the **Package**: macOS --- just pick up GoldenDict(.app), Linux --- start a terminal and execute goldendict from the dir where GoldenDict is in, Windows --- double click on GoldenDict(.exe) 「安装或解压**程序包**：macOS系统直接执行GoldenDict(.app)，Linux版本需要通过终端执行GoldenDict同目录下的goldendict脚本文件，Windows中执行解压出的GoldenDict(.exe)」

3. Optional:  If you need OCR supporting other languages, extra language-pack of the ocr-engine is needed and the data-path which is used by ocr-engine for loading language data should be reset to your language-pack dir --- download and unpack the following package, open GoldenDIct's **Preference** dialog and swich to **OCR Popup**, select an OCR-Engine and set the data path by clicking the button next to the Engines' List, then select module language(s) for the engine 「可选：如需OCR支持其它语言，请下载下列OCR支持库，解压后到**首选项**对话框的**划词**页，针对OCR引擎重设其识别库目录后选择需要识别的语言」
* [**Nicomsoft** OCR](https://www.nicomsoft.com/) Full (84 MB)  [x64](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/ns_ocr_x64.7z) or [x86](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/ns_ocr_x86.7z), only supports Windows.  
* [Google **Tessdata Fast**](https://github.com/nonwill/nwDeployed/releases/download/GoldenDict%2B%2BOCR_2A26_20210223/tessdata_fast.7z) (273 MB), or others from the [Official](https://github.com/tesseract-ocr).

This is **FULL** distribution with all required files, libraries(includes QT libs) and localizations except that VC redist [x64](https://aka.ms/vs/16/release/vc_redist.x64.exe) or [x86](https://aka.ms/vs/16/release/vc_redist.x86.exe) is required by [msvc2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) versions and should be installed first. If [GitHub](https://github.com/nonwill/nwDeployed/releases) is not accessible, all the packages are available at [OneDrive](https://1drv.ms/u/s!AllBS8YFxXjJbFGwCu3UQ6k4Ft4?e=4d8nbd) or [Baidu Netdisk(:ranu)](https://pan.baidu.com/s/1cFY0CHnezl7AoYewrie_pg) 「除[msvc2019版](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)需先下载并安装运行时库[x64](https://aka.ms/vs/16/release/vc_redist.x64.exe)或[x86](https://aka.ms/vs/16/release/vc_redist.x86.exe)外，发行包中已含运行GoldenDict++划词版所需的文件。如果不能访问[GitHub](https://github.com/nonwill/nwDeployed/releases)，请从[微软云](https://1drv.ms/u/s!AllBS8YFxXjJbFGwCu3UQ6k4Ft4?e=4d8nbd)或[百度网盘(:ranu)](https://pan.baidu.com/s/1cFY0CHnezl7AoYewrie_pg)下载。另，鉴于部分资源分享站点有改包并可能添加私有程序/功能的行为，不建议从类似网站下载划词版的程序文件；如发现任何以收费或附赠形式分发GoldenDict++OCR划词版程序文件的行为，请通过[邮件](mailto:nonwill@hotmail.com)告知于我，谢谢」
{{< /notice >}}
{{< notice warning Notice.问题 >}}
#### 0. 划词版相关的bug或改进建议请[点此反馈](mailto:nonwill@hotmail.com)（主题中备注**GD改进**）
>与官版同有的bug请尽可能的提交[issue](https://github.com/goldendict/goldendict/issues)，严重问题会及时的在划词版中予以修正。
#### A. 日常使用
>**首先**快速浏览本文中的**更新日志**来了解划词版，**其次**尽可能的查阅**帮助文档**和相关论坛已有的**主题贴或网文资源**，**然后**尝试在**相关论坛发帖求助**，**最后**浏览或查询[官版issue列表](https://github.com/goldendict/goldendict/issues)亦可了解一些使用方法或禁忌，但请**勿以邮件形式就此类特别是mdx词典相关**问题与我咨询；如您有整理好的使用攻略或方法，欢迎将相关内容（或网文链接）通过[邮件](mailto:nonwill@hotmail.com)（主题中备注**GD攻略**）发送给我，适时整理后可补充到本文内容中去。
1. 强烈推荐[安装使用GoldenDict查词神器](https://keatonlao.gitee.io/use-goldendict/) --- 文章大，内容全，阅后无论是一般使用还是奇淫技巧，您对GoldenDict都将刮目相看。 ------ 感谢 [keatonlao](https://gitee.com/keatonlao)
2. macOS中开启划词和热键取词功能需要系统支持，请到 [系统偏好设置-->安全性与隐私-->辅助功能](https://github.com/goldendict/goldendict/issues/1333#issuecomment-783853905)，添加GoldenDict.app：
>![yqVqr4.png](https://s3.ax1x.com/2021/02/23/yqVqr4.png)
#### B. 从低版本升级或全新部署：
1. 遇到程序闪退及ocr划词或音频播放问题，请检查核对（或重新选择）ocr划词和音频引擎（如还不能解决问题，请备份并删除配置目录下的config.nwx再试）。
2. 如为全新部署则解压可用，升级安装请：
 * 备份好运行目录或安装目录下的配置文件（portable目录，content文件夹等）；
 * 删除运行目录下的所有程序文件；
 * 解压整包中的所有文件到运行目录下；
 * 还原配置文件到原来的位置；
 * 启用程序并修改配置参数。
3. 创建索引失败（index）的问题，请确保配置文件目录下存在index文件夹，没有则新建一个。
4. 最新Windows版本即使关闭“随系统启动”选项，开机还是自启动的问题：
>新版使用名称为GoldenDict++（老版和官版为GoldenDict），请删除注册表项中的"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"路径下的GoldenDict项**或**运行旧版或官版并在其首选项中取消勾选“随系统启动”确定后退出程序**或**任务管理器的启动页面在GoldenDict条鼠标右键禁用即可。
#### C. 从官方版本切换到划词版：
* 配置文件：官版为config，划词版为**config.nwx**且不兼容官版，但都是xml文件，如动手能力强 --- 简单**正则提取替换**即可将**分组参数迁移到划词版**（如您习惯于条理有序，请用**创建基于目录(根)的群组**功能）。
* 收藏记录文件：官版为favorites，划词版为favorites.nwx且已不再兼容官版格式，但都是xml文件，简单的**修改文件名 --- 加后缀\.nwx并对文件内容进行文本替换**即可将文件格式从官版迁移到划词版。
* 历史记录文件：官版为history，划词版为history.nwx且格式未变，简单的**修改文件名 --- 加后缀\.nwx**即可。
* 用户级**总**样式表文件：官版允许放置在配置目录下（qt-style.css和article-style.css），划词版必须放置到**配置目录的styles文件夹下**。
* **用户级js脚本文件**：划词版独有，文件名为**user.gjs**，且必须放置到配置目录下。
{{< /notice >}}
<!---
{{< notice tip Donate.支持.打赏 >}}
If you find GoldenDict++OCR useful, you are welcome to [contribute by **donating💖**](/donate/).  
如果我的劳动对您有所帮助，您的[支持与赞助将**予我以动力💖**](/donate/)。  
{{< /notice >}}
--->
{{< notice info Logs.更新日志 >}}
##### 2021.3.9 2A27：为portable模式开放对音频文件目录的支持，索引文件存放在对应目录下。
##### 2021.3.8 2A27：Fix around [issue](https://github.com/goldendict/goldendict/issues/1359): Add minimize and maximize buttons on titlebar of EditDictionaries' dialog。
##### 2021.3.4 2A27：划屏可选静态截图（使用外置工具，命令行：wingraber）；更稳妥的方式解决macOS中退出时可能发生的崩溃问题。
##### 2021.2.22 2A26：优化日志接口，优化网络资源类词典的日志输出，重新使能--log-to-file日志输出功能；修正查询结果中存在dict server词典但（因匹配不到词条）文章无内容的问题；2021.2.20 2A26：解决macOS中通过Dock栏右键退出时可能发生的崩溃问题；修正从查询工具栏切换到查询面板后查词（匹配）导致程序崩溃的问题；重构Popup窗口使其更方便于快捷查询操作：
>工具栏使用Toolbar组织 --- 紧凑布局以缩减屏占空间；pin状态不再显示标题栏以避免无用的屏占空间；非pin状态可调整大小；工具栏左侧pin按钮，最左侧关闭按钮，最右侧显隐词典栏按钮；工具栏中的标题区域可按下鼠标移动以改变窗体位置；词典栏强制右侧竖排显示且默认隐藏以缩减屏占空间；弹出窗口时鼠标尽可能的指向关闭按钮以便于快速隐藏窗体。
>![pin and ontop](https://s3.ax1x.com/2021/02/20/y4zb0s.png)
##### 2021.2.16 2A25：工具栏样式调整；增加对zim格式词典source标签的poster属性的转换处理；为Qt4版本增加对webp、wbmp图形格式的支持；[DSL: Fix resource loading in some cases](https://github.com/goldendict/goldendict/commit/72dfe25ff38356b7dbe564815d1051ac5abb8d17) by Abs62，同时避免（当词典后缀不包含.dz时）同一路径被测用两次的问题；[DSL: Don't convert escaped spaces into non-breakable inside \[s\] tag](https://github.com/goldendict/goldendict/commit/7db077bd0310ceb42e836f8721a3fddf9144e1b3) by Abs62；修正弹窗查询输入框样式违和（macOS下尤为明显）的问题；portable模式下构词法可以放置到content目录下；在首选项对话框中为触屏手势增加开关选项。
##### 2021.2.7 2A23：修正弹窗首次查询所使用的词典未过滤掉已分组中被排除的词典的问题；修正主窗和弹窗使用相同的词典分组在主窗使用阅读模式查词时，主窗分组被排除而弹窗分组未被排除的词典不被查询的问题（确保阅读模式下两个分组中未被排除的词典都参与查询）；调整阅读模式下弹窗查得的文章顺寻（打开链接：主窗当前词典+弹窗分组词典+主窗分组其它词典；普通查询：弹窗分组词典+主窗分组词典）；确保索引目录存在（尽可能的避免程序启动或扫描词典文件时报Can't use index directory to store GoldenDict index files及未生成索引文件的问题）。
##### 2021.1.28 2A22：解决zim格式打包的最新wiki词典文件信息的语言不被解析识别的问题（更新语言代码兼容ISO 639-2/3/5）；修正zim文章内的部分链接跳转无效（查询失败）的问题；修正含有某些符号（如%、?、\&等）的词头查询不到的问题；更快速更安全的读取索引数据，查询效能显著提升；辞书词条对话框：紧凑布局，加速访问同时解决词条过多时导致界面卡死的问题，加速过滤条件改变后的列表刷新；修正词典枚举过程中stack overflow导致程序异常退出的问题（在程序启动或重新扫描文件时偶尔出现）；增加.gdignored魔法（扫描词典或索引时忽略目录）；解决部分dsl格式词典文件信息的语言不被解析识别的问题；进一步完善语言判据及匹配逻辑（更好的支持语言全称或别称匹配语言代码）。
>.gdignored：当有大量的资源文件（数量(百)万计）存在于资源文件夹中，但这个文件夹下没有任何词典文件却在扫描目录的设定范围内，启动GoldenDict或扫描词典文件时，会在这个文件夹下耗费数十秒至数分钟。当目录中存在.gdignored文件时，该目录的所有子目录在扫描时将被忽略，可以有效的提升索引效能。
>占个坑：对语言判据信息使用自定义配置文件，来存放ISO 639-2/3/5相关的代码定义信息及对应的语言旗标，ocr也用这些个功能，需独立出来封装个库文件。
##### 2021.1.20 2A21：修正zim格式解析src和href存在的问题，合并link的href与image、script等的src处理以提升效率；修正在词典编辑对话框中重新扫描词典后顺序调整及分组编辑的右键菜单功能失效的问题；为portable模式开放对自定义词典目录的支持，在对应目录下创建.gdindex目录来存放该目录（包括其子目录）下的所有词典的索引文件；划词设置界面调整；简化网络管理器对数据接收状态的转收（冗余）处理；bgl词典索引和查询处理的细节优化以提升能效；针对aar、bgl、dsl、zim、slob、sdict、xdxf、dictd、stardict、dict_server格式（无外置样式表）：统一处理词头和文档标签以便于样式的一致设定：
>使用全局标准的css样式：定义并使用了.gd\_headword和.gd\_body全局类，对于xdxf、zim、slob、dictd、aard格式不添加额外的gd\_headword。
##### 2021.1.14 2A20：修正Qt5WebKit不显示tif格式图片的问题（在GoldenDict中无需再做额外的格式转换且不再直接依赖libtiff等库文件）；修正历史记录和收藏记录中的非英文词条可能乱码的问题；为分组编辑的操作按钮增加图标；收藏菜单中的添加菜单项的图标和文字状态与工具栏的收藏按钮的图标和文字状态保持一致；优化文章tab页标签的右键菜单及其行为：
>当右键点击到非当前文章页面的标签（简称**点选文章**）时，弹出菜单项的**关闭当前页面**描述变更为**关闭页面**，其行为由**关闭当前文章**变更为**关闭点选文章**，**关闭其它标签页**的行为由**关闭当前文章除外**的所有文章变更为**关闭点选文章除外**的所有文章。
##### 2020.12.28 2A1F：为音频播放增加停止功能。
>点击工具栏的**朗读词条**按钮：当前有音频正在播放时，则停止播放，否则执行词条朗读功能。鉴于词条朗读一般情况下时长较短，忽略增加停播后的恢复播放功能的需求。
##### 2020.12.20 2A1E：修正多屏时，在非主屏上划词或取词的Popup窗口位置问题（确保Popup窗体出现在鼠标所在的屏幕上），及在非主屏上划词幕布可能出现不会铺满屏幕的问题；修正主窗口最大化后，从最大化状态恢复时窗体位置错误的问题。
##### 2020.12.18 2A1D：Qt5(.9.9): Backport common\&important fixes from source-branch of Qt-5.15，and other Security\&Stability Updates with qtbase modules.
##### 2020.12.14 2A1C：Qt5(.9.9): Backport common\&important fixes from source-branch of Qt-5.12，3rdParty updated to newest，unicode CLDR(Common Locale Data Repository) updated to v35.1，network module now supports openssl-1.1\&dtls and new feathers，and other Security\&Stability Updates with qtbase modules.
>Qt5(.9.9) will be long supported until [QTBUG-87774](https://bugreports.qt.io/browse/QTBUG-87774) is fixed for that Qt(Version>=5.12) leads to serious memory leaks.  
>For Security\&Stability\&Speed, Webkit is now extra feathered with css3 text, css3 text-line-break, mathml, xslt, netscape-plugin-api, modules, custom elements, custom scheme handle, no accelerated-2d canvas, no geolocation, no quota, no media source, no media capture, and no video --- but embed video with flashplayer is still supported.
##### 2020.12.9 2A1B：Qt4: Backport some common\&important fixes(CVE-2013-4549, CVE-2015-0295, CVE-2015-1860, CVE-2015-1859, CVE-2015-1858, CVE-2016-1004, CVE-2018-19872, CVE-2020-17507...) from Fedora Review。
##### 2020.12.8 2A1A：修正缩放比例不为1时作为链接的网站（Web）类型辞书的页面内容（显示）高度错误的问题；修正文章视图中水平滑动条与垂直滑动条样式表不一致的问题；修正Qt4版本关于对话框中版本信息中文乱码的问题；修正全新部署（或升级前未删除旧的参数文件）参数的默认值可能不生效的问题，修正因部署目录变动导致的ocr、划屏和音频引擎失效而必须在首选项对话框中重新配置的问题（2A18引入）。
>无需重置配置文件既可从旧版本无缝顺滑的升级到新版本啦；配置文件中仅保存插件文件名 --- 程序从与其同目录的gdp文件夹下寻找并加载同名插件；针对OCR的数据目录设置，如果目录不再存在或没有手动重置过，则默认从程序所在目录下的tessdata或nsocr文件夹加载语言识别文件。
##### 2020.11.28 2A19：优化辞书列表的刷新机制（提交查询后秒内如页面未完成加载（渲染）则主动更新辞书列表，辞书列表做到秒出）；修正因开发语言多态特性使用不当引发的多处内存泄露问题；修正索引文件创建后文件的写缓存可能不被释放（内存泄露）的问题；优化一处创建索引文件时影响性能的实现；修正词头（索引关键字）超过特定长度（默认256）时查询不到对应记录的问题。
>一本离线辞书中，关键字（长度）超256个字符的记录应该不多，即便有较多的存在，这种情况下以前256个字符做索引关键字，关键字相同的概率应该也是较小的 --- 即便有冲突比着野蛮的丢弃以至无法查询到对应词头的内容的影响也是好的。  
##### 2020.11.22 2A18：修正Linux版本缺失tts引擎相关动态库的问题；Windows版本删除原版中带有的取词功能（这个功能模块使用的技术容易被杀毒软件报毒 --- 详细原因见前述）；优化辞书索引和全文索引处理；规范Web和辞书（epwing和mdx）缓存目录以便于管理；为mdx格式辞书提速 --- 优化查询处理，优化重复访问含有视频内容的词条的访问处理（避免重复刷新缓存文件）；为Qt4版本mdx增加视频支持；对频繁访问的网络资源进行加速 --- 使用缓存（[参考](https://github.com/goldendict/goldendict/pull/1310)）；字符转码效率优化（类xml辞书内容加载到xml文档中既已转码成utf8，无需再次强制转换）；修正在DictionaryBar上快速频繁的点击辞书标签时导致程序崩溃的问题（重构程序类型辞书的查询处理，优化Wiki和Web辞书的处理）；修正在词条列表匹配结束前关闭（退出）程序，会导致程序崩溃的问题；修正收藏夹中的文件夹的展开或收起状态可能不被保存的问题；修正打开首选项对话框然后点击取消按钮或直接关闭对话框后音频引擎失效的问题。
##### 2020.11.15 2A17：优化多处严重影响查询性能的实现；仅在辞书有编辑后刷新所有文章，在扫描辞书文件后仅刷新当前文章；优化收藏列表和历史列表，减少运行时内存占用，在其中 鼠标右键（ 目的是弹出右键菜单而非查词）点中条目时不执行查询操作；增强收藏按钮与收藏列表的联动 --- 从列表删除当前页面的单词时会同步更新收藏按钮的状态，查询单词是否已被收藏时不区分大小写（修正[issue](https://github.com/goldendict/goldendict/issues/1312)），收藏按钮状态变化时同步更新按钮文字以反映其真实状态（修正tab页标签右键菜单中收藏项文字失实的问题）；优化以提升页面资源下载的处理速度， 修正访问Web资源可能引发的内存泄漏问题；重构辞书分组属性编辑功能（修正打开辞书编辑对话框时卡顿及切换到分组页面时程序可能崩掉的问题 --- 分组越多问题越易出现）；修正在程序启动时程序崩掉的问题（极端情况，极少出现）；修正在查询面板和查询工具栏间切换时可能导致程序崩掉的问题（有Web及Wiki类型辞书时易出现）。
##### 2020.11.10 2A16：Fix around [quote possible apostrophe](https://github.com/goldendict/goldendict/pull/1303/commits/63aeb0ef6dbe5c482fba92360e297f51389111f3)，and quotes also need an escape；修正网页审查员不能唤起和置为当前窗口的问题；Qt4版本：修正开着 网页审查员 窗口关闭查词页面导致程序崩掉的问题。
##### 2020.10.29 2A15：Qt4版本：去除bgl辞书的多余换行以优化显示效果，整合字体设置以支持音标等特殊字符的显示（辞书样例:En-En-Longman_Pronunciation_3rd_Ed.dsl），修正Epwing辞书加载失败的问题，修正右键 审查元素 导致程序崩溃的问题，修正开启鼠标取词导致程序崩溃的问题，修正读取xdxf辞书名称错误的问题，修正 收起文章 和 展开文章 图标全黑的问题，增加PhononPlayer音频引擎，修正不支持非全英文路径名称的问题（扫描不到非全英文路径下的字典文件），修正欢迎页面乱码的问题，修正Splash窗体背景虚黑（不透明）的问题；启用Qt4的directwrite支持。Qt5版本回退使用Qt-5.9.9（该版本界面工具栏无不可逆的内存泄露）；修正DictionaryBar的内存泄露（mingw+gcc版完全有效，[Qt-5.12和Qt-5.15待Qt官方修正](https://bugreports.qt.io/browse/QTBUG-87774)）。
##### 2020.10.21 2A14：通过传递屏幕dpi参数值来提高ocr识别的精度；实现截图与ocr功能分离（增强插件可用性及使用的灵活性），增加划屏插件，增加划屏OCR助手，可以配置不同的划屏方案与ocr方案的自由组合 --- 以便于用户实现自己的ocr插件（如腾讯、百度等在线接口的引入）；界面 **大修 | 逻辑优化** ： DictionaryBar中标签高度优化（再也不会因为多国语言的辞书名称而导致的工具栏忽高忽低了）；优化辞书群组列表、候选词列表、搜索框文字和Tab页切换的联动实现（切换Tab页不会丢失其上下文内容）；优化主窗口和Popup窗口的状态栏信息显示，当启用了系统托盘图标且系统支持托盘通知在主界面不可视时将状态信息输出至系统托盘；尽可能早的在界面初始化结束前启动辞书扫描加载工作，提高了程序启动时的速度和稳定性。
##### 2020.10.11 2A13：增加配置选项来设置主窗口查询页面和Pop窗口的最大历史记录数量（影响回退和前进），以限制在低配置硬件上的内存占用 --- 最大数量限定为255，值为0时则不使用历史记录，内存占用最小；优化 Linux/Unix系统划词体验 --- 使用scrot截图和xclip传递图形数据（体验跟macOS基本一致，速度上亦有保证），windows系统仍使用内置截图（更换了鼠标样式）；提升UCS-4转utf8字符串的效率；辞书群组编辑自动生成分组时保持当前分组页面；优化辞书加载流程（在并发线程中执行针对dsl和mdx等格式辞书的自定义初始化处理，在程序启动时不中断并代理gui线程的事件处理）；修正重新扫描文件操作后搜索框失去输入焦点的问题；tesseract划词ocr引擎增加对SSE、AVX的检测支持。
>划词依赖：macOS系统需要screencapture（系统内置）并启用剪切板访问权限；Unix/Linux系统需先安装scrot和xclip：  
>  Debian：apt-get install scrot xclip  
>  Fedora：yum install scrot xclip  
>  Arch：pacman -S scrot xclip 
##### 2020.9.29 2A12：优化下拉复选列表（QComboCheckBox），限定选中状态的改变仅在选择框范围内点选时有效，修正下拉列表不能收起的问题，优化ocr识别语言配置；去除了aard、epwing、xdxf格式辞书查询的关键字的h3显示（样式不可控，有点儿违和）；修正辞书生成的html页面源码css中错误的属性值；优化内置的主题样式表；简化用户样式表及脚本访问接口，并将用户自定义样式表限制在配置文件夹下的styles目录下，将针对金山数据的stardict辞书的样式映射文件sdct_k.style设置到用户styles目录下；解决xdxf及sdct_x格式辞书def层级显示错乱及生成多余（多一个）\<br /\>的问题，修整xdxf预定义css --- 显示更美观了；清除aar格式辞书中的多余换行符；解决在辞书分组设置界面从分组删除多个辞书可能导致程序崩溃的问题；设置在流 I/O 级别同时打开的最大文件数8192（支持管理更多的辞书，如操作系统不支持则改为2048）；为linux版本增加tts引擎支持；解决在不同分辨率的显示器间切换时窗口可能显示在屏幕区域以外的问题；增加阅读模式。
>通过ocr识别语言下拉框，选择区域则该区域下所有选中状态的语言都参与ocr识别，选择某一语言（不一定要在选中状态）则仅该语言参与ocr识别，如所有区域中都没有被选中的语言，则使用英文识别。  
>使能阅读模式后，文章（查询结果）页面，右键菜单增加 在悬浮窗中打开链接 和 在悬浮窗中查询... 项，鼠标中键点击链接、鼠标选择内容后右键查询，按住功能键（Ctrl或Shift）的同时鼠标双击翻译词条或鼠标单击页面链接，将使用 悬浮窗口 显示查询结果；该模式下的查词使用**联合辞书分组**（悬浮窗使用的辞书组+主窗口当前文章（查询结果）页面的辞书组）查询。  
>加载样式表的顺序是：（内建通用样式表  -+> 内建主题样式表） -+> styles目录下的（自定义样式表 -+> 自定义主题目录下的样式表）  
>![xdxf](https://s1.ax1x.com/2020/09/16/wcQVUJ.png)
![xdxf](https://s1.ax1x.com/2020/09/16/wcQZ59.png)
##### 2020.8.30 2A11：解决多语言环境下epwing辞书可能不被识别问题；优化OCR引擎语言列表的加载时机及初始化机制（在识别库目录无效时，不初始化语言列表，不实例化划词引擎，以避免程序崩溃）；优化索引（加载后）所占用的内存，优化辞书图标的处理（大幅降低内存占用）；添加基于辞书目录的自动群组功能：
>以**辞书来源**下的**文件**页面所添加的**辞书文件所在目录**为**基础（根）目录**，以其下级存在字典的子目录（不递归）名自动添加群组，如果基础（根）目录下存在辞书文件，自动添加以基础（根）目录名为名称的群组。
##### 2020.7.7 2A10：音频和ocr引擎适配插件机制；查词结果的标签页（View）绑定辞书群组 --- 修改辞书群组仅对当前标签页有效，多个标签页可以使用不同的辞书群组，切换标签页时群组同步切换，在标签页上提示其所使用的辞书群组信息及查询的词条内容；启用对程序自身标签页取词的开关（同 忽略程序自身的选择剪切变更 项）设置。
##### 2020.6.22 2A0F：解决linux下ffmpeg+ao库发音引擎（ao库打开设备失败）的问题；linux系统下取词功能修复，macOS/Windows中取词功能按需挂载Accessibility/注册Hook接口：
>在启用屏幕取词，但未使能取词功能的情况下不加载对应的功能模块 --- 降低了资源占用，在Windows中尽可能的规避了Hook对系统及其它程序的负面影响 --- 见前述。
##### 2020.6.18 2A0E：为ocr引擎设置默认识别库目录；OCR划词功能适配macOS和Linux系统，解决macOS版ffmpeg+ao发音引擎问题，Linux版本添加bass发音引擎；为划词增加Esc按键支持。
>划词过程中的按键：鼠标右键 - 取消划词；待划屏状态(划取屏幕前) Esc按键- 取消划词；划屏过程中(按住鼠标左键未释放) Esc按键- 取消划取范围，释放鼠标左键后恢复待划屏状态。  
在macOS平台上，因为QMediaPlayer的缺陷(无法从内存buf的io设备播放音频内容)，Qt Multimedia引擎播放不了音频，故实际有效的发音引擎只有ffmpeg+ao。  
此为2A0最终版了，在2A0F版本(如有)将仅解决bug，不再做任何功能改进与更新；从2A10版本开始将逐步完成插件化的处理，代码不再与2A0版本兼容。
##### 2020.6.1 2A0D：解决枚举不到自安装的tts引擎的问题；Add Zstd compression support for ZIM format，by [Abs62](https://github.com/goldendict/goldendict/commit/6e85b273377b094e09d0a5a3dbad048cbfb23bd2)。
>关于tts引擎：如果tts组件为32位版本的，则只能为32位版本的程序加载使用，反之，64位的tts引擎组件则只能为64位版本的程序加载使用。  
>ocr划词可以较好的取代鼠标取词，如确实需要，将完全以插件程序的方式实现鼠标取词功能。当前鼠标取词存在的弊端：
> 1. 功能的实现分两部分，既存在于程序内部，又需要一个外挂程序来配合，相对复杂，取词能力还受限(在很多软件中取不到词)；
> 2. 在程序UI(主线程)卡顿时会影响操作系统或其它应用程序的运行，表现为系统相关功能(开始菜单等)或其它应用卡顿或无响应；
> 3. 程序存在获取不到全局鼠标或键盘消息的可能(其它进程Hook处理后未继续传递消息)；
> 4. 因为使用了Hook(监控鼠标键盘及其它应用的内存信息)及共享内存(进程间通信)，会被部分严苛的杀毒软件判定为木马或病毒软件；
> 5. Hook技术影响操作系统运行的稳定性。......
##### 2020.5.8 2A0C：增加对全局js脚本文件的支持:
>需要在配置文件目录下新建 user.gjs 文件，在其中添加javascript代码即可，代码对查词结果页面全局有效（每个辞书都可使用其中定义的变量和方法）。例，可以在 user.gjs 中加入jQuery的代码，这样各个辞书就不需要使用单独的jQuery脚本文件了。对查词结果的内存使用会有一定的影响（降低了内存占用），同时减少了文件io操作，对结果页面的解析效率应该也会有小幅度的提升。
##### 2020.4.5 2A0B：解决全图片辞书mdd中图片读取错乱的bug，by [last_idol](https://forum.freemdict.com/t/topic/1329)；开放trackClipboardChanges设置项（监控剪切版变化取词）；添加Tesseract OCR划词引擎，支持多国家/地区语言的选配。
<!---
>|  Chinese Simplified  | Chinese-Simplified(vertical)  | Chinese-Traditional  | 
|  :--------------  |  :--------------  | :-------------- | 
| Afrikaans | Irish | Norwegian | 
| Amharic | Galician | Occitan(post1500) | 
| Arabic | Greek, Ancient(to1453) | Oriya | 
| Assamese | Gujarati | Panjabi;Punjabi | 
| Azerbaijani | Haitian; HaitianCreole | Polish | 
| Azerbaijani-Cyrilic | Hebrew | Portuguese | 
| Belarusian | Hindi | Pushto;Pashto | 
| Bengali | Croatian | Quechua | 
| Tibetan | Hungarian | Romanian; Moldavian; Moldovan | 
| Bosnian | Armenian | Russian | 
| Breton | Inuktitut | Sanskrit | 
| Bulgarian | Indonesian | Sinhala;Sinhalese | 
| Catalan;Valencian | Icelandic | Slovak | 
| Cebuano | Italian | Slovak-Fraktur | 
| Czech | Italian-Old | Slovenian | 
| Javanese | Sindhi | Japanese(vertical)  |
| Spanish; Castilian | Japanese | Spanish; Castilian-Old | 
| Chinese-Traditional (vertical) | Kannada | Albanian | 
| Cherokee | Georgian | Serbian | 
| Corsican | Georgian-Old | Serbian-Latin | 
| Welsh | Kazakh | Sundanese | 
| Danish | CentralKhmer | Swahili | 
| Danish-Fraktur | Kirghiz; Kyrgyz | Swedish | 
| German | Kurmanji (Kurdish-LatinScript) | Syriac | 
| German-Fraktur | Korean | Tamil | 
| Dhivehi; Divehi; Maldivian | Korean(vertical) | Tatar | 
| Dzongkha | Kurdish(ArabicScript) | Telugu | 
| Greek, Modern(1453-) | Kurdish(ArabicScript) | Tajik | 
| English | Lao | Tagalog | 
| English, Middle(1100-1500) | Latin | Thai | 
| Esperanto | Latvian | Tigrinya | 
| Mathandequations | Lithuanian | Tonga | 
| Estonian | Luxembourgish | Turkish | 
| Basque | Malayalam | Uighur;Uyghur | 
| Faroese | Marathi | Ukrainian | 
| Persian | Macedonian | Urdu | 
| Filipino;Pilipino | Maltese | Uzbek | 
| Finnish | Mongolian | Uzbek-Cyrilic | 
| French | Maori | Vietnamese | 
| German-Fraktur | Malay | Yiddish | 
| French, Middle(ca.1400-1600) | Burmese | Yoruba | 
| WesternFrisian | Nepali |  Dutch;Flemish | 
| ScottishGaelic;Gaelic |
-->
##### 2020.3.17 2A0A：使用ebu代替eb处理epwing格式字典；增加[Bass](https://www.un4seen.com/bass.html)发音引擎；解决程序退出时的异常问题（表现为在部分机器上程序退出后不能马上再次启动，可能需要等待较长时间或重启电脑后才能启动）；解决划取（ocr）到的字符串仅有无效字符（标点符号等）时程序异常退出的问题，解决划词时选取区域为空（无字符）时程序异常退出的问题；划词支持多国家/地区语言的选配。
<!---
>|  Chinese Simplified  | Chinese Traditional | English |  Estonian  | 
|  :----------------  |  :----------------  | :---------------- | :---------------- | 
|	Bulgarian	|	Hungarian	|	Slovak	|	Finnish	|
|	Catalan	|	Indonesian	|	Slovenian	|	French	|
|	Croatian	|	Italian	|	Spanish	|	German	|
|	Czech	|	Latvian	|	Swedish	|	Romanian	|
|	Danish	|	Lithuanian	|	Turkish	|	Russian	|
|	Dutch	|	Norwegian	|	Arabic	|	Japanese	|
|	Polish	|	Portuguese	|	Korean	|

如果在学习中英外的其它语种，也可以通过手工修改配置文件来开启您需要的OCR语言：
>1. 用文本编辑器打开ocr64或ocr目录下的Config.dat。
>2. 定位/搜索找到\<Languages\>，其下的内容为支持的语言，需要开启的话将其中标签内的文字0改为1即可，关闭则改1为0。
>3. 部分语言需要字典支持，可能需要同时在\<Dictionaries\>下同时添加字典信息。
>4. 确保3步中配置所需的辞书存在与ocr目录或其下的asian目录下，修改完保存重启GD即可。
-->
##### 2020.2.25 2A09：增加鼠标划词（原生内置OCR）识别 ，支持动态划图，支持划词时多屏间任意切换（双/多屏时划词幕布随鼠标游动自动切屏），可配置划词热键。
##### 2020.2.6 2A08：针对各种格式辞书的索引和查询做优化；增加辞书按照 路径（目录+文件名）来排序的功能；剔除bgl格式辞书显示的多余换行；为mdx辞书添加对 tif 格式图片的支持；解决zim和slob格式辞书 tif 格式图片支持问题（暂时没有对应格式的图片辞书来测试验证）。
<!-- >![按字典目录排序](/media/goldendict/sort_by_dir.png ) -->
##### 2020.1.31 2A07：全文搜索功能全面优化 --- 并发索引，词头去重，界面优化；增加全文搜索结果的导入（从已保存的文件加载）导出（保存为文件）功能；为金山数据的stardict格式辞书增加样式表支持，所有该格式类型的辞书共享同一样式 --- 标签对应的类名称和样式都可由用户自定义。
>下载并解压[sdct_k.style.7z](/media/goldendict/sdct_k.style.7z) (275 字节) ，将解压出的文件放到GD的配置目录下（并按需编辑其中的标签对照表），在自定义的article-style.css添加对应标签的样式属性。
<!-- >![金山数据stardict格式字典样式](/media/goldendict/sdct_k_style.png) -->
##### 2020.01.18 2A06：挖掘内存使用优化带来的提速潜力，查询性能显著提升；优化全文搜索和辞书词条对话框的部分实现，避免可能出现的内存泄漏和界面假死现象；消灭保存文章功能的内存泄漏；重构保存文章时的进度显示；优化组织查询到的辞书列表以缩短界面阻塞时间。
##### 2020.01.08 2A04：解决多部epwing格式辞书时创建索引导致程序异常退出的问题（针对这格式的辞书创建索引同步进行以避免线程安全问题导致的异常退出）；版本信息中添加编译时间；解决xdxf格式辞书def标签的序号错乱问题。
##### 2020.01.06 2A02：弃用QtXml，使用效率更高的pugixml解析库，受影响部分：mdict/xdxf/stardict格式辞书和forvo在线发音的解析，配置文件的读写（配置、收藏、历史记录文件）；解决启动到托盘功能失效的问题。
>注意：今后将仅维护2A版本；2A01及后续版本可与之前的老版本并存（同时）运行（共享运行目录和配置/辞书/索引目录），但配置文件并不兼容且并不提供转换工具，使用2A01及后续版本您的所有关于GD偏好的个人设置（编辑菜单的辞书和首选项）都必须手动重新设置。
##### 2019.12.26 2019年终版：解决64位msvc2019版GD不能识别大小超2G文件的问题；支持修改字典显示名称；消灭一堆内存泄漏问题；优化启动界面的信息提示；并发初始化索引和加载辞书，大大减少启动时间和重新扫描文件的耗时。
<!-- >![重命名辞书](/media/goldendict/rename_dict.png)  -->
##### [2019.03.12-2019.10.19](https://github.com/nonwill/goldendict/commits/master)：第三方库更新；编译器适配最新版本；界面布局调整；解决一些影响稳定性（导致程序频繁的异常蹦掉）的问题；为mdx格式辞书增加flash和视频播放支持；......
{{< /notice >}}