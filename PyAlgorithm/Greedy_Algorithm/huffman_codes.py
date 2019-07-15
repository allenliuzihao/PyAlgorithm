'''
Input: probability pi for each character in character set
Output: binary tree T minimizing the average encoding length

average encoding length: sum of probability of each character times the encoding length
of each character
'''

import re
from bst_huffman_code import HuffmanBinaryTree

'''
Extract words in text to an array of strings
'''
def process_text(file_location):
	f = open(file_location, 'r')
	all_words = map(lambda l: l.split(" "), f.readlines())
	cleaned = all_words[0] if all_words[0] != ['\n'] else []
	cleaned = [re.sub(r'[^\w]', '', string.strip()) for string in cleaned]
	for i in xrange(1, len(all_words)):
		if all_words[i] != ['\n']:
			temp = [re.sub(r'[^\w]', '', string.strip()) for string in all_words[i]]
			cleaned += temp
	cleaned = [word for word in cleaned if word != '']
	return cleaned

def text_stats(words):
	stat = {}
	for word in words:
		if word in stat:
			stat[word] += 1
		else:
			stat[word] = 1
	num_words = float(len(words))
	for key in stat:
		stat[key] /= num_words
	return stat

def huffman_code(file_location):
	stats = text_stats(process_text(file_location))
	original_string = ''.join(stats.keys())
	tree = HuffmanBinaryTree(stats)
	encoding = tree.getEncoding()
	encoding_str = ''
	for key in encoding:
		encoding_str += encoding[key]
	a = sorted(tree.decode(encoding_str))
	b = sorted(original_string)
	print a == b

if __name__ == '__main__':
	huffman_code("data.txt")