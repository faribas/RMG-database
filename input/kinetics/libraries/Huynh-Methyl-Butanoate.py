#!/usr/bin/env python
# encoding: utf-8

name = "Huynh-Methyl-Butanoate"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
	index = 1,
	reactant1 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}

""",
	product1 = 
"""
ME2J
1 C 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 C 1 {3,S}
""",
	product2 = 
"""
C2H5
1 C 1 {2,S}
2 C 0 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (8000000000000.0, 's^-1'),
		n = 0,
		Ea = (0, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""
Some methyl butanoate reactions.
Unimolecular decomposition rates.

These are from http://dx.doi.org/10.1016/j.combustflame. 2012.05.013
A. Farooq, W. Ren, K. Lam, D. F. Davidson, R. K. Hanson, C. K. Westbrook. Shock tube studies of methyl butanoate pyrolysis with relevance to biodiesel. The Journal of
Combustion and Flame, 159(11):3235-3241, Nov 2012.
""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)

entry(
	index = 2,
	reactant1 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
BAOJ
1 C 0 {2,S} {6,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 1 {3,S}
6 C 0 {1,S}
""",
	product2 = 
"""
CH3
1 C 1
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (30000000000000.0, 's^-1'),
		n = 0,
		Ea = (0.0, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)

entry(
	index = 3,
	reactant1 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
CH3OCO
1 C 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
""",
	product2 = 
"""
C3H7
1 C 0 {2,S}
2 C 0 {1,S} {3,S}
3 C 1 {2,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (18100000000000.0, 's^-1'),
		n = 0.0,
		Ea = (0.0, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)

entry(
	index = 4,
	reactant1 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
MP3J
1 C 0 {2,S} {6,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 C 0 {4,S}
6 C 1 {1,S}
""",
	product2 = 
"""
CH3
1 C 1
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (10000000000000.0, 's^-1'),
		n = 0.0,
		Ea = (0.0, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)


entry(
	index = 5,
	reactant1 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
C3H7CO
1 C 0 {2,S} {5,S}
2 C 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 C 0 {1,S}
""",
	product2 = 
"""
CH3O
1 O 1 {2,S}
2 C 0 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (30000000000000.0, 's^-1'),
		n = 0.0,
		Ea = (0.0, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)



entry(
	index = 6,
	reactant1 = 
"""
Hj
1 H 1
""",
	reactant2 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
	product2 = 
"""
MB2J
1 C 0 {2,S} {7,S}
2 C 1 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(A=(31800, 'cm^3/(mol*s)'), n=2.8, Ea=(2.276, 'kcal/mol'), T0=(1, 'K')),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""
H-abstraction
""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)

entry(
	index = 7,
	reactant1 = 
"""
Hj
1 H 1
""",
	reactant2 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
	product2 = 
"""
MBMJ
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 1 {5,S}
7 C 0 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(A=(961, 'cm^3/(mol*s)'), n=3.3, Ea=(3.940, 'kcal/mol'), T0=(1, 'K')),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""
H-abstraction
""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)
entry(
	index = 8,
	reactant1 = 
"""
Hj
1 H 1
""",
	reactant2 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
	product2 = 
"""
MB4J
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 1 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=3, Ea=(4.290, 'kcal/mol'), T0=(1, 'K')),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""
H-abstraction
""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)
entry(
	index = 9,
	reactant1 = 
"""
Hj
1 H 1
""",
	reactant2 = 
"""
MB
1 C 0 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
	product2 = 
"""
MB3J
1 C 1 {2,S} {7,S}
2 C 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {5,S}
4 O 0 {3,D}
5 O 0 {3,S} {6,S}
6 C 0 {5,S}
7 C 0 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(A=(495000, 'cm^3/(mol*s)'), n=2.5, Ea=(3.261, 'kcal/mol'), T0=(1, 'K')),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""
H-abstraction
""",
	history = [
		("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
	],
)
entry(
	index = 10,
	reactant1 = 
"""
CH3OCO
1 C 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
""",
	product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
	product2 = 
"""
CH3
1 C 1
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (1550000000000.0, 's^-1'),
		n = 0.5,
		Ea = (15.174, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
			("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
		],
	)
	
entry(
	index = 11,
	reactant1 = 
"""
CH3OCO
1 C 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
""",
	product1 = 
"""
CO
1 C 0 {2,D}
2 O 0 {1,D}
""",
	product2 = 
"""
CH3O
1 O 1 {2,S}
2 C 0 {1,S}
""",
	degeneracy = 1,
	kinetics = Arrhenius(
		A = (7370000000000.0, 's^-1'),
		n = 0.5,
		Ea = (23.793, 'kcal/mol'),
		T0 = (1, 'K'),
	),
	reference = None,
	referenceType = "",
	shortDesc = u"""""",
	longDesc = 
u"""

""",
	history = [
			("Mon May 6 11:13:30 2013","Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> imported this entry from the Huynh model."""),
		],
	)
	