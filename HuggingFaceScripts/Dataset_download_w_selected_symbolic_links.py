from huggingface_hub import list_repo_files, hf_hub_download
import os
import shutil

# Define repository details
repo_id = "ai4ce/EgoPAT3Dv2"
branch = "main"

# List all files in the repository, specifying repo_type as 'dataset'
files = list_repo_files(repo_id, revision=branch, repo_type="dataset")

# Exclude files in the 'raw_mkvs' folder
files_to_download = [f for f in files if not f.startswith("raw_mkvs/")]

# Define local directory to save the files
local_dir = "EgoPAT3Dv2_partial"

os.makedirs(local_dir, exist_ok=True)

# Download the selected files
for file_path in files_to_download:
    print(f"Downloading {file_path}...")
    try:
        # Download the file to cache_dir, specifying repo_type as 'dataset'
        downloaded_file = hf_hub_download(
            repo_id=repo_id,
            filename=file_path,
            revision=branch,
            cache_dir=local_dir,
            repo_type="dataset"
        )
        # Determine the relative path and destination path
        relative_path = os.path.relpath(downloaded_file, local_dir)
        destination_path = os.path.join(local_dir, file_path)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        # Move the downloaded file to the desired location
        shutil.move(downloaded_file, destination_path)
    except Exception as e:
        print(f"Failed to download {file_path}: {e}")

print("Download completed.")


"""
~/EgoPAT3Dv2_partial/11$ ls -l
total 20
lrwxrwxrwx 1 v-zhifeng@microsoft.com users 79 Dec 17 11:42 11.1.zip -> ../../../blobs/4cd8bcdd264f0c19cf78eb8c6da5fbf936eefbf67ed51b3e087a0306aaabc6c8
"""