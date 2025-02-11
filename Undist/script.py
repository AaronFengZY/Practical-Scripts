import numpy as np
import cv2

def rotation_matrix_from_vectors(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Calculate the rotation matrix such that R*a = b.
    If a and b are already parallel, return the identity matrix.
    """
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    v = np.cross(a, b)
    s = np.linalg.norm(v)
    c = np.dot(a, b)
    if s < 1e-8:
        return np.eye(3)
    # Construct the skew-symmetric matrix
    vx = np.array([[    0, -v[2],  v[1]],
                   [ v[2],     0, -v[0]],
                   [-v[1],  v[0],     0]])
    R = np.eye(3) + vx + vx @ vx * ((1 - c) / (s ** 2))
    return R

def undist_img(img: np.ndarray,
               center_x: float, center_y: float,
               intrinsics_matrix: np.ndarray,
               output_size: tuple = None) -> np.ndarray:
    """
    Simulate the extrinsic rotation operation based on the given intrinsics and target center,
    rotating the line of sight corresponding to (center_x, center_y) in the original image to the front,
    and project it to the center of the new image. The basic idea is:
      1. Map (center_x, center_y) to normalized coordinates using K⁻¹ to get the direction vector r;
      2. Calculate the rotation matrix R such that R * r = [0, 0, 1]^T;
      3. Construct a new intrinsics matrix K_new, setting the principal point of the output image to the image center;
      4. Construct the homography H = K_new * R * K⁻¹, and use cv2.warpPerspective to remap the original image.

    Args:
        img (np.ndarray): Input image, required to be a numpy array (usually BGR).
        center_x (float): The x-coordinate of the pixel in the original image that is desired to be the new optical axis.
        center_y (float): The y-coordinate of the pixel in the original image that is desired to be the new optical axis.
        intrinsics_matrix (np.ndarray): The original camera intrinsics matrix K (3×3).
        output_size (tuple, optional): Output image size (width, height); default is the same as the original image.

    Returns:
        np.ndarray: The remapped image (undistorted image).
    """
    h, w = img.shape[:2]
    if output_size is None:
        output_size = (w, h)  # (width, height)

    # 1. Calculate the normalized coordinate direction corresponding to (center_x, center_y) in the original image
    p = np.array([center_x, center_y, 1.0])
    K_inv = np.linalg.inv(intrinsics_matrix)
    r = K_inv @ p
    r = r / np.linalg.norm(r)  # Normalize

    # 2. Calculate the rotation matrix R such that R * r = [0, 0, 1]^T.
    #    That is, rotate the ray pointing to (center_x, center_y) in the original image to the front.
    target_dir = np.array([0.0, 0.0, 1.0])
    R = rotation_matrix_from_vectors(r, target_dir)

    # 3. Construct a new intrinsics matrix K_new, setting the principal point of the output image to the image center
    fx = intrinsics_matrix[0, 0]
    fy = intrinsics_matrix[1, 1]
    cx_new = output_size[0] / 2.0
    cy_new = output_size[1] / 2.0
    K_new = np.array([[fx,    0, cx_new],
                      [ 0,   fy, cy_new],
                      [ 0,    0,    1 ]], dtype=np.float32)

    # 4. Construct the homography matrix H = K_new * R * K⁻¹
    H = K_new @ R @ K_inv

    # 5. Remap the image. cv2.warpPerspective maps the output image coordinates to the original image pixel positions.
    undistorted_img = cv2.warpPerspective(img, H, output_size, flags=cv2.INTER_LINEAR)
    return undistorted_img

# ===== Example =====
if __name__ == '__main__':
    # Assume there is an image and an intrinsics matrix K
    img_path = 'your_image.jpg'
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None:
        raise IOError(f"Cannot read image {img_path}")

    # For example, the original camera intrinsics (note: actual values should be modified according to the specific situation)
    K = np.array([[1000, 0, img.shape[1]/2],
                  [0, 1000, img.shape[0]/2],
                  [0,    0,          1]], dtype=np.float32)

    # Set the position in the original image that you want to rotate to the front,
    # such as the position of a detected keypoint center_x, center_y
    center_x, center_y = 600, 400  # Example values

    undistorted = undist_img(img, center_x, center_y, K)
    cv2.imshow("Original", img)
    cv2.imshow("Undistorted", undistorted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
