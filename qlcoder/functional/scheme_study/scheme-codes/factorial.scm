(define fac
  (lambda (x)
    (if (= x 0)
        1
        (* x (fac (- x 1))))))

(fac 5)

;Currying
;F = (lambda (h) (lambda (n) (if (< n 2) 1 (* n (h (- n 1))))))
(define F
  (lambda (h)
    (lambda(n)
      (if (< n 2)
          1
          (* n (h (- n 1)))))))

;假定对于函数f，存在不动点x，有f(x) = x，那么Y(f) = x，这是Y算子的基础。
;Easy to find that : (f (Y f)) = (Y f)
