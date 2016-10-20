require 'ruby-pinyin'

# return ['jie', 'cao']
PinYin.of_string('节操')

# return ['jie2', 'cao1']
PinYin.of_string('节操', true)
PinYin.of_string('节操', :ascii)

# return ["jié", "cāo"]
PinYin.of_string('节操', :unicode)

# 正确处理多音字: return ["nán", "jīng", "shì", "cháng", "jiāng", "dà", "qiáo"]
PinYin.of_string('南京市长江大桥', :unicode)

# return %w(gan xie party gan xie guo jia)
PinYin.of_string('感谢party感谢guo jia')

# return 'gan-xie-party-gan-xie-guo-jia'
PinYin.permlink('感谢party感谢guo jia')

# return 'gxpartygxguojia'
PinYin.abbr('感谢party感谢guo jia')

# return 'gan xie party, gan xie guo jia!'
# PinYin.sentence保留标点符号, 同时用对应英文标点代替中文标点
PinYin.sentence('感谢party， 感谢guo家！')

# override readings with your own data file
PinYin.override_files = [File.expand_path('../my.dat', __FILE__)]
