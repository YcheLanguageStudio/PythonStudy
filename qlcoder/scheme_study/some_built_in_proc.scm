(null? '())  ; null意为空类型，它表示为 '() ，即括号里什么都没有的符号
(define x 123)	;	定义变量x其值为123
(symbol? x)		;=> #f
(symbol? 'x)	;	=> #t  ; 此时 'x 为符号x，并不表示变量x的值
