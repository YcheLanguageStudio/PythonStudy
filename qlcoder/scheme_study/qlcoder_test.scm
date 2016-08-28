(define (gao n)
 (do ((d (do ((i (- n 1) (- i 1))     ;var var update
              (d '() (cons i d)))     ;end of that
             ((< i 0) d))
         (append (cddr d) (list (car d)))))
     ((null? (cdr d)) (car d)))）
(display (gao 987654321))
