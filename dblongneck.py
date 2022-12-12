import sys, os, json
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
			dt=datetime.now().strftime("%d/%m/%Y")+"-"+datetime.now().strftime("%H:%M:%S")
			self.__Write(dir, {"dbl":"DBLongneckFile", "dbld":dt, "ver":"1.0"})

	def Load(self ,dir):
		if self.debug:
			print("Loading ", os.path.join(self.rootdir, dir+".dbl"))
		self.Check(dir)
		with open(os.path.join(self.rootdir, dir+".dbl"), 'r') as file:
			return json.loads(file.read())

	def __Dir(self, dir):
		if self.debug:
			print("Making Directory ", os.path.join(self.rootdir, dir))
		os.mkdir(os.path.join(self.rootdir,dir))

	def __Write(self, dir, data):
		if self.debug:
			print("Writing ", os.path.join(self.rootdir, dir+".dbl"))
		with open(os.path.join(self.rootdir, dir+".dbl"), 'w') as file:
			print(json.dumps(data, indent=4), file=file)

	def Wipe(self, dir, delete=False):
		if self.debug:
			print("Wiping ", os.path.join(self.rootdir, dir+".dbl"))
		if not delete:
			self.Check(dir)
			self.__Write(dir,"{}")
		else:
			os.remove(os.path.join(self.rootdir, dir+".dbl"))