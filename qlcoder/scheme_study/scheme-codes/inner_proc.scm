(define fix
	(lambda (x y z)
		(define add
			(lambda (a b) (+ a b)))
		(- x (add y z))))
(display (fix 100 20 30))
