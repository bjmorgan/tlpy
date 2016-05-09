from tlpy.defect_charge_state import Defect_Charge_State

import numpy as np

def numpy_pprint( np_array ):
    return "\n".join( [ ' '.join( [ '{}'.format( f ) for f in p ] ) for p in np_array ] )

class Defect:
    """A specific defect corresponding to a specified change in stoichiometry.
    
    Attributes:
        name (str): identifying label for this defect.
        stoichiometry (dict): the change in stoichiometry associated with forming this defect.
                              e.g. for an oxygen vacancy this would be { 'O' : -1 }.
        charge_state (dict): set of Defect_Charge_State objects corresponding to the different charge states for this defect.
                             the key for each Defect_Charge_State is the defect charge,
                             e.g. { '-1' : Defect_Charge_State(...) }.
                             Individual charge states can be added to a Defect object using the add_charge_state method.
        host (tlpy.host.Host): Host object describing the stoichiometric host system.
        site (str): identifying label for the defect site in the host structure.""" 

    def __init__( self, name, stoichiometry, host, site ):
        """Create a Defect object."""
        self.name = name
        self.stoichiometry = stoichiometry
        self.host = host
        self.site = site
        self.charge_state = {}

    def add_charge_state( self, charge, energy ):
        """Create a Defect_Charge_State object, and add it to the self.charge_state dict.

        Args:
            charge (int): charge for the charge state, e.g. +1 if 1 electron is transferred to the Fermi level.
            energy (float): energy of this charge state.

        Returns:
            The new Defect_Charge_State object."""
        self.charge_state[ charge ] = Defect_Charge_State( charge, energy, self.host, self.stoichiometry )
        return self.charge_state[ charge ]

    def charge_state_at_fermi_energy( self, e_fermi ):
        """Returns the charge state with the lowest formation energy at a given Fermi energy.

        Args:
            e_fermi (float): Fermi energy

        Returns:
            (Defect_Charge_State)"""
        return min( [ ( q, q.relative_formation_energy( e_fermi ) ) for q in self.charge_state.values() ], key = lambda x : x[1] )[0]

    def tl_profile( self, delta_mu, ef_min, ef_max ):
        """Generates the set of points for a transition level diagram.

        Args:
            delta_mu (?):
            ef_min (float):
            ef_max (float):

        Returns:
            points (np.array):"""
        charge_state = self.charge_state_at_fermi_energy( ef_min )
        points = [ ( ef_min, charge_state.formation_energy( ef_min, delta_mu ) ) ]
        q1 = charge_state.charge
        while q1 != min( self.charge_state_list() ):
            next_point, next_q = min( ( ( self.transition_level( q1, q2, delta_mu ), q2 ) for q2 in ( q for q in self.charge_state if q < q1 ) ), key = lambda p : p[0][0] )
            if next_point[0] < ef_max:
                points.append( next_point )
                q1 = next_q
            else:
                break
        points.append( ( ef_max, self.charge_state[ q1 ].formation_energy( ef_max, delta_mu ) ) )
        return np.array( points )

    def defect_energy_at_fermi_energy( self, e_fermi, delta_mu ):
        return self.charge_state_at_fermi_energy( e_fermi ).formation_energy( e_fermi, delta_mu )

    def charge_state_list( self ):
        return [ q for q in self.charge_state ]

    def transition_level( self, q1, q2, delta_mu ):
        c = self.charge_state[ q1 ].formation_energy( e_fermi = 0.0, delta_mu = delta_mu )
        d = self.charge_state[ q2 ].formation_energy( e_fermi = 0.0, delta_mu = delta_mu )
        a = q1
        b = q2
        x = ( d - c ) / ( a - b )
        y = a * x + c 
        return ( x, y )

    def xmgrace_output( self, delta_mu, ef_min = 0.0, ef_max = None ):
        """Returns a string representation of the transition level diagram for this defect,
           appropriate for plotting in xmgrace using e.g. `xmgrace output.dat`

        Args:
            delta_mu (dict): elemental chemical potentials for calculating these transition levels, e.g. { 'O' : -0.345 }
            ef_min (Optional(float)): minimum Fermi energy (relative to the host VBM). Defaults to 0.0 eV.
            ef_max (Optional(float)): maximum Fermi energy (relative to the host VBM). Defaults to the host fundamental gap.

        Returns:
            str: e.g.
                 # V_O
                 0.0 -2.4
                 1.3 0.8
                 2.6 0.8
        """
        if not ef_max:
            ef_max = self.host.fundamental_gap
        points = self.tl_profile( delta_mu, ef_min, ef_max )
        ret = '# {}\n'.format( self.name )
        ret += numpy_pprint( points ) + '\n'
        return ret

    def matplotlib_data( self, delta_mu, ef_min = 0.0, ef_max = None):
        """Returns the set of points for a transition level diagram transposed for direct matplotlib plotting.

        Args:
            delta_mu (dict): elemental chemical potentials for calculating these transition levels, e.g. { 'O' : -0.345 }
            ef_min (Optional(float)): minimum Fermi energy (relative to the host VBM). Defaults to 0.0 eV.
            ef_max (Optional(float)): maximum Fermi energy (relative to the host VBM). Defaults to the host fundamental gap.

        Returns:
            np.array
        """
        if not ef_max:
            ef_max = self.host.fundamental_gap
        return self.tl_profile( delta_mu, ef_min, ef_max ).T

