import time

def hello_world():
	print("hello world")

def bye_world():
	time.sleep(2)
	print("bye world")
	print("modified in otherbranch")
	print("i will make conflict with otherbranch")
	print("i like master more")

if __name__ == "__main__":
	hello_world()
	bye_world()
	print("yeah is mater branch!")
	print("one more print on master")
	print("print something on anotherbranch")
	print("qw")
	print("1")
	print("2")
	print("qw")