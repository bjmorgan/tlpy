class Host:

    def __init__( self, energy, vbm, cbm, elemental_energies, correction_scaling ):
        self.energy = energy
        self.vbm = vbm
        self.cbm = cbm
        self.elemental_energies = elemental_energies
        self.correction_scaling = correction_scaling
        self.fundamental_gap = cbm - vbm
