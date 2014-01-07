#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["ene", "diene_out"], products=["Six_Ring"], ownReverse=False)

reverse = "Retro_Diels_Alder_Addition"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['CHANGE_BOND', '*4', '1', '*5'],
    ['CHANGE_BOND', '*5', '-1', '*6'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*6'],
])

entry(
    index = 1,
    label = "diene_out",
    group = "OR{diene_unsub_unsub_out, diene_unsub_monosub_out, diene_unsub_disub_out, diene_monosub_monosub_out, diene_monosub_disub_out, diene_disub_disub_out}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "diene_in",
    group = 
"""
1 *4 Cd 0 {2,S}
2 *5 Cd 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "ene",
    group = 
"""
1 *1 {Cd,Od} 0 {2,D}
2 *2 {Cd,Od} 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "diene_unsub_unsub_out",
    group = 
"""
1 *3 {Cd,Od} 0 {2,D} {5,S} {6,S}
2 *4 Cd 0 {1,D} {3,S}
3 *5 Cd 0 {2,S} {4,D}
4 *6 {Cd,Od} 0 {3,D} {7,S} {8,S}
5    H  0 {1,S}
6    H  0 {1,S}
7    H  0 {4,S}
8    H  0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "diene_unsub_monosub_out",
    group = 
"""
1 *3 {Cd,Od}  0 {2,D} {5,S} {6,S}
2 *4 Cd  0 {1,D} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *6 {Cd,Od}  0 {3,D} {7,S} {8,S}
5    H   0 {1,S}
6    H   0 {1,S}
7    H   0 {4,S}
8    R!H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "diene_unsub_monosubNd_out",
    group = 
"""
1 *3 {Cd,Od}     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 {Cd,Od}     0 {3,D} {7,S} {8,S}
5    H      0 {1,S}
6    H      0 {1,S}
7    H      0 {4,S}
8    {Cs,O} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "diene_unsub_monosubDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    H             0 {1,S}
7    H             0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "diene_unsub_disub_out",
    group = 
"""
1 *3 {Cd,Od}  0 {2,D} {5,S} {6,S}
2 *4 Cd  0 {1,D} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *6 {Cd,Od}  0 {3,D} {7,S} {8,S}
5    H   0 {1,S}
6    H   0 {1,S}
7    R!H 0 {4,S}
8    R!H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "diene_unsub_disubNd2_out",
    group = 
"""
1 *3 {Cd,Od}     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 {Cd,Od}     0 {3,D} {7,S} {8,S}
5    H      0 {1,S}
6    H      0 {1,S}
7    {Cs,O} 0 {4,S}
8    {Cs,O} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "diene_unsub_disubNdDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    H             0 {1,S}
7    {Cs,O}        0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "diene_unsub_disubDe2_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    H             0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "diene_monosub_monosub_out",
    group = 
"""
1 *3 {Cd,Od}  0 {2,D} {5,S} {6,S}
2 *4 Cd  0 {1,D} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *6 {Cd,Od}  0 {3,D} {7,S} {8,S}
5    H   0 {1,S}
6    R!H 0 {1,S}
7    R!H 0 {4,S}
8    H   0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "diene_monosubNd_monosubNd_out",
    group = 
"""
1 *3 {Cd,Od}     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 {Cd,Od}     0 {3,D} {7,S} {8,S}
5    H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {4,S}
8    H      0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "diene_monosubNd_monosubDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {4,S}
8    H             0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "diene_monosubDe_monosubDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {4,S}
8    H             0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "diene_monosub_disub_out",
    group = 
"""
1 *3 {Cd,Od}  0 {2,D} {5,S} {6,S}
2 *4 Cd  0 {1,D} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *6 {Cd,Od}  0 {3,D} {7,S} {8,S}
5    H   0 {1,S}
6    R!H 0 {1,S}
7    R!H 0 {4,S}
8    R!H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "diene_monosubNd_disubNd2_out",
    group = 
"""
1 *3 {Cd,Od}     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 {Cd,Od}     0 {3,D} {7,S} {8,S}
5    H      0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {4,S}
8    {Cs,O} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "diene_monosubNd_disubNdDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cs,O}        0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "diene_monosubNd_disubDe2_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cs,O}        0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "diene_monosubDe_disubNd2_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cs,O}        0 {4,S}
8    {Cs,O}        0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "diene_monosubDe_disubNdDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cs,O}        0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "diene_monosubDe_disubDe2_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    H             0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    {Cd,Ct,Cb,CO} 0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "diene_disub_disub_out",
    group = 
"""
1 *3 {Cd,Od}  0 {2,D} {5,S} {6,S}
2 *4 Cd  0 {1,D} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *6 {Cd,Od}  0 {3,D} {7,S} {8,S}
5    R!H 0 {1,S}
6    R!H 0 {1,S}
7    R!H 0 {4,S}
8    R!H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "diene_disubNd2_disubNd2_out",
    group = 
"""
1 *3 {Cd,Od}     0 {2,D} {5,S} {6,S}
2 *4 Cd     0 {1,D} {3,S}
3 *5 Cd     0 {2,S} {4,D}
4 *6 {Cd,Od}     0 {3,D} {7,S} {8,S}
5    {Cs,O} 0 {1,S}
6    {Cs,O} 0 {1,S}
7    {Cs,O} 0 {4,S}
8    {Cs,O} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "diene_disubNd2_disubDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    {Cs,O}        0 {1,S}
6    {Cs,O}        0 {1,S}
7    R!H           0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "diene_disubDe_disubDe_out",
    group = 
"""
1 *3 {Cd,Od}            0 {2,D} {5,S} {6,S}
2 *4 Cd            0 {1,D} {3,S}
3 *5 Cd            0 {2,S} {4,D}
4 *6 {Cd,Od}            0 {3,D} {7,S} {8,S}
5    R!H           0 {1,S}
6    {Cd,Ct,Cb,CO} 0 {1,S}
7    R!H           0 {4,S}
8    {Cd,Ct,Cb,CO} 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "diene_in_2H",
    group = 
"""
1 *4 Cd 0 {2,S} {3,S}
2 *5 Cd 0 {1,S} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "diene_in_HNd",
    group = 
"""
1 *4 Cd     0 {2,S} {3,S}
2 *5 Cd     0 {1,S} {4,S}
3    H      0 {1,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "diene_in_HDe",
    group = 
"""
1 *4 Cd            0 {2,S} {3,S}
2 *5 Cd            0 {1,S} {4,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "diene_in_NdH",
    group = 
"""
1 *4 Cd     0 {2,S} {3,S}
2 *5 Cd     0 {1,S} {4,S}
3    {Cs,O} 0 {1,S}
4    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "diene_in_DeH",
    group = 
"""
1 *4 Cd            0 {2,S} {3,S}
2 *5 Cd            0 {1,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "diene_in_Nd2",
    group = 
"""
1 *4 Cd     0 {2,S} {3,S}
2 *5 Cd     0 {1,S} {4,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "diene_in_NdDe",
    group = 
"""
1 *4 Cd            0 {2,S} {3,S}
2 *5 Cd            0 {1,S} {4,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "diene_in_DeNd",
    group = 
"""
1 *4 Cd            0 {2,S} {3,S}
2 *5 Cd            0 {1,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "diene_in_De2",
    group = 
"""
1 *4 Cd            0 {2,S} {3,S}
2 *5 Cd            0 {1,S} {4,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "ene_unsub_unsub",
    group = 
"""
1 *1 {Cd,Od} 0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od} 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "ene_unsub_monosub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "ene_2H_HNd",
    group = 
"""
1 *1 {Cd,Od}    0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "ene_2H_HDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "ene_monosub_unsub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    H   0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "ene_HNd_2H",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "ene_HDe_2H",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "ene_monosub_monosub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "ene_HNd_HNd",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "ene_HNd_HDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "ene_HDe_HNd",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "ene_HDe_HDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "ene_unsub_disub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "ene_2H_Nd2",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    H      0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "ene_2H_NdDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "ene_2H_De2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    H             0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "ene_disub_unsub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    H   0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "ene_Nd2_2H",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    H      0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "ene_NdDe_2H",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "ene_De2_2H",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    H             0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "ene_monosub_disub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    H   0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "ene_HNd_Nd2",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    H      0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "ene_HNd_NdDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "ene_HNd_De2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "ene_HDe_Nd2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "ene_HDe_NdDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "ene_HDe_De2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "ene_disub_monosub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    H   0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "ene_Nd2_HNd",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    H      0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "ene_Nd2_HDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "ene_NdDe_HNd",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "ene_NdDe_HDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "ene_De2_HNd",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "ene_De2_HDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    H             0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "ene_disub_disub",
    group = 
"""
1 *1 {Cd,Od}  0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}  0 {1,D} {5,S} {6,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {2,S}
6    R!H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "ene_Nd2_Nd2",
    group = 
"""
1 *1 {Cd,Od}     0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}     0 {1,D} {5,S} {6,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {2,S}
6    {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "ene_Nd2_NdDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "ene_Nd2_De2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cs,O}        0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "ene_NdDe_Nd2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "ene_NdDe_NdDe",
    group = 
"""
1 *1 {Cd,Od}           0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "ene_NdDe_De2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "ene_De2_Nd2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cs,O}        0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "ene_De2_NdDe",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cs,O}        0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "ene_De2_De2",
    group = 
"""
1 *1 {Cd,Od}            0 {2,D} {3,S} {4,S}
2 *2 {Cd,Od}            0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
6    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: diene_out
    L2: diene_unsub_unsub_out
    L2: diene_unsub_monosub_out
        L3: diene_unsub_monosubNd_out
        L3: diene_unsub_monosubDe_out
    L2: diene_unsub_disub_out
        L3: diene_unsub_disubNd2_out
        L3: diene_unsub_disubNdDe_out
        L3: diene_unsub_disubDe2_out
    L2: diene_monosub_monosub_out
        L3: diene_monosubNd_monosubNd_out
        L3: diene_monosubNd_monosubDe_out
        L3: diene_monosubDe_monosubDe_out
    L2: diene_monosub_disub_out
        L3: diene_monosubNd_disubNd2_out
        L3: diene_monosubNd_disubNdDe_out
        L3: diene_monosubNd_disubDe2_out
        L3: diene_monosubDe_disubNd2_out
        L3: diene_monosubDe_disubNdDe_out
        L3: diene_monosubDe_disubDe2_out
    L2: diene_disub_disub_out
        L3: diene_disubNd2_disubNd2_out
        L3: diene_disubNd2_disubDe_out
        L3: diene_disubDe_disubDe_out
L1: diene_in
    L2: diene_in_2H
    L2: diene_in_HNd
    L2: diene_in_HDe
    L2: diene_in_NdH
    L2: diene_in_DeH
    L2: diene_in_Nd2
    L2: diene_in_NdDe
    L2: diene_in_DeNd
    L2: diene_in_De2
L1: ene
    L2: ene_unsub_unsub
    L2: ene_unsub_monosub
        L3: ene_2H_HNd
        L3: ene_2H_HDe
    L2: ene_monosub_unsub
        L3: ene_HNd_2H
        L3: ene_HDe_2H
    L2: ene_monosub_monosub
        L3: ene_HNd_HNd
        L3: ene_HNd_HDe
        L3: ene_HDe_HNd
        L3: ene_HDe_HDe
    L2: ene_unsub_disub
        L3: ene_2H_Nd2
        L3: ene_2H_NdDe
        L3: ene_2H_De2
    L2: ene_disub_unsub
        L3: ene_Nd2_2H
        L3: ene_NdDe_2H
        L3: ene_De2_2H
    L2: ene_monosub_disub
        L3: ene_HNd_Nd2
        L3: ene_HNd_NdDe
        L3: ene_HNd_De2
        L3: ene_HDe_Nd2
        L3: ene_HDe_NdDe
        L3: ene_HDe_De2
    L2: ene_disub_monosub
        L3: ene_Nd2_HNd
        L3: ene_Nd2_HDe
        L3: ene_NdDe_HNd
        L3: ene_NdDe_HDe
        L3: ene_De2_HNd
        L3: ene_De2_HDe
    L2: ene_disub_disub
        L3: ene_Nd2_Nd2
        L3: ene_Nd2_NdDe
        L3: ene_Nd2_De2
        L3: ene_NdDe_Nd2
        L3: ene_NdDe_NdDe
        L3: ene_NdDe_De2
        L3: ene_De2_Nd2
        L3: ene_De2_NdDe
        L3: ene_De2_De2
"""
)

forbidden(
    label = "threeMemberedRing_2342",
    group = 
"""
1 *3 Cd 0 {2,D}
2 *4 Cd 0 {1,D} {3,S} {4,S}
3 *5 Cd 0 {2,S} {4,D}
4 *6 Cd 0 {2,S} {3,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

forbidden(
    label = "threeMemberedRing_3213",
    group = 
"""
1 *3 Cd 0 {2,D} {3,S}
2 *4 Cd 0 {1,D} {3,S}
3 *5 Cd 0 {1,S} {2,S} {4,D}
4 *6 Cd 0 {3,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

