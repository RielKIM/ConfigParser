

class ConfigDict(dict):

	def __init__(self, *args):
		self.dict = dict.__init__(self, args)

	def __setitem__(self, key, value):
		if key == '$':
			dict.__setitem__(self, key, value)
		elif key in self:
			dict.__getitem__(self, key)['$'] = value
		else:
			tmp_dict = ConfigDict()
			dict.__setitem__(self, key, tmp_dict)
			tmp_dict['$'] = value

	def __str__(self):
		if '$' in self:
			return str(dict.__getitem__(self, '$'))
		else:
			return dict.__str__(self)


	def setValue(self, value):
		dict.__setitem__(self, '$', value)
