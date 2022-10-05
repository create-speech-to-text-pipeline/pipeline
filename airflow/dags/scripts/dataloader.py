import uuid
import pandas as pd

class DataLoader:
    """A class for loading the data
    """
    def read_csv(self, path):
        """
        Read csv file and return dataframe
        Args:
            path: The path of the file
        Return:
            df: dataframe
        """
        df = pd.read_csv(path)
        return df
        
    def add_uuid(self, df):
        """
        Add uuid column in the dataframe
        Args:
            df: dataframe
        Return:
            df: A dataframe with uuid
        """
        df['uuid'] = [uuid.uuid4() for _ in range(len(df.index))]
        return df

    
        
    