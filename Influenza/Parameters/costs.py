# Parameter values for the costs
from PiecewiseAgeParameter import PiecewiseAgeNumber, PiecewiseAgeRate
import demography

import numpy


#:
#: +--------------------------------------------------+-----------------------+
#: | Case Hospitalization                             | Reference             |
#: +==================================================+=======================+
#: | 0.0141 (SD 0.0047) (Ages 0--4)                   | Molinari et al., 2007 |
#: +--------------------------------------------------+                       |
#: | 0.0006 (SD 0.0002) (Ages 5--17)                  |                       |
#: +--------------------------------------------------+                       |
#: | 0.0042 (SD 0.0014) (Ages 18--49)                 |                       |
#: +--------------------------------------------------+                       |
#: | 0.0193 (SD 0.0064) (Ages 50--64)                 |                       |
#: +--------------------------------------------------+                       |
#: | 0.0421 (SD 0.0140) (Ages 65+)                    |                       |
#: +--------------------------------------------------+-----------------------+
#: | 0.0245 (95% CI: 0.0110--0.0556) (Ages 0--4)      | Preanis et al., 2009  |
#: +--------------------------------------------------+                       |
#: | 0.0033 (95% CI: 0.0021--0.0063) (Ages 0--4)      |                       |
#: +--------------------------------------------------+                       |
#: | 0.0061 (95% CI: 0.0027--0.0134) (Ages 5--17)     |                       |
#: +--------------------------------------------------+                       |
#: | 0.0011 (95% CI: 0.0008--0.0018) (Ages 5--17)     |                       |
#: +--------------------------------------------------+                       |
#: | 0.0300 (95% CI: 0.0135--0.0592) (Ages 18--64)    |                       |
#: +--------------------------------------------------+                       |
#: | 0.0015 (95% CI: 0.0011--0.0025) (Ages 18--64)    |                       |
#: +--------------------------------------------------+                       |
#: | 0.0184 (95% CI: 0.0021--0.2538) (Ages 65+)       |                       |
#: +--------------------------------------------------+                       |
#: | 0.0016 (95% CI: 0.0010--0.0030) (Ages 65+)       |                       |
#: +--------------------------------------------------+-----------------------+
#:
caseHospitalizationPW = PiecewiseAgeRate(
    [numpy.random.triangular(0.0033, 0.0141, 0.0245),
     numpy.random.triangular(0.0006, 0.0011, 0.0061),
     numpy.random.triangular(0.0015, 0.0042, 0.0300),
     numpy.random.triangular(0.0015, 0.0193, 0.0300),
     numpy.random.triangular(0.0016, 0.0184, 0.0421)],
    [0, 5, 18, 50, 65])



#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5081294/#S2: 0.131
#Burden of Communicable Diseases in Europe Project 2015: 0.051 (and IHME)
#http://www.rivm.nl/bibliotheek/rapporten/appendix150205001.pdf: for acute infection=
disabilityWeight= 0.051


#: For years of life lost. 
#: From US Life Tables 2014
expectationOfLifePW = PiecewiseAgeNumber(
    [78.9,78.3,74.4,69.5,64.5,59.7,54.9,50.2,45.4,40.7,36.1,31.7, 27.4,23.3,19.4,15.7,12.3,9.2,6.7,4.6,3.2,2.3],
    [0,1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])


