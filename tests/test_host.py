import unittest
import tlpy.host

class HostTestCase( unittest.TestCase ):
    """Test for `host.py`"""

    def setUp( self ):
        self.elemental_energies = { 'Ge' : -4.48604,
                               'P'  : -5.18405,
                               'O'  : -4.54934575 }

        self.energy = -2884.79313425
        self.vbm = 0.4657
        self.cbm = 4.0154
        self.correction_scaling = 0.099720981

        self.host = tlpy.host.Host( energy = self.energy,
                                    vbm = self.vbm,
                                    cbm = self.cbm,
                                    elemental_energies = self.elemental_energies,
                                    correction_scaling = self.correction_scaling )

    def test_is_host_initialised( self ):
        """Is a Host object created successfully?"""
        self.assertEqual( self.host.energy, self.energy )
        self.assertEqual( self.host.vbm, self.vbm )
        self.assertEqual( self.host.cbm, self.cbm )
        self.assertEqual( self.host.elemental_energies, self.elemental_energies )
        self.assertEqual( self.host.correction_scaling, self.correction_scaling )
        self.assertEqual( self.host.fundamental_gap, self.cbm - self.vbm )

if __name__ == '__main__':
    unittest.main()
