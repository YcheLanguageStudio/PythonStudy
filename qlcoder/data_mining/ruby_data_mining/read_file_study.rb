arr = IO.readlines("pinyin.txt")
arr.each do |ele|
  print ele
end

# for ele in arr
#   print ele
#   print PinYin.of_string(ele)
#
# end