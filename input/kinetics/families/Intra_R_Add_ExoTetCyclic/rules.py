#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_ExoTetcyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 807,
    label = "R1_rad_R2_R3;multiplebond_intra;radadd_intra",
    group1 = "OR{R4, R5, R6, R7}",
    group2 = 
"""
1 *2 {C,O} 0 {2,S}
2 *3 {C,O} 0 {1,S}
""",
    group3 = 
"""
1 *1 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",

)


