import urllib3
from urllib.parse import quote
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

http = urllib3.PoolManager()
x = quote(sys.argv[1])
y = "http://dict.youdao.com/w/"
r = http.request('GET', y+x)
data = r.data.decode('utf-8')
css = """<style type="text/css">

.youdaoOnLine #webTrans {margin-top: -10px;}
.youdaoOnLine .c-topbar-wrapper {    margin-top: 1px;    padding-top: 3px;display:none}

.youdaoOnLine #scontainer {    margin-top: -50px;    padding-top: 1px;}
.youdaoOnLine #container {    margin-top: -50px;    padding-top: 0px;}
.youdaoOnLine .trans-container {     margin-top: 0px;	 font-size:13px;	font-weight: normal;	color: ;}
.youdaoOnLine .keyword {     margin-top: 0px;		 font-size:14px;	font-weight: bold;	color: ;}
.youdaoOnLine .def {   	color: green ;	 display:block }
.youdaoOnLine #phrsListTab .trans-container li {    font-weight: normal;    color: green ;} 
.youdaoOnLine  #tEETrans {
   display:none
} 
.youdaoOnLine  #collinsResult{
   display:none
} 
.youdaoOnLine .additional{
   display:inline-block
} 
.youdaoOnLine .c-topbar {
    height: 1px;
    line-height: 2px;
    color: #626262;
    font-size: 14px;
    margin-top: -145px;
    display:none
}
.youdaoOnLine .title {
    color: green ;
	font-weight: normal;
    font-size: ;
}
.youdaoOnLine .c-subtopbar  {display:none}
.youdaoOnLine .c-snav {display:none}
.youdaoOnLine .c-sust {display:none}
.youdaoOnLine .c-logo {display:none}
.youdaoOnLine #authTrans {display:none}
.youdaoOnLine #eTransform {display:none}
.youdaoOnLine #examples {display:}
.youdaoOnLine #authority {display:none}
.youdaoOnLine #originalSound {display:none}
.youdaoOnLine #rel-search {display:none}
.youdaoOnLine #c_footer {display:none}
.youdaoOnLine #ugcTrans {display:none}
.youdaoOnLine #wordArticle {display:none}
.youdaoOnLine #follow {display:none}
.youdaoOnLine .c-header {display:none}
.youdaoOnLine #result_navigator {display:none}
.youdaoOnLine .dict-votebar {display:none}
.youdaoOnLine .img-list{display:none}

.youdaoOnLine #results {margin-left: -115px;}
.youdaoOnLine #dict-inter {margin-left: -200px;}

.youdaoOnLine .results-contents {margin-top: -145px;padding-top: 30px;}
.youdaoOnLine .c-topbar-wrapper {
    width: 100%;
    background-color: #fcfcfe;
    box-shadow: 0 0 3px 3px #e6e6e6;
    height: 1px;
    position: ;
    top: -145px;
    z-index: 3;
    min-width: 1px;
}
</style>"""

print('%s<div class="youdaoOnLine">%s</div>' % (css, data))
