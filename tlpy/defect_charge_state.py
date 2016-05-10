class Defect_Charge_State:

    def __init__( self, charge, energy, host, stoichiometry ):
        self.charge = charge
        self.energy = energy
        self.host = host
#        self.correction = self.host.correction_scaling * self.charge * self.charge
        self.stoichiometry = stoichiometry

    def formation_energy( self, e_fermi, delta_mu ):
        energy = self.energy - self.host.energy
        for element in self.stoichiometry:
            energy -= ( self.host.elemental_energies[ element ] + delta_mu[ element ] ) * self.stoichiometry[ element ]
        energy += float( self.charge ) * ( self.host.vbm + e_fermi )
        energy += self.correction
        return energy

    def relative_formation_energy( self, e_fermi ):
        energy = self.energy - self.host.energy
        energy += float( self.charge ) * ( self.host.vbm + e_fermi )
        energy += self.correction
        return energy

    @property
    def correction( self ):
        return self.host.correction_scaling * self.charge * self.charge

"""
Notes for the defect formation energy calculation approach currently used here:

The defect formation energy is calculated using the standard "Zhang and Northrup" approach:
[Zhang & Northrup, PRL 67, 2339 (1991) and e.g. Scanlon, PRB 87, 161201R (2013)].

H_f(D,q) = (E^D,q - E^H) + \sum_i n_i(E_i + \mu_i) + q(E_Fermi + E_VBM^H) + E_align[q]

E^D,q is the energy of the defect D in charge state q
E^H is the energy of the corresponding host material

The sum over i terms correspond to transfer of atoms with approriate reserviors, 
n_i is the change in atom numbers of species i
E_i is the reference energy of this atomic species
\mu_i is the (relative) chemical potential of this atomic species.

The next term incorporates the Fermi energy (electronic chemical dependence) on charge state, which includes a term E_VBM^H to account for the VBM in the *host* structure not necessarily having an energy of zero.

The final term E_align includes a potential alignment term, and an image-charge correction term (finite size correction).

The *current* implementation of the code neglects the potential alignment term (which should be an additional delta_E * q term): this code has previously only been used for defect calculations on Ge5O(PO4)6 in large enough unit cells that the potential alignment term was (I guess) negligible.
The image charge correction term (as currently implemented) uses the Lany and Zunger "3rd order" correction scheme. This approximates the Makov-Payne correction (up to 3rd order) [1,2] with a scaled first order term (see Lany's `third_order_correction` code for details), that can be expressed as a constant energy, dependent on the supercell geometry and the host material (via the dielectric constant) multiplied by q^2. As currently implemented, the constant correction scaling factor is set in self.host.correction_scaling.

[1] G. Makov and M. C. Payne, PRB 51, 4014 (1995)
[2] S. Lany and A. Zunger, PRB 78, 235104 (2008)
"""
