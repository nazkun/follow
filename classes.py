from config import default_flags

class flags:
	def __init__(self, disable_defaults=False, *, noall=None, crawler=None, lydia=None, adminreport=None, noerr=None):
		for flag in default_flags.keys():
			self.__dict__[flag] = default_flags[flag]
		def iin(flag, rflag):
			if flag in default_flags.keys() and not disable_defaults:
				if rflag is not None:
					return rflag
				return default_flags[flag]
			return rflag
		self.noall = iin('noall', noall)
		self.crawler = iin('crawler', crawler)
		self.lydia = iin('lydia', lydia)
		self.adminreport = iin('adminreport', adminreport)
		self.noerr = iin('noerr', noerr)

	def __repr__(self):
		return f'flags(noall={self.noall}, crawler={self.crawler}, lydia={self.lydia}, adminreport={self.adminreport}, noerr={self.noerr})'

	def compare(self, to_be_compared):
		for flag in to_be_compared.__dict__.keys():
			if to_be_compared.__dict__[flag] == self.__dict__[flag] == True:
				return True
		for flag in to_be_compared.__dict__.keys():
			if to_be_compared.__dict__[flag]:
				if flag not in ('noerr',):
					return False
		return True

class identify:
	def __init__(self, int_id, name, session_path, trust=float('inf'), flags=flags(**default_flags)):
		self.int_id = int_id
		self.name = name
		self.session_path = session_path
		self.trust = trust
		self.flags = flags

class internal_chat:
	def __init__(self, actual_chat, chat):
		self.actual_chat = actual_chat
		self.chat = chat

	def __eq__(self, chat):
		if self.chat == chat:
			return True
		if chat in set(self.chat):
			return True
		return False

class follower:
	def __init__(self, identifier, client, me, enu):
		self.identifier = identifier
		self.client = client
		self.me = me
		self.enu = enu

		self.disconnect = client.disconnect

	def __eq__(self, int_id):
		return self.identifier.int_id == int_id

	async def online(self):
		return self.client.is_connected() == await self.client.is_user_authorized() == True
