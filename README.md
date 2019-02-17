# Read-and-Write-RINEX-observation-files
Convert RINEX data files to a dictionnary easy to use.
This script, creates a class called RNX, with 3 parameters: RINEX version, Observales, and the body data.

###### To launch the script
Go to the terminal, go to the script directory, type "python RNX.py /yourRINEXfileDIRECTORY/YourRINEXfile"
You will have in the output all the parameters as listed above

###### Important:
      1- Class def:
           class RNX:
            def __init__(self,version, ConstellationObservables, EpochPrnData):
	            self.version = version
              self.ConstellationObservables = ConstellationObservables
              self.EpochPrnData = EpochPrnData
     2- Version:
            type str("2.0" up to "3.03")
     3- ConstellationObservables:
            type dictionnary: keys   = Contellation ('G':GPS, 'E':Galille, etc)
                              values = List of observables ('C1C', 'L2C', 'S1C',etc)
    4- EpochPrnData:
            type dictionnary: keys = epochs (float between 0 to 86399)
                              values = dictionnary: keys   : PRNs ('G03','E12', etc)
                                                    values : Record (list of DATA)
                                                    
                                                    

