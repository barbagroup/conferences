**Tutorial Submissions**
Tutorials should be focused on covering a well-defined topic in a hands-on manner. We want to see attendees coding! We encourage submissions to be designed to allow at least 50% of the time for hands-on exercises even if this means the subject matter needs to be limited. Tutorials will be 4 hours in duration. In your tutorial application, you can indicate what prerequisite skills and knowledge will be needed for your tutorial, and the approximate expected level of knowledge of your students (i.e., beginner, intermediate, advanced).
For the submission you will need the following information:
* A short bio of the presenter or team members, containing a description of past experiences as a trainer/teacher/speaker, and (ideally) links to videos of these experiences if available.
* A list of prerequisite skills expected of attendees, so that participants can chose level appropriate tutorials.
* A description of the tutorial, suitable for posting on the SciPy website for attendees to view. It should include the target audience, the expected level of knowledge prior to the class, and the goals of the class.
* A more detailed outline of the tutorial content including the duration of each part and exercise sessions. Please include a description of how you plan to make the tutorial hands-on.
* Detailed installation instructions for various common Python environments so that attendees can have everything ready for participating before heading to SciPy.
* If available, the tutorial notes, slides, exercise files, and IPython notebooks, even if they are preliminary.
Additional information on tutorial submissions may be found at https://www.scipy2019.scipy.org/tutorials. Presenters will be notified on March 22nd.

# Title:
## “Land on Vector Spaces: Practical Linear Algebra with Python”

*Short summary* 
> The summary should be less than 100 words and should be suitable to be used as a description in the online program.

Linear algebra is the foundational mathematical subject that everyone needs to know today. Get lost, calculus!
Conventional presentations of linear algebra in undergraduate STEM curricula are overly focused on rules and memorization, overloaded with nomenclature, and slowed down by pen-and-paper methods.
This tutorial skips the rule-based procedures and instead uses a visualization-rich approachto and computation with NumPy to illuminate the concepts and usefulness of linear algebra.
We promise a launching pad for participants to venture into this subject and continue learning after, with a solid conceptual grasp and none of the slog. 
You don't need previous experience in the subject; some recollection of having learned about matrices and linear systems of equations could help, but is not required.

*Detailed description of the tutorial*
> Include a detailed outline for reviewers including the duration of each part and exercise sessions. It should also include the target audience, expected level of knowledge prior to the class and the goals of the class. This description is used by the reviewers to evaluate your submission. If you decide to attach extra documentation below (under Paper), please mention it in the outline.

The target audience is anyone with an interest in getting a practical entry point to one of the most important mathematical subjects underpinning data science and AI. Whether or not the participant took an undergraduate linear algebra course, this tutorial will demystify the core ideas and give overall intuition that is routinely missing from traditional teaching of this subject. The tutorial assumes only a minimal recollection of having seen matrices or linear systems of equations as a student.

The goal of this tutorial is to accelerate through from vague ideas of what are a vector and a matrix, to mastering the essential concepts and the power of linear algebra in modern applications.
The tutorial is organized in five lessons, each a Jupyter notebook. It will use NumPy and Matplotlib, but requires only beginner level at both. The only additional dependency is a helper script that we provide for creating certain custom plots. The materials are being developed on GitHub at:
https://github.com/engineersCode/EngComp4_landlinear

We will provide a Binder button to launch an interactive session with the notebooks. Otherwise, participants are invited to clone the repository, and we will provide an `environments.yml` file.

The five lessons of this learning module are a follows:

1. What is a vector? The physicist's view versus the computer scientist's view. Fundamental vector operations: visualizing vector addition and multiplication by a scalar. Intuitive presentation of basis vectors, linear combination and span. What is a matrix? A matrix as a linear transformation mapping a vector in one space, to another space. Visualizing linear transformations. Matrix-vector multiplication: a linear combination of the matrix columns. Some special transformations: rotation, shear, scaling. Matrix-matrix multiplication: a composition of two linear transformations. Idea of inverse of a matrix as a transformation that takes vectors back to where they came from.

2. Matrix-vector multiplication: (lhs of) a linear system of equation. Idea of solving for unknown vector in a linear system is equivalent to finding the input vector given the transformation matrix its transformed vector (rhs vector). Visualize 3d linear transformations. What is rank of a matrix: the dimensionality of the space spanned by the transformed vectors. Visualize the transformations of rank-deficient matrices.

3. Matrix-vector multiplication: change of basis. A matrix converts a vector's coordinates from one coordinate system to another. Visualizing the same vector before and after applying the change of basis. An inverse of that matrix will change the vector's coordinates back to original basis. Differentiate the interpretation of linear transformation with the interpretation of changing basis: the former means a matrix transforms a vector to a new vector under the same basis, the latter means a matrix can express the same vector's coordinates in a new coordinate system (basis).
 
4. Developing on the idea that a matrix can be treated as a linear transformation or a change of basis, notebook 4 visually explains the concept of eigenvalues and eigenvectors: eigenvectors of a matrix only change their scales but not directions after applying the linear transformation, eigenvalues are the corresponding scaling factors.

This notebook will also come with an application - PageRank algorithm. The algorithm will decide the order of websites from a Google search. By assuming the importance of a website is determined by the number and the importance of other websites that have a link to it, we represent these connections as a “linking” matrix and use this matrix to iteratively find our rank vectors.

The hands-on task in this notebook is to draw the linear transformation of a symmetric matrix, calculate and plot the eigenvectors of the matrix. For a 2d symmetric matrix, the two eigenvectors should be orthogonal. 

5. This notebook will cover the geometrical interpretation of singular value decomposition (SVD). While eigendecomposition is a combination of change of basis and stretching, SVD is a combination of rotation and stretching, which can be treated as a generalization of eigendecomposition.

We will add an example of how to use SVD in image compression. A 2d image can be represented as an array where each pixel is an element of the array. By applying SVD and dropping smaller singular values, we can reconstruct the original image at a lower computational and memory cost.
