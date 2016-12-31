#Python Study
##Python2.7 Study
- language core

content | detail 
--- | --- 
[cocurrent](study/language_core_and_lib/concurrent) | thread_pool
[data structure](study/language_core_and_lib/data_structure) | algorithm, structure, collection, string 
[function](study/language_core_and_lib/function) | function, operator 
[os](study/language_core_and_lib/os) | rename, system 
[regex](study/language_core_and_lib/regex) | regex 

- third-party libraries

content | detail 
--- | --- 
[crawler](study/third_party_library/crawler) | bs4 
[numpy-usage](study/third_party_library/numpy_usage) | numpy
[plot](study/third_party_library/plot) | matplot

##Software Analysis Study
- [software analysis tools](software_analysis_tool), corresponding dataset is held in [software_analysis_tool/dataset](software_analysis_tool/dataset)

content | detail
--- | ---
[def-use coverage](software_analysis_tool/def_use_coverage.py) | def-use coverage, dependency is networkx
[prime-path-coverage](software_analysis_tool/prime_path_coverage.py) | prime-path coverage, dendency is networkx

##Cryptography Study
- [course materials](course_materials), which covers following contents.
  - three assignments, [assign1](course_materials/crypto_homework1), [assign2](course_materials/crypto_homework2), [assign3](course_materials/crypto_homework3)
  - one report about identity-based encryption system, which is one type of public-key cipher, [identity-based encryption report](course_materials/project_ibe)

- [cryptography tools](crpyto_tool), which covers following contents.

content | detail
--- | ---
[Finite Field](crpyto_tool/libs/finite_field_op.py)  | number theorem about finite filed
[With Integer](crpyto_tool/libs/extended_euclidean.py), [With Finite Filed](crpyto_tool/libs/extended_euclidean_poly.py)  | extended eculidean algorithm with integer and finite field number
[Chinese RemainderUsage](crpyto_tool/libs/chinese_remainder_theorem.py)  | chinese remainder theorem
[Substitution Cipher](crpyto_tool/libs/substitution_cipher.py) | symmetric-key cipher
[RSA](crpyto_tool/libs/rsa.py) | public-key cipher: rsa
[RSA-Variant](crpyto_tool/libs/rsa_with_chinese_remainder.py) | public-key cipher: rsa-variant with chinese remainder
[Elgamal](crpyto_tool/libs/elgamal.py) | public-key cipher: elgamal
[HMAC](crpyto_tool/libs/hmac.py) | hmac implementation with `md5` as the hash function
[SHA-1](crpyto_tool/libs/sha1.py) | components in sha1 implementation

##Other
- [userful links](other), some useful links of python repositories
