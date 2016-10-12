(\f.
  (\x.(f \v.((x x) v))
   \x.(f \v.((x x) v)))
   \fact.
    \n.
      (((cond ((less n) 1)) \_.1)
        ((mul n) (fact ((sub n) 1)))
))
