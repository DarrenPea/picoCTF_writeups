import tarfile
import os

def extract(tar_path, extract_to_dir):
	tar_queue = [tar_path]

	while tar_queue:
		# process next .tar
		current_tar_path = tar_queue.pop(0)

		with tarfile.open(current_tar_path, 'r:*') as tar:
			print(f"Extracting from: {current_tar_path}")

			for member in tar.getmembers():
				# if a nested .tar file is found, add it to the queue
				if member.name.endswith('.tar'):
					print(f"Found nested tar file: {member.name}")
					nested_tar_path = os.path.join(extract_to_dir, os.path.basename(member.name))
					# extract .tar file
					tar.extract(member, path=extract_to_dir)
					# add nested .tar to queue
					tar_queue.append(nested_tar_path)

				else:
					tar.extract(member, path=extract_to_dir)

		# delete .tar file after extracting
		if os.path.exists(current_tar_path):
			print(f"Deleting tar file: {current_tar_path}")
			os.remove(current_tar_path)

			
            
extract('1000.tar', 'extracted_files')