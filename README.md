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

## Contributing
Feel free to open issues or create pull requests if you have any improvements or additional scripts you’d like to include. We welcome community contributions and feedback.

## License
This repository is made available under the [MIT License](LICENSE). Please review the license before using or distributing any part of this code.

---

**Author**: Aaron Feng  
**Last Update**: 1/5/2025