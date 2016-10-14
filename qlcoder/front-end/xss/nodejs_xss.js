function escape(input) {
var stripTagsRE = /<\/?[^>]+>/gi;
input=input.replace(stripTagsRE, '');
//“<>”与“<\>”被过滤了，只有“<”和“<\”能存在，需要用<script 与浏览器自动补全特性来插入代码
input=input.replace(/[(]/g, '');
//左括号被过滤了,需要用(来替代
input=input.replace(/>|on.+?=|focus/gi, '_');
//无法用“>”闭合后写入代码或通过onxxxx=来执行script
return '<article>' + input + '</article>';
}
text=text.replace(/[+]/g,' ');
//所有加号被过滤了，所以不能用[U+0028]来表示