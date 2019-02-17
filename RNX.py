import numpy as np
import sys
import os.path



#Directory of RINEX FILE
RINEX = sys.argv[1]



class RNX:
  def __init__(self,version, ConstellationObservables, EpochPrnData):
	self.version = version
    self.ConstellationObservables = ConstellationObservables
    self.EpochPrnData = EpochPrnData
    
#Name: RINEX3CONSTOBS
#Purpose: from a RINEX obs File extraxt the constellation and the observables as a dictionnary and give 
##########the index of the line when the header ends

def RINEX3CONSTOBS(obs):
    # Initialization of the output dictionary
    ConstellationObservables = dict()

    # Get the file name of the input RINEX file
    obsFileName = obs

    ''' The reading step of the input files '''
    with open(obsFileName, "r+") as obsFd:

        # Read lines of files
        obsLines = obsFd.readlines()
	#version
	version = obsLines[0].split()[0]
        # Initialisation of the list containing the observables the will be the value
        Observables = []

        ''' header and body information'''

        # Loop on the lines
        for i in range(len(obsLines) - 1):

            obsLine1 = obsLines[i]  # current line

            obsLine2 = obsLines[i + 1]  # next line

            # If the end of the header is reached

            if "END OF HEADER" in obsLine1:

                counter = i  # The line where the body should start

            else:
                # Identification of the Constellation and the observables line
                if "SYS / # / OBS TYPES" in obsLine1:
                    # To know if the observables are written in one or two lines
                    if obsLine1[0] != ' ' and obsLine2[0] == ' ' and "SYS / # / OBS TYPES" in obsLine2:

                        Observables = Observables + (obsLine1[6:60]).split() + ((obsLine2[0:60]).split())

                        ConstellationObservables[obsLine1[0]] = (obsLine1[6:60]).split() + (obsLine2[0:60]).split()

                    elif obsLine1[0] != ' ' and "SYS / # / OBS TYPES" in obsLine1:

                        Observables = Observables + (obsLine1[6:60]).split()

                        ConstellationObservables[obsLine1[0]] = (obsLine1[6:60]).split()
		
                    # End of if " 2 lines check"
                # End of if "SYS / # / OBS TYPES"
            # End of end of header check

    return ConstellationObservables, counter, version

#Name : func
#Purpose: return a dictionnary with epochs as keys and the values are dictionnries with prns as keys and the values are the observations
def ConvertRnxToDict(obs):
	Rinex2Dict = dic()
	counter = RINEX3CONSTOBS(file)[1]
  	with open(RINEX,'r+') as fd:
	  	lines = fd.readlines()
	  	LineCounter = counter
	  	while LineCounter < len(lines):
		  	if ">" == lines[LineCounter][0]:
			  	EpochSec  = float(lines[LineCounter].split()[6])
			  	EpochMin  = float(lines[LineCounter].split()[5])
			  	EpochHour = float(lines[LineCounter].split()[4])
			  	Epoch     = EpochSec + 60.0*EpochMin + 60.0*60.0*EpochHour
			  	NumSat    = int(lines[LineCounter].split()[8])
			  	Rinex2Dict[Epoch]=dict()
			  	LineInEpochCounter = 1
			  	while LineInEpochCounter < NumSat+1:
				
			  		PRN  = lines[LineInEpochCounter+LineCounter].split()[0]
					Data = lines[LineInEpochCounter+LineCounter].split()[1:]
					Rinex2Dict[Epoch][PRN] = Data
					LineInEpochCounter+=1
					
			 	LineCounter = LineCounter + Numsat + 1
	return Rinex2Dict


constObs,ver= RINEX3CONSTOBS(RINEX)[0],RINEX3CONSTOBS(RINEX)[2]
EpchprnData = ConvertRnxToDict(RINEX)
Output = RNX(ver,constObs,EpchprnData)

				
				
				
