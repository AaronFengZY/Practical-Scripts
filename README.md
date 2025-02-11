# Practical-Scripts

This repository contains practical scripts designed to help everyone avoid common pitfalls in various tasks. The scripts included are designed to simplify and streamline operations, providing easy-to-follow solutions for common problems.

## Repository Structure

### `HuggingFaceScripts/`
This directory contains two scripts related to Hugging Face datasets and symbolic links:

1. **`Dataset_download_w_selected.py`**  
   A script that downloads specific datasets from Hugging Face, allowing you to select datasets based on your preferences.

2. **`Dataset_download_w_selected_symbolic_links.py`**  
   This script is similar to the previous one but also supports creating symbolic links for downloaded datasets, enabling more efficient dataset management.

---

### `GithubScripts/`
This directory contains helpful guides and documentation for GitHub-related tasks:

1. **`MergeUpstreamUpdate.md`**  
   A step-by-step guide on how to merge upstream changes into your local fork. It covers fetching the latest changes, merging them into your local branch, resolving conflicts, and pushing the updated branch to your own GitHub repository.

---

### `MSRAInternToolkit/`
This directory contains a guide on using the MSRA Intern Toolkit in Visual Studio Code:

1. **`HowToUse.md`**  
   A comprehensive step-by-step guide on how to submit jobs using the MSRA Intern Toolkit. It covers:
   - Selecting a cluster (virtual cluster, workspace, instance type, SLA tier)
   - Configuring IO (blob datastore, paths, and modes)
   - Setting up environments (AMD vs. NVIDIA)
   - Naming experiments and jobs
   - Configuring managed identity
   - Providing a reference script to clone repositories, set environment variables, and run training jobs

---

### `CondaEnvironment/`
This directory includes a collection of Conda environment YAML files for various environments (e.g., `arctic_env_environment.yml`, `hoimoge_environment.yml`, etc.), along with a script for exporting Conda requirements:

1. **`export_all_envs.sh`**  
   A handy script that iterates through multiple Conda environments and exports their configurations to `.yml` files. By editing or extending the list of environments in this script, you can quickly back up or share all of your Conda environments.

2. **Conda environment YAML files**  
   - Multiple `.yml` files (one per environment) representing specialized setups.  
   - These files can be used to re-create each environment elsewhere using:  
     ```bash
     conda env create -f <environment-file>.yml
     ```  
     or  
     ```bash
     conda env update -f <environment-file>.yml
     ```

---

### `Amulet/`
This directory contains instructions and examples related to [AMLT](https://amulet-docs.azurewebsites.net/main/config_file.html). Specifically, it includes a **`README.md`** covering:

- **`amlt cache base-images`**  
  - How to list all AMLT base images (including NVIDIA and AMD).
- **SLA Tier**  
  - How to select between **Premium**, **Standard**, and **Basic** service tiers.
- **Documentation Link**  
  - Direct link to official AMLT docs for further configuration details.

For more information, see [`Amulet/README.md`](Amulet/README.md).

---

### `Undist/`
This directory contains the undistortion script along with its documentation:

1. **`script.py`**  
   A Python script that implements an image undistortion process. It rotates the input image so that a specified pixel becomes the new forward direction, then remaps the image using a computed homography. The script:
   - Converts the target pixel to a normalized camera ray by applying the inverse of the camera intrinsics matrix.
   - Computes a rotation matrix (via the Rodrigues formula) that rotates the ray to align with \([0, 0, 1]^T\).
   - Constructs a new intrinsics matrix to center the image and forms a homography.
   - Uses OpenCV's `cv2.warpPerspective` to generate the final undistorted image.

2. **`README.md`**  
   Documentation that explains the underlying principles of the undistortion process, along with detailed usage instructions and code examples.  
   For more details on the implementation and usage, please refer to [`Undist/README.md`](Undist/README.md).

---

## Contributing
Feel free to open issues or create pull requests if you have any improvements or additional scripts you’d like to include. We welcome community contributions and feedback.

## License
This repository is made available under the [MIT License](LICENSE). Please review the license before using or distributing any part of this code.

---

**Author**: Aaron Feng  
**Last Update**: 2/11/2025
```
