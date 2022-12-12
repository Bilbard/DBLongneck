import sys, os, json, zstd
from datetime import datetime

class Longneck:
	def __init__(self, root, debug=False):
		self.rootdir=root
		self.debug=debug
		if self.debug:
			print("Initialized DB ", self.rootdir)

	def Update(self, dir, data):
		if self.debug:
			print("Updating ", os.path.join(self.rootdir, dir+".dbl"))
		t=self.Load(dir)
		t.update(data.copy())
		self.__Write(dir, t)
		
	def Check(self, dir):
		if self.debug:
			print("Checking ", os.path.join(self.rootdir, dir+".dbl"))
		if not os.path.exists(os.path.join(self.rootdir, dir+".dbl")):
			try:
				self.__Dir("/".join(dir.split("/")[:-1]))
			except:
				pass
			self.__Write(dir, self.__DefaultHeader())

	def Load(self, dir):
		if self.debug:
			print("Loading ", os.path.join(self.rootdir, dir+".dbl"))
		self.Check(dir)
		with open(os.path.join(self.rootdir, dir+".dbl"), 'rb') as file:
			return json.loads(self.__Decompress(file.read()).decode())
	
	def __Compress(self, data):
		if self.debug:
			print("Compressing data")
		return zstd.compress(data,8)

	def __Decompress(self, data):
		if self.debug:
			print("Decompressing data")
		return zstd.decompress(data)
	
	def IsBlank(self, dir):
		if list(os.path.join(self.rootdir, dir+".dbl"))==list(self._DefaultHeader):
			return True
		return False
	
	def __DefaultHeader(self):
		dt=datetime.now().strftime("%d/%m/%Y")+"-"+datetime.now().strftime("%H:%M:%S")
		return {"dbl":"DBLongneckFile", "dbld":dt, "ver":"1.1"}
	
	def __Dir(self, dir):
		if self.debug:
			print("Making Directory ", os.path.join(self.rootdir, dir))
		os.mkdir(os.path.join(self.rootdir,dir))

	def __Write(self, dir, data):
		if self.debug:
			print("Writing ", os.path.join(self.rootdir, dir+".dbl"))
		with open(os.path.join(self.rootdir, dir+".dbl"), 'wb') as file:
			c = str.encode(json.dumps(data, indent=4))
			file.write(self.__Compress(c))

	def GetLast(self, dir):
		t=self.Load(dir)
		t2=t[list(t)[-1]]
		return t2

	def Wipe(self, dir, delete=False):
		if self.debug:
			print("Wiping ", os.path.join(self.rootdir, dir+".dbl"))
		if not delete:
			self.Check(dir)
			self.__Write(dir,self.__DefaultHeader())
		else:
			os.remove(os.path.join(self.rootdir, dir+".dbl"))