(define fac
  (lambda (x)
    (if (= x 0)
        1
        (* x (fac (- x 1))))))

(fac 5)
