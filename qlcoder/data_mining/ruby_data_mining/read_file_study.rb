require 'ruby-pinyin'

arr = IO.readlines("pinyin.txt")
arr.each do |ele|
  print ele
  arr = PinYin.of_string(ele)
  print arr
  puts
end

# for ele in arr
#   print ele
#   print PinYin.of_string(ele)
#
# end
