def lines(file):
	'''
	add an empty line in the end of the file
	'''
	for line in file:
		yield line
	yield '\n'

def blocks(file):
	'''
	make a block to a whole string
	'''
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []
