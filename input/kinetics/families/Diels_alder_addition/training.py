#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = 
"""
1  C 0 {2,S} {6,S} {10,S}
2  C 0 {1,S} {3,S} {9,S}
3  C 0 {2,S} {4,S} {8,S}
4  C 0 {3,S} {5,D} {7,S}
5  C 0 {4,D} {6,S}
6  O 0 {1,S} {5,S}
7  O 0 {4,S}
8  O 0 {3,S}
9  O 0 {2,S}
10 C 0 {1,S} {11,S}
11 O 0 {10,S}
""",
    product1 = 
"""
1 C 0 {2,D} {4,S} {6,S}
2 C 0 {1,D} {3,S}
3 O 0 {2,S}
4 C 0 {1,S} {5,D}
5 O 0 {4,D}
6 O 0 {1,S}

""",
    product2 = 
"""
1 C 0 {2,S} {5,S}
2 C 0 {1,S} {3,D}
3 C 0 {2,D} {4,S}
4 O 0 {3,S}
5 O 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A=(2.3e+13,'s^-1'),
        n=0.0,
        Ea=(44.6,'kcal/mol'),
        T0=(1,'K'),
        Tmin = (1000,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3, # MEANING UNKNOWN!
    shortDesc = u"""Hans-Heinrich Carstense et al. (2010) doi:10.1021/bk-2010-1052.ch010""",
    longDesc = 
u"""
 Electronic structure calculations at the CBS-QB3 method followed by the TST
 calculations yielded the following rate constants of reaction for the retro-
 Diels-Alder reaction (Taken from: Development of Detailed Kinetic Models for
the Thermal Conversion of Biomass via First Principle Methods and Rate Estimation
 Rules,Hans-Heinrich Carstense et al. (2010) doi:10.1021/bk-2010-1052.ch010 )
 
 Valid temperature range is from 286-2000 (where the paper mentioned).

""",
    history = [
        ("Thu Jan 7 15:39:30 2014","Fariba Seyedzadeh <seyedzadehkhanshan.fn@husky.neu.edu>","action","""Fariba Seyedzadeh <seyedzadehkhanshan.f@husky.neu.edu> created this entry."""),
    ],
)
