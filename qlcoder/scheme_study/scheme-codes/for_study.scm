(do ((i 0 (+ i 1)))
    ((= i 5) i)      ; maybe return the last value of the iteration
  (display i))

(define factorial
  (lambda (n)
    (do ((i n (- i 1)) (a 1 (* a i)))
        ((zero? i) a))))
(factorial 10)  ;
