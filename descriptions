source: https://cms.mpi.univie.ac.at/wiki/index.php/PROCAR

For static calculations, the file PROCAR contains the spd- and site projected wave function character of each band. The wave function character is calculated by projecting the wave functions onto spherical harmonics that are non zero within spheres of a radius RWIGS around each ion. LORBIT determines what information is written to PROCAR. For instance RWIGS must be specified in the INCAR file in order to obtain the file for LORBIT<10.

Mind: The spd- and site projected character of each band is not evaluated in the parallel version if NPAR 1.

Format for LORBIT=11
---------------------------------------------------------------------------
# of k-points:    5         # of bands:   26         # of ions:    3

k-point     1 :    0.00000000 0.00000000 0.00000000     weight = 0.06250000

band     1 # energy  -17.37867948 # occ.  1.00000000

ion      s     py     pz     px    dxy    dyz    dz2    dxz  x2-y2    tot  
    1  0.144  0.000  0.000  0.000  0.000  0.000  0.000  0.000  0.000  0.145
    2  0.291  0.000  0.006  0.000  0.000  0.000  0.000  0.000  0.000  0.298
    3  0.291  0.000  0.006  0.000  0.000  0.000  0.000  0.000  0.000  0.298
tot    0.727  0.000  0.013  0.000  0.000  0.000  0.000  0.000  0.000  0.740
---------------------------------------------------------------------------

The header contains the information about the number of k-points, bands and how many ions are considered. The next line prints the k-point with the three coordinates in the first Brillouin zone and the corresponding k-point weight for the numerical integration followed by the band number and the energy and occupancy of the state. Each (k-point,band) pair contains the projections for every ion  , where  is the spherical harmonic centered at ion index  ,  the angular moment and magnetic quantum and  the wavefunction. The line and column with "tot" is the corresponding sum of the line and column, respectively.

For ISPIN=2 PROCAR contains a second set of projections for the spin down channel.
For LNONCOLLINEAR=.TRUE. three additional projections for each ion are printed and the output is similar to
---------------------------------------------------------------------------
ion      s     py     pz     px    dxy    dyz    dz2    dxz  x2-y2    tot  
    1  0.144  0.000  0.000  0.000  0.000  0.000  0.000  0.000  0.000  0.145
    2  0.291  0.000  0.006  0.000  0.000  0.000  0.000  0.000  0.000  0.298
    3  0.291  0.000  0.006  0.000  0.000  0.000  0.000  0.000  0.000  0.298
tot    0.727  0.000  0.013  0.000  0.000  0.000  0.000  0.000  0.000  0.740
    1 -0.011 -0.000 -0.000 -0.000 -0.000 -0.000 -0.000  0.000 -0.000 -0.011
    2 -0.023 -0.000 -0.000  0.000  0.000 -0.000 -0.000  0.000 -0.000 -0.023
    3 -0.023 -0.000 -0.000  0.000  0.000 -0.000 -0.000  0.000 -0.000 -0.023
tot   -0.057 -0.000 -0.001  0.000  0.000 -0.000 -0.000  0.000 -0.000 -0.058 
    1 -0.142 -0.000  0.000  0.000  0.000  0.000 -0.000 -0.000 -0.000 -0.142
    2 -0.286  0.000 -0.006 -0.000 -0.000  0.000 -0.000 -0.000  0.000 -0.293
    3 -0.286  0.000 -0.006 -0.000 -0.000  0.000 -0.000 -0.000  0.000 -0.293
tot   -0.715  0.000 -0.012 -0.000 -0.000  0.000 -0.000 -0.000  0.000 -0.727
    1 -0.024 -0.000  0.000 -0.000 -0.000  0.000 -0.000  0.000 -0.000 -0.024
    2 -0.048  0.000 -0.001  0.000  0.000  0.000 -0.000  0.000  0.000 -0.049
    3 -0.048  0.000 -0.001  0.000  0.000  0.000 -0.000  0.000  0.000 -0.049
tot   -0.119  0.000 -0.002  0.000  0.000  0.000 -0.000  0.000  0.000 -0.121
---------------------------------------------------------------------------
Here the entries correspond to the projected magnetizations  and are calculated for the spinor of the spinor  and the Pauli matrices:
The first set is the total (absolute) magnetization, while the remaining three sets of entries correspond to the three directions  .
