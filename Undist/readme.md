Below is an organized README that explains the purpose, method, and usage of the `undistort_script.py` in a clear, step-by-step manner.

---

# Undistort Script README

## Overview

The `undistort_script.py` reprojects an image so that a selected pixel (or region of interest) becomes the new center of view. In other words, it rotates the camera view such that the ray corresponding to the chosen pixel aligns with the forward direction \([0, 0, 1]^T\), and then it reprojects the image accordingly. This process is useful when you want to “recenter” an image on a particular feature or keypoint.

---

## How It Works

The script follows these key steps:

1. **Compute the Target Ray Direction**
   - **Purpose:**  
     Convert the target pixel coordinates \((\text{center\_x}, \text{center\_y})\) into a normalized direction in camera space.
   - **How:**  
     Use the inverse of the camera intrinsics matrix \(K\) to map the pixel coordinates back to normalized camera coordinates:
     \[
     \mathbf{r} = K^{-1} \begin{bmatrix} \text{center\_x} \\ \text{center\_y} \\ 1 \end{bmatrix}
     \]
     Then normalize \(\mathbf{r}\) to obtain a unit vector representing the viewing ray.

2. **Calculate the Rotation Matrix**
   - **Purpose:**  
     Determine a rotation \(R\) that rotates the computed ray \(\mathbf{r}\) to align with the forward (or principal) direction \([0, 0, 1]^T\).
   - **How:**  
     Use the Rodrigues formula (or equivalently, compute the cross product for the rotation axis and the dot product for the angle) to construct \(R\) such that:
     \[
     R\,\mathbf{r} = [0, 0, 1]^T
     \]
   - **Note on Uniqueness:**  
     - For two non-collinear unit vectors (when \(\mathbf{r} \neq -[0, 0, 1]^T\)), the minimal rotation (i.e., the one with the smallest rotation angle) is unique.
     - If \(\mathbf{r}\) is already \([0, 0, 1]^T\), \(R\) is the identity matrix.
     - In the special case where \(\mathbf{r} = -[0, 0, 1]^T\) (i.e., exactly opposite), there are infinitely many valid rotations. In practice, additional constraints are required to select one solution; here, the minimal rotation solution is chosen.

3. **Construct the Homography Matrix**
   - **Purpose:**  
     Map the rotated (or “undistorted”) image back into the image plane.
   - **How:**  
     First, define a new intrinsics matrix \(K_{\text{new}}\) that places the principal point at the center of the output image (and typically uses the same focal lengths as \(K\)). Then, form the homography:
     \[
     H = K_{\text{new}}\, R\, K^{-1}
     \]
     This homography describes how points in the output image correspond to points in the original image.

4. **Remap the Image Using OpenCV**
   - **Purpose:**  
     Apply the computed homography to obtain the final “undistorted” image.
   - **How:**  
     Use `cv2.warpPerspective`, which uses the homography \(H\) to map every pixel from the output image back to the appropriate location in the original image.

---

## Key Functions

### `rotation_matrix_from_vectors(a: np.ndarray, b: np.ndarray) -> np.ndarray`
- **Description:**  
  Computes a rotation matrix that rotates vector `a` to align with vector `b` using the Rodrigues formula.
- **Special Cases:**
  - If `a` and `b` are already aligned, the function returns the identity matrix.
  - If `a` and `b` are anti-parallel, the rotation is 180° and there are infinitely many solutions; the function selects one based on the minimal rotation criterion.

### `undist_img(img: np.ndarray, center_x: float, center_y: float, intrinsics_matrix: np.ndarray, output_size: tuple = None) -> np.ndarray`
- **Description:**  
  Implements the complete undistortion process:
  1. Converts the chosen pixel to a normalized camera ray.
  2. Computes the rotation matrix.
  3. Constructs a new intrinsics matrix (with the principal point at the output image center).
  4. Forms the homography and applies `cv2.warpPerspective`.
- **Parameters:**
  - `img`: The input image (as a NumPy array).
  - `center_x`, `center_y`: The pixel coordinates that you wish to rotate to the forward direction.
  - `intrinsics_matrix`: The original camera intrinsics matrix \(K\).
  - `output_size`: Optional tuple \((\text{width}, \text{height})\) for the output image size. Defaults to the input image size.
- **Returns:**  
  The remapped (undistorted) image.

---

## Why Use \(K^{-1}\) for the Target Ray?

The camera projection is governed by:
\[
s \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = K \begin{bmatrix} X \\ Y \\ Z \end{bmatrix}
\]
where \((u,v)\) are the pixel coordinates and \([X, Y, Z]^T\) represents a point (or direction) in camera space. Multiplying by \(K^{-1}\) reverses the effect of the camera intrinsics (focal lengths and principal point offsets), yielding the normalized camera coordinates. This step is essential to obtain a direction vector that reflects the true geometric ray from the camera center, independent of pixel scaling and offsets.

---

## Example Usage

Below is a sample code snippet demonstrating how to use the undistortion process:

```python
import cv2
import numpy as np
from undistort_script import undist_img  # or include the functions directly

# Load an image
img = cv2.imread('your_image.jpg')
if img is None:
    raise IOError("Cannot load image 'your_image.jpg'")

# Define the camera intrinsics (update with your actual parameters)
h, w = img.shape[:2]
K = np.array([
    [1000, 0, w / 2],
    [0, 1000, h / 2],
    [0, 0, 1]
], dtype=np.float32)

# Choose the target pixel (for instance, a keypoint you want to recenter)
center_x, center_y = 600, 400

# Undistort the image (rotate so the chosen pixel is centered)
undistorted = undist_img(img, center_x, center_y, K)

# Display the original and undistorted images
cv2.imshow("Original", img)
cv2.imshow("Undistorted", undistorted)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Conclusion

The `undistort_script.py` provides a flexible way to reorient an image so that a particular pixel (or region) becomes the center of view. By converting pixel coordinates to normalized camera coordinates, computing a minimal rotation, and constructing a homography, the script remaps the image for further analysis or processing. Adjust the intrinsics, target pixel, and output size as needed for your specific application.

Feel free to extend or modify the script to suit your requirements.
