P_{x}^{2}+P_{y}^{2}+P_{z}^{2}=P_{0}^{2}

The left three is three spin projection component in PROCAR, and the right is total projection.


With respect to SAIXS, 

To initialize calculations with the magnetic moment parallel to a chosen vector (x,y,z), it is therefore possible to either specify (assuming a single atom in the cell)


MAGMOM = x y z   ! local magnetic moment in x,y,z

SAXIS =  0 0 1   ! quantisation axis parallel to z

or

MAGMOM = 0 0 total_magnetic_moment   ! local magnetic moment parallel to SAXIS

SAXIS =  x y z   ! quantization axis parallel to vector (x,y,z)
