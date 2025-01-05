# README

## Overview

This repository (or project) leverages the `amlt` command-line tool to manage and work with base images. One of the key commands we use here is:

```
amlt cache base-images
```

This command lists all the available base images, including those for NVIDIA and AMD.

## Command Usage

### `amlt cache base-images`

- **Description**: Lists all the base images stored in the AMLT cache.
- **Examples**:
  ```bash
  # Lists all cached images including those for NVIDIA and AMD
  amlt cache base-images
  ```

## SLA Tier

You can specify different service-level agreement tiers via the `sla_tier` parameter. Three tiers are supported:

1. **Premium**  
2. **Standard**  
3. **Basic**
