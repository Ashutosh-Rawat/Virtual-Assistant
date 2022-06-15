from sys import platform
from database import get_name

name = get_name()

def is_ubuntu():
	if platform == 'linux':
		return True
	elif platform == 'win32':
		return False
