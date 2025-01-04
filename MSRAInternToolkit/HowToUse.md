**MSRA Intern Toolkit – How to Submit a Job**

*Author: ZhiYuan Feng*  
*Updated: 1/4/2025*

This document provides a step-by-step guide on how to submit a job using the MSRA Intern Toolkit in Visual Studio Code (VS Code). Follow the instructions below to ensure a successful job submission process.

---

## 1. Select a Cluster
1. **Choose Cluster**: Select the desired cluster from the list of available options.  
2. **Set Virtual Cluster**: Specify which virtual cluster your job will run on.  
3. **Configure Workspace**: Select or create the workspace where the job will be executed.  
4. **Specify Instance Type**: Choose the machine type best suited for your job.  
5. **Select Number of Nodes**: Indicate how many machines (nodes) are needed.  
6. **Pick SLA Tier**:
   - **Premium**  
   - **Standard**  
   - **Basic**  

   > *Note*: The SLA Tier determines service level and cost.  

7. **Location**: Choose the default location or another preferred region if available.

---

## 2. IO (Input/Output) Configuration
1. **Database Selection**: Typically, a Blob datastore is used.  
2. **Name**: Use the name `environment` (or another meaningful name) to identify this I/O setting.  
3. **Datastore**: Select the corresponding datastore that points to your blob storage.  
4. **Path**: Provide the exact path corresponding to your blob container or folder.  
5. **Mode**: Choose one of the following access modes:
   - **Read**  
   - **Write**  
   - **Mount**  

   > *Read* gives read-only access, *Write* allows writing, and *Mount* attaches the blob storage as a folder accessible to your environment.

---

## 3. Environment Configuration
Choose the appropriate environment based on your hardware requirements:
- **AMD**: For CPU or AMD-based machines.  
- **NVIDIA**: For jobs that require GPU acceleration.  

Make sure to pick the correct environment image so your job can run properly (e.g., CUDA libraries for GPU jobs).

---

## 4. Experiment Setup
1. **Experiment Name**: Give your experiment a clear name (e.g., `hoi_experiment_v1`).  
2. **Job Name**: Name your job to help distinguish it from other jobs (e.g., `hoi_training_run1`).  

These names will help you organize and identify your experiments and their associated results.

---

## 5. Managed Identity (Optional)
If you need credentials or permissions to access certain resources, configure the **Managed Identity** settings. This ensures your job can securely interact with external services or data sources without hard-coding credentials.

---

## 6. Script Setup and Submission
You can provide a custom script to run once your environment is active. Below is a reference script that clones a GitHub repository, sets environment variables, and initiates the training process.

```bash
PAT=github_pat_....

cd /tmp
git clone https://$PAT@github.com/AaronFengZY/HOI_moge.git
cd HOI_moge
git checkout hoimoge
ln -s ${{blobmnt_fzy}} blobmnt

export GRADIENT_ACCUMULATION_STEPS=1
export BATCH_SIZE_FORWARD=2
export NUM_MACHINES=4
export NUM_PROCESSES=32
export CONFIG=configs/revision/fzy_ft/vitl_contitrain.json
export WORKSPACE=blobmnt/workspace/fzy_ft/vitl_contitrain
export CHECKPOINT=latest
export SCRIPT=scripts/train/train.py
export GRADIENT_CHECKPOINTING=True

sh scripts/shell/train.sh
```

### Notes on the Script:
1. **Authentication**: Set your personal access token (`PAT`) to allow GitHub operations.  
2. **Cloning Repository**: The script clones the `HOI_moge` repo from GitHub and checks out a specific branch (`hoimoge`).  
3. **Blob Storage Mount**: `ln -s ${{blobmnt_fzy}} blobmnt` links your blob mount path inside the container.  
4. **Environment Variables**:
   - `GRADIENT_ACCUMULATION_STEPS`, `BATCH_SIZE_FORWARD`, `NUM_MACHINES`, `NUM_PROCESSES`, etc. allow you to easily configure training parameters.  
   - `CONFIG` points to your training configuration file.  
   - `WORKSPACE` is set to the path where artifacts (checkpoints, logs, etc.) will be saved.  
5. **Launch Script**: Finally, it executes `train.sh` which initiates the model training.

---

## Finalizing Your Job Submission
Once you have completed the configuration steps above and provided your script, you can proceed to **Submit** your job. The MSRA Intern Toolkit will queue your job in the selected cluster. You can then monitor its progress and access logs or artifacts upon completion.

---

### Questions or Feedback
If you encounter any issues or have feedback regarding the MSRA Intern Toolkit plugin, please consult the official documentation or reach out to the plugin maintainers for further assistance.

---

*Author: ZhiYuan Feng*  
*Update Date: 1/4/2025*  