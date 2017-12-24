# -*- coding: iso-8859-1 -*-
#
# Epidemiological parameter values
#

from PiecewiseAgeParameter import PiecewiseAgeRate
import numpy

numpy.random.seed()
#:
#: +-----------------------------------------------+------------------------+
#: | Infectious Period                             | Reference              |
#: +===============================================+========================+
#: | 2.5  (range 1.1--4.0)                         | Balcan et al., 2009    |
#: +-----------------------------------------------+------------------------+
#: | 3.8  (range 3.1--4.6)                         | Cauchemez et al., 2004 |
#: +-----------------------------------------------+------------------------+
#: | 3.4 � 0.8                                     | Moritz et al., 1980    |
#: +-----------------------------------------------+------------------------+
#: | 2.3 � 1.4                                     | Reeve et al., 1980     |
#: +-----------------------------------------------+------------------------+
#: | 4.1                                           | Longini et al., 2004   |
#: +-----------------------------------------------+------------------------+
#:
recoveryRatePW = PiecewiseAgeRate(
    [1. / numpy.random.triangular(0.9, 2.5, 4.6)],
    [0])


#:
#: +-----------------------------------------------+------------------------+
#: | Latent Period                                 | Reference              |
#: +===============================================+========================+
#: | 1.1  (range 1.1--2.5)                         | Balcan et al., 2009    |
#: +-----------------------------------------------+------------------------+
#: | 1.9                                           | Elveback et al., 1976  |
#: +-----------------------------------------------+------------------------+
#: | 2.0                                           | Moser et al., 1979     |
#: +-----------------------------------------------+------------------------+
#: | 2.0                                           | Yang et al., 2009      |
#: +-----------------------------------------------+------------------------+
#: | 2.5                                           | Shinde et al., 2009    |
#: |                                               | (NSOIAHN, 2009)        |
#: +-----------------------------------------------+------------------------+
#:
latencyRatePW = PiecewiseAgeRate(
    [1. / numpy.random.triangular(1.1, 2.0, 2.5)],
    [0])


#:
#: From "H1N1 Modeling Parameters with High Risk Data 8-18-09 with asthma.xls"
#:
#: +----------------+-------------------+
#: | Ages           | Proportion Immune |
#: +================+===================+
#: | 0--4           | 0.0%              |
#: +----------------+-------------------+
#: | 5--24          | 2.0%              |
#: +----------------+-------------------+
#: | 25--49         | 6.0%              |
#: +----------------+-------------------+
#: | 50--64         | 9.0%              |
#: +----------------+-------------------+
#: | 65+            | 34.0%             |
#: +----------------+-------------------+
#:
susceptibilityPW = PiecewiseAgeRate(
    [numpy.random.uniform(0.9, 1.),
     numpy.random.uniform(0.7, 1.),
     numpy.random.uniform(0.6, 1.),
     numpy.random.uniform(0.5, 1.),
     numpy.random.uniform(0.3, 1)],
    [0, 5, 25, 50, 65])




#: Placeholder value.  Set later by fixing R0.
transmissibilityPW = PiecewiseAgeRate(
    [1.],
    [0])


#: 
#: +-----------------------------------------------+------------------------+
#: | Vaccine Efficacy Vs Infection                 | Reference              |
#: +===============================================+========================+
#: | 91.4 (95% CI 63.8--98.0) (ages 1--15) (H1N1)  | Neuzil et al., 2001    |
#: +-----------------------------------------------+                        |
#: | 43.6 (95% CI -3.5--69.2) (ages 1--5) (H1N1)   |                        |
#: +-----------------------------------------------+                        |
#: | 76.1 (95% CI 53.0--87.9) (ages 6--10) (H1N1)  |                        |
#: +-----------------------------------------------+                        |
#: | 80.5 (95% CI 46.6--92.9) (ages 11--15) (H1N1) |                        |
#: +-----------------------------------------------+                        |
#: | 67.1 (95% CI 51.1--77.8) (ages 1--15) (H1N1)  |                        |
#: +-----------------------------------------------+                        |
#: | 77.3 (95% CI 20.3--93.5) (ages 1--15) (H3N2)  |                        |
#: +-----------------------------------------------+                        |
#: | 48.5 (95% CI -38.5--80.7) (ages 1--5) (H3N2)  |                        |
#: +-----------------------------------------------+                        |
#: | 73.8 (95% CI 37.4--89.1) (ages 6--10) (H3N2)  |                        |
#: +-----------------------------------------------+                        |
#: | 70.4 (95% CI -1.2--91.4) (ages 11--15) (H3N2) |                        |
#: +-----------------------------------------------+                        |
#: | 65.5 (95% CI 39.1--80.4) (ages 1--15) (H3N2)  |                        |
#: +-----------------------------------------------+------------------------+
#: | 65                                            | Waldman et al., 1972   |
#: +-----------------------------------------------+------------------------+
#: | 51 (Children)                                 | WHO, 2009              |
#: +-----------------------------------------------+                        |
#: | 56 (Adults)                                   |                        |
#: +-----------------------------------------------+                        |
#: | 42 (Elderly)                                  |                        |
#: +-----------------------------------------------+------------------------+
#: | 71                                            | CDC ACIP, 2009         |
#: +-----------------------------------------------+                        |
#: | 77                                            |                        |
#: +-----------------------------------------------+------------------------+
#: | 60--90 (Children)                             | Nichol et al., 2003    |
#: +-----------------------------------------------+                        |
#: | 70--90 (Adults)                               |                        |
#: +-----------------------------------------------+                        |
#: | 50--60 (Elderly)                              |                        |
#: +-----------------------------------------------+------------------------+
#: | 65 (45--77) (Children)                        | Negri et al., 2005     |
#: +-----------------------------------------------+                        |
#: | 63 (43--76) (Children)                        |                        |
#: +-----------------------------------------------+------------------------+
#: | 90 (Children)                                 | Longini et al., 2000   |
#: +-----------------------------------------------+                        |
#: | 85 (Children)                                 |                        |
#: +-----------------------------------------------+                        |
#: | 95 (95% CI 89--98) (Children)                 |                        |
#: +-----------------------------------------------+                        |
#: | 95 (95% CI 89--98) (Children)                 |                        |
#: +-----------------------------------------------+                        |
#: | 94 (95% CI 89--97) (Children)                 |                        |
#: +-----------------------------------------------+                        |
#: | 100 (95% CI NA) (Children)                    |                        |
#: +-----------------------------------------------+                        |
#: | 89 (95% CI 81--94) (Children)                 |                        |
#: +-----------------------------------------------+                        |
#: | 90 (95% CI 82--94) (Children)                 |                        |
#: +-----------------------------------------------+                        |
#: | 90 (95% CI 83--94) (Children)                 |                        |
#: +-----------------------------------------------+------------------------+
#: 

##vaccines not given to <6month old. 
relative_vaccineEfficacyVsInfectionPW = PiecewiseAgeRate(
    [0,
     numpy.random.triangular(0.4, 0.7, 1.),
     numpy.random.triangular(0.5, 0.7, 0.9),
     numpy.random.triangular(0.4, 0.5, 0.6)],
    [0,
     0.5,
     16,
     65])


# source :  https://www.cdc.gov/flu/fluvaxview/index.htm	
#------------------------------------------------------------
#Year	|  6m-4y    |5y - 17y  | 18y-49y |50y - 64y|	65y+|
#-----------------------------------------------------------
#2012-13|	69.8|	53.1   | 31.1	 |45.1	   |	66.2
#2013-14|	70.4|	55.3   |32.3	 |45.3     |	65
#2014-15|	70.4|	55.8   |33.5	 |47	   |	66.7
#2015-16|	70  |	55.9   |32.7	 |43.6	   | 	63.4
#2016-17|	70  | 	55.6   |33.6	 |45.4	   |	65.3
#----------------------------------------------------------					
					
relative_coveragePW = PiecewiseAgeRate(
	[0.7012, 0.5514, 0.3264, 0.4528, 0.6532],
	[0.6, 5, 18, 45, 65])


#: 
#: +-----------------------------------------------+------------------------+
#: | Vaccine Efficacy Vs Mortality                 | Reference              |
#: +===============================================+========================+
#: | 50 (95% CI 45--56) (Elderly)                  | Nichol et al., 2003    |
#: +-----------------------------------------------+                        |
#: | 68 (95% CI 56--76) (Elderly)                  |                        |
#: +-----------------------------------------------+------------------------+
#: | 40, 75 (0--19)                                | Meltzer et al., 1999   |
#: +-----------------------------------------------+                        |
#: | 40, 70 (20--64)                               |                        |
#: +-----------------------------------------------+                        |
#: | 30, 60 (65+)                                  |                        |
#: +-----------------------------------------------+------------------------+
#:
vaccineEfficacyVsDeathPW = PiecewiseAgeRate(
    [numpy.random.uniform(0.4, 0.75),
     numpy.random.uniform(0.4, 0.7),
     numpy.random.uniform(0.3, 0.7)],
    [0,
     20,
     65])

#:
#: +-----------------------------------------------+------------------------+
#: | Proportion High Risk                          | Reference              |
#: +===============================================+========================+
#: | 0.0415 (SE 0.0044) + 0.0002 (Ages 0.5--1)     | Zimmerman et al., 2010 |
#: +-----------------------------------------------+                        +
#: | 0.0883 (SE 0.0051) + 0.0003 (Ages 2--4)       |                        |
#: +-----------------------------------------------+                        +
#: | 0.1168 (SE 0.0030) + 0.0024 (Ages 5--18)      |                        |
#: +-----------------------------------------------+                        +
#: | 0.1235 (SE 0.0055) + 0.0068 (Ages 19--24)     |                        |
#: +-----------------------------------------------+                        +
#: | 0.1570 (SE 0.0027) + 0.0131 (Ages 25--49)     |                        |
#: +-----------------------------------------------+                        +
#: | 0.3056 (SE 0.0044) + 0.0327 (Ages 50--64)     |                        |
#: +-----------------------------------------------+                        +
#: | 0.4701 (SE 0.0050) + 0.0614 (Ages 65+)        |                        |
#: +-----------------------------------------------+------------------------+
#:


#:
#: +--------------------------------------------------+-----------------------+
#: | Case Mortality                                   | Reference             |
#: +==================================================+=======================+
#: | 0.00004 (SD 0.00001) (Ages 0--4)                 | Molinari et al., 2007 |
#: +--------------------------------------------------+                       |
#: | 0.00001 (SD 0.00000) (Ages 5--17)                |                       |
#: +--------------------------------------------------+                       |
#: | 0.00009 (SD 0.00003) (Ages 18--49)               |                       |
#: +--------------------------------------------------+                       |
#: | 0.00134 (SD 0.00045) (Ages 50--64)               |                       |
#: +--------------------------------------------------+                       |
#: | 0.01170 (SD 0.00390) (Ages 65+)                  |                       |
#: +--------------------------------------------------+-----------------------+
#: | 0.00026 (95% CI: 0.00006--0.00092) (Ages 0--4)   | Preanis et al., 2009  |
#: +--------------------------------------------------+                       |
#: | 0.00002 (95% CI: 0.00001--0.00011) (Ages 0--4)   |                       |
#: +--------------------------------------------------+                       |
#: | 0.00010 (95% CI: 0.00003--0.00031) (Ages 5--17)  |                       |
#: +--------------------------------------------------+                       |
#: | 0.00002 (95% CI: 0.00000--0.00004) (Ages 5--17)  |                       |
#: +--------------------------------------------------+                       |
#: | 0.00159 (95% CI: 0.00066--0.00333) (Ages 18--64) |                       |
#: +--------------------------------------------------+                       |
#: | 0.00010 (95% CI: 0.00007--0.00016) (Ages 18--64) |                       |
#: +--------------------------------------------------+                       |
#: | 0.00090 (95% CI: 0.00008--0.01471) (Ages 65+)    |                       |
#: +--------------------------------------------------+                       |
#: | 0.00010 (95% CI: 0.00003--0.00025) (Ages 65+)    |                       |
#: +--------------------------------------------------+-----------------------+
#: | 0.0030--0.0060                                   | Fraser et al. 2009    |
#: +--------------------------------------------------+                       |
#: | 0.0003--0.0005                                   |                       |
#: +--------------------------------------------------+                       |
#: | 0.0090--0.0180                                   |                       |
#: +--------------------------------------------------+                       |
#: | 0.0008--0.0016                                   |                       |
#: +--------------------------------------------------+-----------------------+
#:
caseMortalityPW = PiecewiseAgeRate(
    [numpy.random.triangular(0.00002, 0.00004, 0.00026),
     numpy.random.triangular(0.00001, 0.00002, 0.00010),
     numpy.random.triangular(0.00009, 0.00010, 0.00159),
     numpy.random.triangular(0.00010, 0.00134, 0.00159),
     numpy.random.triangular(0.00010, 0.00090, 0.01170)],
    [0, 5, 18, 50, 65])





#:
#: +-----------------------------------------------+------------------------+
#: | R0 values                                     | Reference              |
#: +===============================================+========================+
#: | 1.75 (95% CI 1.64--1.88)                      | Balcan et al., 2009    |
#: +-----------------------------------------------+------------------------+
#: | 1.7 (range 1.5--1.8) (during school term)     | Cauchemez et al., 2008 |
#: +-----------------------------------------------+                        |
#: | 1.4 (range 1.3--1.6) (during school holidays) |                        |
#: +-----------------------------------------------+------------------------+
#: | 1.49 (95% CI 1.45--1.53) (Spring 1918 wave)   | Chowell et al., 2006   |
#: +-----------------------------------------------+                        |
#: | 3.75 (95% CI 3.57--3.93) (Fall 1918 wave)     |                        |
#: +-----------------------------------------------+------------------------+
#: | 1.39                                          | Gani et al., 2005      |
#: +-----------------------------------------------+                        |
#: | 1.55                                          |                        |
#: +-----------------------------------------------+                        |
#: | 1.65                                          |                        |
#: +-----------------------------------------------+                        |
#: | 1.70                                          |                        |
#: +-----------------------------------------------+                        |
#: | 2.0                                           |                        |
#: +-----------------------------------------------+                        |
#: | 2.2                                           |                        |
#: +-----------------------------------------------+------------------------+
#: | 2.98 (95% CI 2.73--3.25)                      | Chowell et al., 2007   |
#: +-----------------------------------------------+                        |
#: | 2.38 (95% CI 2.16--2.60)                      |                        |
#: +-----------------------------------------------+                        |
#: | 2.20 (95% CI 1.55--2.84)                      |                        |
#: +-----------------------------------------------+                        |
#: | 3.53 (95% CI 3.45--3.62)                      |                        |
#: +-----------------------------------------------+                        |
#: | 2.10 (95% CI 1.21--2.95)                      |                        |
#: +-----------------------------------------------+                        |
#: | 2.36 (95% CI 2.07--2.60)                      |                        |
#: +-----------------------------------------------+------------------------+
#: | 1.3--1.7                                      | Yang et al., 2009      |
#: +-----------------------------------------------+------------------------+
#:
## changed R0 range
R0 = numpy.random.triangular(1.2, 1.5, 2.0)
