import pandas as pd
import os
class Compare:
    def __init__(self):
        pass
    def compare(self, file_1, file_2):
        
        read_file_1 = pd.read_excel(file_1)
        read_file_2 = pd.read_excel(file_2)

        read_file_1 = read_file_1.sort_index(axis=1)
        read_file_2 = read_file_2.sort_index(axis=1)

        all_cols = read_file_1.columns.union(read_file_2.columns)

        read_file_1 = read_file_1.reindex(columns= all_cols)
        read_file_2 = read_file_2.reindex(columns= all_cols)

        max_rows = max(len(read_file_1), len(read_file_2))

        read_file_1 = read_file_1.reindex(range(max_rows))
        read_file_2 = read_file_2.reindex(range(max_rows))

        
        result = read_file_1.compare(read_file_2)

        base_name_1 = os.path.basename(file_1)
        base_name_2 = os.path.basename(file_2)

        file_1_name , extension_1 = os.path.splitext(base_name_1)
        file_2_name , extension_2 = os.path.splitext(base_name_2)
        
       
        result.to_excel(file_1_name + '_' + file_2_name + '.xlsx')
        return file_1_name + '_' + file_2_name + '.xlsx'
