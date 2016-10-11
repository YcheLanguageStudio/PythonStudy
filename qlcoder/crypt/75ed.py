def f(keys, text):
	bytes = [ord(c) for c in text]
	result_str = ""
	for i in range(0, len(bytes), 3):
		temp = 0
		for j in range(3):
			temp <<= 8
			temp += bytes[i + j]
		for j in range(3):
			temp ^= (keys[temp & 3] << 8)
			temp = (temp << 7) | (temp >> 17)
			temp &= ((1 << 24) - 1)
		result_str += format(temp,'06x')
	return result_str


if __name__ == "__main__":
	key = [11, 22, 33, 44] #key数组是byte数组,元素的取值范围是0-255
	ans = f(key, "hello,world!")
	print ans
