class Defect_Charge_State:

    def __init__( self, charge, energy, host, stoichiometry ):
        self.charge = charge
        self.energy = energy
        self.host = host
        self.correction = self.host.correction_scaling * self.charge * self.charge
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
