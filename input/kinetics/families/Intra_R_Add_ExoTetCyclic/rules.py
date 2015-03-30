#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_ExoTetcyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
<<<<<<< HEAD
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


    index = 800,
    label = "R1_rad_R2_R3;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
=======
    index = 800,
    label = "R1_rad_R2_R3;radadd_intra",
    group1 = "OR{R2OO, R3OO, R4OO, R5OO}",
    group2 = 
"""
1 *1 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
>>>>>>> b60bf41336e4a52f6397f18b7d4e90d4d41af42f
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
<<<<<<< HEAD
=======
    shortDesc = u"""""",
>>>>>>> b60bf41336e4a52f6397f18b7d4e90d4d41af42f
    longDesc = 
u"""
The kinetics for head nodes of this family have been copied from "Cyclic_Ether_Formation" family,
"Cyclic_Ether_Formation" is a special case of "Intra_R_Add_ExoTetcyclic" family, to make this reaction family possible.
Seems even kinetics of "Cyclic_Ether_Formation" are just an initial guess.
<<<<<<< HEAD
More accurate rate parameters should be estimated for both reaction families.
=======
More accurate rate parameters should be estimated for both reaction families. 
>>>>>>> b60bf41336e4a52f6397f18b7d4e90d4d41af42f
""",
)

