import os
import argparse


def find_files(dir_path, file_ext, min_size=None, max_size=None):
	"""
	Searches for files with the given extension in the specified directory and its subdirectories.
	Filters the results based on the specified file size range (in MB) if provided.
	Returns a list of matching file paths.
	"""
	# Convert min and max sizes to bytes if provided
	if min_size is not None:
		min_size = min_size * 1024 * 1024
	if max_size is not None:
		max_size = max_size * 1024 * 1024

	# Walk the directory tree and search for files with the given extension
	matches = []
	for root, dirs, files in os.walk(dir_path):
		for file in files:
			if file.endswith(file_ext):
				file_path = os.path.join(root, file)
				# Check file size if min or max sizes are specified
				if (min_size is None or os.path.getsize(file_path) >= min_size) and \
						(max_size is None or os.path.getsize(file_path) <= max_size):
					matches.append(file_path)

	return matches


if __name__ == "__main__":
	# Parse command line arguments
	parser = argparse.ArgumentParser(description="Find files with a given extension and size range in a directory.")
	parser.add_argument("dir_path", help="The directory to search for files.")
	parser.add_argument("file_ext", help="The file extension to search for (e.g. '.txt').")
	parser.add_argument("--min-size", type=float, help="The minimum file size in MB (optional).")
	parser.add_argument("--max-size", type=float, help="The maximum file size in MB (optional).")
	args = parser.parse_args()

	# Find matching files
	matches = find_files(args.dir_path, args.file_ext, args.min_size, args.max_size)

	# Print matching file paths
	if len(matches) == 0:
		print(f"No files with extension '{args.file_ext}' were found.")
	else:
		print(f"Found {len(matches)} files with extension '{args.file_ext}':")
		for match in matches:
			print(match)
