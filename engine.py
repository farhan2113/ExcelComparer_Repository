import pandas as pd
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

      
        file_1_name = ''
        for char in reversed(file_1):
            if char not in '\/':
                file_1_name = char + file_1_name
            else:
                break
        

        file_2_name = ''
        for char in reversed(file_2):
            if char not in '\/':
                file_2_name = char + file_2_name
            else:
                break        

        if file_1_name[:-4] == '.xls':
            file_1_name = file_1_name[:-4]
        else:
            file_1_name = file_1_name[:-5]

        if file_2_name[:-4] == '.xls':
            file_2_name = file_2_name[:-4]
        else:
            file_2_name = file_2_name[:-5]
        
       
        result.to_excel(file_1_name + '_' + file_2_name + '.xlsx')
        return file_1_name + '_' + file_2_name + '.xlsx'
