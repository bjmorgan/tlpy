import unittest
import tlpy.defect
import tlpy.host

class DefectTestCase( unittest.TestCase ):
    """Test for `defect.py`"""

    def setUp( self ):

        elemental_energies = { 'Ge' : -4.48604,
                       'P'  : -5.18405,
                       'O'  : -4.54934575 }

        self.host = tlpy.host.Host( energy = -2884.79313425,
                                    vbm = 0.4657,
                                    cbm = 4.0154,
                                    elemental_energies = elemental_energies,
                                    correction_scaling = 0.099720981 )

        self.name = 'V_O1'
        self.stoichiometry = { 'O' : -1 }
        self.site = 'O'
        self.defect = tlpy.defect.Defect( self.name, self.stoichiometry, self.host, self.site )
       
        qs0 = self.defect.add_charge_state(  0, -2876.05861202 )
        qs1 = self.defect.add_charge_state( +1, -2877.36415986 )
        qs2 = self.defect.add_charge_state( +2, -2880.33856625 )
        self.charge_states = [ qs0, qs1, qs2 ]

    def test_is_defect_initialised( self ):
        """Checking Defect object is correctly initialised"""
        self.assertEqual( self.defect.name, self.name )
        self.assertEqual( self.defect.stoichiometry, self.stoichiometry )
        self.assertEqual( self.defect.host, self.host )
        self.assertEqual( self.defect.site, self.site )

    def test_add_charge_state( self ):
        """Checking adding a Defect_Charge_State object to a Defect object"""
        q = 0
        energy = -2876.05861202
        self.defect.add_charge_state( q, energy )
        self.assertEqual( self.defect.charge_state[ q ].charge, q )
        self.assertEqual( self.defect.charge_state[ q ].energy, energy )

    def test_charge_state_at_fermi_energy( self ):
        """Lowest formation energy charge state at a specific Fermi energy"""
        self.assertEqual( self.defect.charge_state_at_fermi_energy( 0.0 ), self.charge_states[ 2 ] )
        self.assertEqual( self.defect.charge_state_at_fermi_energy( 3.0 ), self.charge_states[ 0 ] )

    def test_charge_state_list( self ):
        """List of charge states returned"""
        self.assertEqual( self.defect.charge_state_list(), [ cs.charge for cs in self.charge_states ] )

if __name__ == '__main__':
    unittest.main()
