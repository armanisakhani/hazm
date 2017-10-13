# coding: utf-8

from __future__ import unicode_literals
from nltk.stem.api import StemmerI
from .WordTokenizer import WordTokenizer
from .utils import default_words
import re


class Stemmer(StemmerI):
	"""
	>>> stemmer = Stemmer()
	>>> stemmer.stem('کتابی')
	'کتاب'
	>>> stemmer.stem('کتاب‌ها')
	'کتاب'
	>>> stemmer.stem('کتاب‌هایی')
	'کتاب'
	>>> stemmer.stem('کتابهایشان')
	'کتاب'
	>>> stemmer.stem('اندیشه‌اش')
	'اندیشه'
	>>> stemmer.stem('خانۀ')
	'خانه'
	"""

	def __init__(self, words_file=default_words, words=None):
		self.ends = ['ات', 'ان', 'ترین', 'تر', 'م', 'ت', 'ش', 'یی', 'ی', 'ها', 'ٔ', '‌ا', '‌']
		if words is None:
			tokenizer = WordTokenizer(words_file=words_file)
			self.words = tokenizer.words
		else:
			self.words = words

	def stem(self, word):
		for end in self.ends:
			if word.endswith(end):
				word = re.sub(r'[\u200c\s]+$', '', word[:-len(end)])
				if word in self.words:
					break

		if word.endswith('ۀ'):
			word = word[:-1] + 'ه'

		return word
