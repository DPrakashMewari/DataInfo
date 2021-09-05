import pandas as pd

class Datainfo:
    def __init__(self,filename):
        self.filename = filename
        file=pd.read_csv(self.filename)
        print("File Shape :",file.shape)
        print("-----" * 4)
        print("File Size :",file.size)
        print("-----" * 4)
        count = [file[x].value_counts() for x in file.columns]
        print("File Columns Frequency:",count)
        print("-----" * 4)
        print("Data Types Info:",file.info())
        print("-----"*4)
        print("Total Null Values Are",file.isna().sum())
        print("-----" * 4)
        unique = [file[x].value_counts().nunique() for x in file.columns]
        print("Unique value in Different Columns",unique)
        print("------" * 4)
        print("Data Description",file.describe())



def main(file=input()):
    obj=Datainfo(file)

if __name__ == "__main__":
    main()
