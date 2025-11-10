import os, shutil

def recursive_mover(current_path):
	public_path = "public" + current_path[6:]
	if os.path.isfile(current_path):
		print(f"copying {current_path} to {public_path}")
		shutil.copy(current_path,public_path)
		return
	else:
		os.mkdir(public_path)

	for sub in os.listdir(current_path):
		moveto = os.path.join(current_path,sub)
		recursive_mover(moveto)
