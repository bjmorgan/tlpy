import unittest
import tlpy.host

class HostTestCase( unittest.TestCase ):
    """Test for `host.py`"""

    def test_is_host_initialised( self ):
        """Is a Host object created successfully?"""
        energy = 1.0
        vbm = 2.0
        cbm = 5.0
        elemental_energies = { 'A' : -2.3, 'B' : -3.4 }
        correction_scaling = 0.2
        host = tlpy.host.Host( energy, vbm, cbm, elemental_energies, correction_scaling )
        
        self.assertEqual( host.energy, energy )
        self.assertEqual( host.vbm, vbm )
        self.assertEqual( host.cbm, cbm )
        self.assertEqual( host.elemental_energies, elemental_energies )
        self.assertEqual( host.correction_scaling, correction_scaling )
        self.assertEqual( host.fundamental_gap, cbm - vbm )

if __name__ == '__main__':
    unittest.main()
