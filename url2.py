import urlextraction
import re
import pandas as pd

    
frame={'Digit':urlextraction.obj.digit,
       'Alphabet':urlextraction.obj.alpha}

def dataframe(frame):
    
    tabular=pd.DataFrame(frame)

    return tabular

Dataframe=dataframe(frame)
print(Dataframe)

