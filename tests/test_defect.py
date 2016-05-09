import unittest
import tlpy.defect
import tlpy.host
import numpy as np
from unittest.mock import Mock

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

    def test_transition_level( self ):
        """Calculate the transition level for two charge states"""
        tl = self.defect.transition_level( 0, 2, delta_mu = { 'O' : 0 } )
        self.assertAlmostEqual( tl[0], 1.474835153 )
        self.assertAlmostEqual( tl[1], 4.185176480 )

    def test_transition_level_missing_mu( self ):
        """Raise KeyError if the correct chemical potential is missing in a transition level calculation"""
        self.assertRaises( KeyError, self.defect.transition_level, 0, 2, { 'Ti' : 0 } )

    def test_transition_level_profile( self ):
        """Calculate the set of points that give the transition level plot for this defect"""
        tl_profile = self.defect.tl_profile( { 'O' : 0 }, 0.0, 3.0 )
        expected_profile = [ [ 0.0,         1.23550617],
                             [ 1.47483515,  4.18517648],
                             [ 3.0,         4.18517648] ]
        self.assertTrue( np.allclose( tl_profile, expected_profile ) )

    def test_xmgrace_output_generated_correctly( self ):
        self.defect.name = 'name'
        self.defect.tl_profile = Mock( return_value = np.array( [[1,2],[3,4],[5,6]] ) )
        xmgrace_output = self.defect.xmgrace_output( delta_mu = { 'O' : 0 } )
        self.assertEqual( xmgrace_output, "# name\n1 2\n3 4\n5 6\n" )

    def test_xmgrace_calls_tl_profile_correctly( self ):
        self.defect.tl_profile = Mock( return_value = np.array( [[1,2],[3,4],[5,6]] ) )
        self.defect.host.fundamental_gap = 1.0
        self.defect.xmgrace_output( delta_mu = { 'O' : 0 } )
        self.defect.tl_profile.assert_called_with( { 'O' : 0 }, 0.0, 1.0 )

    def test_xmgrace_calls_tl_profile_correctly_with_optional_arguments( self ):
        self.defect.tl_profile = Mock( return_value = np.array( [[1,2],[3,4],[5,6]] ) )
        self.defect.xmgrace_output( delta_mu = { 'O' : 0 }, ef_min = 0.5, ef_max = 1.5 )
        self.defect.tl_profile.assert_called_with( { 'O' : 0 }, 0.5, 1.5 )

if __name__ == '__main__':
    unittest.main()
