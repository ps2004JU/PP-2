import pandas as pd
a = {
    "name" :["Punya", "Rashid","Elvin"],
    "degree" : ["MCA","MA","BCA"]
}
d = pd.DataFrame(a,index=range(1,4))
print(d)
