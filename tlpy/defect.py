from tlpy.defect_charge_state import Defect_Charge_State

import numpy as np

class Defect:

    def __init__( self, name, stoichiometry, host, site ):
        self.name = name
        self.stoichiometry = stoichiometry
        self.charge_state = {}
        self.host = host
        self.site = site

    def add_charge_state( self, charge, energy ):
        self.charge_state[ charge ] = Defect_Charge_State( charge, energy, self.host, self.stoichiometry )

    def charge_state_energy_at_fermi_energy( self, q, e_fermi, delta_mu ):
        return self.charge_state[ q ].relative_formation_energy( e_fermi )
        return self.charge_state[ q ].formation_energy( e_fermi, delta_mu )

    def charge_state_at_fermi_energy( self, e_fermi, delta_mu ):
        return min( [ ( q, q.formation_energy( e_fermi, delta_mu ) ) for q in self.charge_state.values() ], key = lambda x : x[1] )[0]

    def tl_profile( self, delta_mu, ef_min, ef_max ):
        # first point is the lowest energy charge state at E_Fermi = 0.0 eV
        charge_state = self.charge_state_at_fermi_energy( ef_min, delta_mu )
        points = [ ( ef_min, charge_state.formation_energy( ef_min, delta_mu ) ) ]
        q1 = charge_state.charge
        # where does this line cross other charge state energies?
        while q1 != min( self.charge_state_list() ):
            next_point, next_q = min( ( ( self.transition_level( q1, q2, delta_mu ), q2 ) for q2 in ( q for q in self.charge_state if q < q1 ) ), key = lambda p : p[0][0] )
            if next_point[0] < ef_max:
                points.append( next_point )
                q1 = next_q
            else:
                break
        points.append( ( ef_max, self.charge_state[ q1 ].formation_energy( ef_max, delta_mu ) ) )
        return points

    def defect_energy_at_fermi_energy( self, e_fermi, delta_mu ):
        return self.charge_state_at_fermi_energy( e_fermi, delta_mu ).formation_energy( e_fermi, delta_mu )

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

    def xmgrace_output( self, delta_mu ):
        ret = '# {}\n'.format( self.name )
        points = self.tl_profile( delta_mu = delta_mu, ef_min = 0.0, ef_max = self.host.fundamental_gap )
        ret += '\n'.join( [ '{} {}'.format( p[0], p[1] ) for p in points ] ) + '\n'
        return ret

    def matplotlib_data( self, delta_mu, ef_min, ef_max ):
        return np.array( self.tl_profile( delta_mu, ef_min, ef_max ) ).T

