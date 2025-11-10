from textnode import TextNode, TextType
from copystatic import recursive_mover

def main():
	
	print("hello")
	if os.path.exists("public"):
		print("Deleting /public")
		shutil.rmtree("public")

	recursive_mover("static")




main()



