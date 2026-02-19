#!/usr/bin/env python3
"""
Low-Poly Easter Bunny Generator
Generates a 3D low-poly Easter bunny model as an STL file.
"""

import numpy as np
from stl import mesh


def create_icosphere(radius=1.0, subdivisions=1, center=(0, 0, 0)):
    """
    Create a low-poly icosphere (geodesic sphere).
    
    Args:
        radius: Radius of the sphere
        subdivisions: Number of subdivisions (0 = icosahedron, higher = more detail)
        center: Center position (x, y, z)
    
    Returns:
        vertices: Array of vertex positions
        faces: Array of face indices
    """
    # Golden ratio
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    
    # Base icosahedron vertices (12 vertices)
    a = 1.0
    vertices = np.array([
        [-a,  phi,  0],
        [ a,  phi,  0],
        [-a, -phi,  0],
        [ a, -phi,  0],
        
        [ 0, -a,  phi],
        [ 0,  a,  phi],
        [ 0, -a, -phi],
        [ 0,  a, -phi],
        
        [ phi,  0, -a],
        [ phi,  0,  a],
        [-phi,  0, -a],
        [-phi,  0,  a],
    ])
    
    # Normalize vertices to unit sphere
    vertices = vertices / np.linalg.norm(vertices[0])
    
    # Base icosahedron faces (20 triangles)
    faces = np.array([
        [0, 11, 5],
        [0, 5, 1],
        [0, 1, 7],
        [0, 7, 10],
        [0, 10, 11],
        
        [1, 5, 9],
        [5, 11, 4],
        [11, 10, 2],
        [10, 7, 6],
        [7, 1, 8],
        
        [3, 9, 4],
        [3, 4, 2],
        [3, 2, 6],
        [3, 6, 8],
        [3, 8, 9],
        
        [4, 9, 5],
        [2, 4, 11],
        [6, 2, 10],
        [8, 6, 7],
        [9, 8, 1],
    ])
    
    # Scale by radius and translate to center
    vertices = vertices * radius
    vertices[:, 0] += center[0]
    vertices[:, 1] += center[1]
    vertices[:, 2] += center[2]
    
    return vertices, faces


def create_ellipsoid(rx=1.0, ry=1.0, rz=1.0, subdivisions=1, center=(0, 0, 0)):
    """
    Create a low-poly ellipsoid by scaling an icosphere.
    
    Args:
        rx, ry, rz: Radii in x, y, z directions
        subdivisions: Number of subdivisions
        center: Center position (x, y, z)
    
    Returns:
        vertices: Array of vertex positions
        faces: Array of face indices
    """
    vertices, faces = create_icosphere(radius=1.0, subdivisions=subdivisions, center=(0, 0, 0))
    
    # Scale differently in each axis
    vertices[:, 0] *= rx
    vertices[:, 1] *= ry
    vertices[:, 2] *= rz
    
    # Translate to center
    vertices[:, 0] += center[0]
    vertices[:, 1] += center[1]
    vertices[:, 2] += center[2]
    
    return vertices, faces


def create_box(width=1.0, height=1.0, depth=1.0, center=(0, 0, 0)):
    """
    Create a simple box (8 vertices, 12 triangular faces).
    
    Args:
        width: Size in x direction
        height: Size in y direction
        depth: Size in z direction
        center: Center position (x, y, z)
    
    Returns:
        vertices: Array of vertex positions
        faces: Array of face indices
    """
    w, h, d = width / 2, height / 2, depth / 2
    cx, cy, cz = center
    
    vertices = np.array([
        [cx - w, cy - h, cz - d],
        [cx + w, cy - h, cz - d],
        [cx + w, cy + h, cz - d],
        [cx - w, cy + h, cz - d],
        [cx - w, cy - h, cz + d],
        [cx + w, cy - h, cz + d],
        [cx + w, cy + h, cz + d],
        [cx - w, cy + h, cz + d],
    ])
    
    faces = np.array([
        # Front
        [0, 1, 2],
        [0, 2, 3],
        # Back
        [4, 6, 5],
        [4, 7, 6],
        # Left
        [0, 3, 7],
        [0, 7, 4],
        # Right
        [1, 5, 6],
        [1, 6, 2],
        # Bottom
        [0, 4, 5],
        [0, 5, 1],
        # Top
        [3, 2, 6],
        [3, 6, 7],
    ])
    
    return vertices, faces


def combine_meshes(mesh_list):
    """
    Combine multiple meshes (vertices, faces) into a single mesh.
    
    Args:
        mesh_list: List of tuples (vertices, faces)
    
    Returns:
        combined_vertices: Combined vertex array
        combined_faces: Combined face array with corrected indices
    """
    all_vertices = []
    all_faces = []
    vertex_offset = 0
    
    for vertices, faces in mesh_list:
        all_vertices.append(vertices)
        # Adjust face indices based on current vertex offset
        adjusted_faces = faces + vertex_offset
        all_faces.append(adjusted_faces)
        vertex_offset += len(vertices)
    
    combined_vertices = np.vstack(all_vertices)
    combined_faces = np.vstack(all_faces)
    
    return combined_vertices, combined_faces


def create_bunny_mesh():
    """
    Create a low-poly Easter bunny mesh.
    
    Returns:
        combined_vertices: All vertices
        combined_faces: All faces
    """
    meshes = []
    
    # Body: Flattened ellipsoid (wider in x-z, shorter in y)
    body_vertices, body_faces = create_ellipsoid(
        rx=1.5,  # Width
        ry=1.8,  # Height
        rz=1.2,  # Depth
        center=(0, 1.0, 0)
    )
    meshes.append((body_vertices, body_faces))
    
    # Head: Smaller sphere on top of body
    head_vertices, head_faces = create_ellipsoid(
        rx=0.8,  # Width
        ry=0.9,  # Height
        rz=0.8,  # Depth
        center=(0, 3.0, 0.2)
    )
    meshes.append((head_vertices, head_faces))
    
    # Left ear: Elongated box
    left_ear_vertices, left_ear_faces = create_box(
        width=0.3,
        height=1.5,
        depth=0.2,
        center=(-0.4, 4.2, 0.2)
    )
    meshes.append((left_ear_vertices, left_ear_faces))
    
    # Right ear: Elongated box
    right_ear_vertices, right_ear_faces = create_box(
        width=0.3,
        height=1.5,
        depth=0.2,
        center=(0.4, 4.2, 0.2)
    )
    meshes.append((right_ear_vertices, right_ear_faces))
    
    # Left foot: Small ellipsoid
    left_foot_vertices, left_foot_faces = create_ellipsoid(
        rx=0.5,
        ry=0.3,
        rz=0.7,
        center=(-0.7, 0.2, 0.3)
    )
    meshes.append((left_foot_vertices, left_foot_faces))
    
    # Right foot: Small ellipsoid
    right_foot_vertices, right_foot_faces = create_ellipsoid(
        rx=0.5,
        ry=0.3,
        rz=0.7,
        center=(0.7, 0.2, 0.3)
    )
    meshes.append((right_foot_vertices, right_foot_faces))
    
    # Tail: Small sphere at back of body
    tail_vertices, tail_faces = create_icosphere(
        radius=0.4,
        center=(0, 1.2, -1.5)
    )
    meshes.append((tail_vertices, tail_faces))
    
    # Combine all meshes
    combined_vertices, combined_faces = combine_meshes(meshes)
    
    return combined_vertices, combined_faces


def save_stl(vertices, faces, filename):
    """
    Save vertices and faces as an STL file.
    
    Args:
        vertices: Array of vertex positions
        faces: Array of face indices
        filename: Output STL filename
    """
    # Create mesh
    bunny_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    # Fill mesh with vertex data
    for i, face in enumerate(faces):
        for j in range(3):
            bunny_mesh.vectors[i][j] = vertices[face[j]]
    
    # Save to file
    bunny_mesh.save(filename)
    print(f"✓ Low-poly Easter bunny saved to '{filename}'")
    print(f"  - Vertices: {len(vertices)}")
    print(f"  - Faces: {len(faces)}")


def main():
    """Main function to generate the Easter bunny STL file."""
    print("Generating low-poly Easter bunny...")
    
    # Create bunny mesh
    vertices, faces = create_bunny_mesh()
    
    # Save as STL
    output_file = "easter_bunny_lowpoly.stl"
    save_stl(vertices, faces, output_file)
    
    print("\nDone! You can now open the STL file with any 3D viewer or slicer.")


if __name__ == "__main__":
    main()
