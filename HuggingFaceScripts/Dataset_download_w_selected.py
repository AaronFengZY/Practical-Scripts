from huggingface_hub import list_repo_files, hf_hub_download
import os
import shutil
import tempfile

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

# Create a temporary directory for caching downloads
with tempfile.TemporaryDirectory() as temp_cache_dir:
    # Download the selected files
    for file_path in files_to_download:
        print(f"Downloading {file_path}...")
        try:
            # Download the file to the temporary cache directory
            downloaded_file = hf_hub_download(
                repo_id=repo_id,
                filename=file_path,
                revision=branch,
                cache_dir=temp_cache_dir,
                repo_type="dataset"
            )
            # Determine the destination path in local_dir
            destination_path = os.path.join(local_dir, file_path)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            
            # Copy the actual file content from the cache to local_dir
            shutil.copy2(downloaded_file, destination_path)
        except Exception as e:
            print(f"Failed to download {file_path}: {e}")

print("Download completed.")
