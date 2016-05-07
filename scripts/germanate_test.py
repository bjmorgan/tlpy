#! /usr/bin/env python3

from tlpy.host import Host
from tlpy.defect import Defect

elemental_energies = { 'Ge' : -4.48604,
                       'P'  : -5.18405,
                       'O'  : -4.54934575 }

host = Host( energy = -2884.79313425,
             vbm = 0.4657,
             cbm = 4.0154,
             elemental_energies = elemental_energies,
             correction_scaling = 0.099720981 )

chemical_potential_limits = {}

chemical_potential_limits[ 'A' ] = { 'Ge' : -4.8746,
                                     'P'  : -8.165,
                                     'O'  :  0.0 }

chemical_potential_limits[ 'B' ] = { 'Ge' : -4.8664,
                                     'P'  : -8.718,
                                     'O'  :  0.0 }

chemical_potential_limits[ 'C' ] = { 'Ge' : 0.0,
                                     'P'  : -2.0718,
                                     'O'  : -2.4373 }

chemical_potential_limits[ 'D' ] = { 'Ge' : 0.0,
                                     'P'  : -2.0888,
                                     'O'  : -2.4332 }

VO1 = Defect( 'V_O1', stoichiometry = { 'O' : -1 }, host = host, site = 'O' )
VO1.add_charge_state(  0, -2876.05861202 )
VO1.add_charge_state( +1, -2877.36415986 )
VO1.add_charge_state( +2, -2880.33856625 )

VO2 = Defect( 'V_O2', stoichiometry = { 'O' : -1 }, host = host, site = 'O' )
VO2.add_charge_state( 0, -2877.91757552 )
VO2.add_charge_state( +1, -2878.40444833 )
VO2.add_charge_state( +2, -2878.85619152 )

VO3 = Defect( 'V_O3', stoichiometry = { 'O' : -1 }, host = host, site = 'O' )
VO3.add_charge_state(  0, -2876.646 )
VO3.add_charge_state( +1, -2877.139 )
VO3.add_charge_state( +2, -2877.594 )

VO4 = Defect( 'V_O4', stoichiometry = { 'O' : -1 }, host = host, site = 'O' )
VO4.add_charge_state(  0, -2876.170 )
VO4.add_charge_state( +1, -2877.217 )
VO4.add_charge_state( +2, -2880.752 )

VO5 = Defect( 'V_O5', stoichiometry = { 'O' : -1 }, host = host, site = 'O' )
VO5.add_charge_state(  0, -2876.028 )
VO5.add_charge_state( +1, -2877.561 )
VO5.add_charge_state( +2, -2879.462 )

Oi = Defect( 'O_i', stoichiometry = { 'O' : +1 }, host = host, site = 'i' )
Oi.add_charge_state(  0, -2887.757 )
Oi.add_charge_state( -1, -2885.340 )
Oi.add_charge_state( -2, -2882.347 )

VGe1 = Defect( 'V_Ge1', stoichiometry = { 'Ge' : -1 }, host = host, site = 'Ge' )
VGe1.add_charge_state(  0, -2870.216817 )
VGe1.add_charge_state( -1, -2868.426975 )
VGe1.add_charge_state( -2, -2866.739624 )
VGe1.add_charge_state( -3, -2864.304834 )
VGe1.add_charge_state( -4, -2861.29928 )

VGe2 = Defect( 'V_Ge2', stoichiometry = { 'Ge' : -1 }, host = host, site = 'Ge' )
VGe2.add_charge_state(  0, -2867.345547 )
VGe2.add_charge_state( -1, -2867.211323 )
VGe2.add_charge_state( -2, -2866.265491 )
VGe2.add_charge_state( -3, -2864.710182 )
VGe1.add_charge_state( -4, -2862.476172 )

VGe3 = Defect( 'V_Ge3', stoichiometry = { 'Ge' : -1 }, host = host, site = 'Ge' )
VGe3.add_charge_state(  0, -2869.32676 )
VGe3.add_charge_state( -1, -2868.426748 )
VGe3.add_charge_state( -2, -2866.739636 )
VGe3.add_charge_state( -3, -2864.294208 )
VGe3.add_charge_state( -4, -2861.300372 )

VP = Defect( 'V_P', stoichiometry = { 'P' : -1 }, host = host, site = 'P' )
VP.add_charge_state(  0, -2864.292 )
VP.add_charge_state( -1, -2863.078 )
VP.add_charge_state( -2, -2860.643 )
VP.add_charge_state( -3, -2857.421 )
VP.add_charge_state( -4, -2853.678 )
VP.add_charge_state( -5, -2849.884 )

PGe1 = Defect( 'PGe1', stoichiometry = { 'P' : +1, 'Ge' : -1 }, host = host, site = 'Ge1' )
PGe1.add_charge_state(  0, -2885.223 )
PGe1.add_charge_state( +1, -2889.005 )

PGe2 = Defect( 'PGe2', stoichiometry = { 'P' : +1, 'Ge' : -1 }, host = host, site = 'Ge2' )
PGe2.add_charge_state(  0, -2883.819 )
PGe2.add_charge_state( +1, -2887.755 )

PGe3 = Defect( 'PGe3', stoichiometry = { 'P' : +1, 'Ge' : -1 }, host = host, site = 'Ge3' )
PGe3.add_charge_state(  0, -2883.874 )
PGe3.add_charge_state( +1, -2887.826 )

GeP = Defect( 'GeP', stoichiometry = { 'P' : -1, 'Ge' : +1 }, host = host, site = 'P' )
GeP.add_charge_state(  0, -2879.026 )
GeP.add_charge_state( -1, -2878.217 )

VPO4 = Defect( 'VPO4', stoichiometry = { 'P' : -1, 'O' : -4 }, host = host, site = 'P' )
VPO4.add_charge_state(  0, -2846.845 )
VPO4.add_charge_state( +1, -2850.335 )
VPO4.add_charge_state( +2, -2851.6172 )
VPO4.add_charge_state( +3, -2854.244 )

defects = [ VO1, VO2, VO3, VO4, VO5, Oi, VGe1, VGe2, VGe3, VP, PGe1, PGe2, PGe3, GeP, VPO4 ]

mu = chemical_potential_limits[ 'D' ]

for d in defects:
    print( d.xmgrace_output( delta_mu = mu ) )

