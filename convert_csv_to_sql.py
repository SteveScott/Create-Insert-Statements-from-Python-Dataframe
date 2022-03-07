##### A CLI script to read a csv and convert it into SQL INSERT INTO statements. #####
##### Takes as an input the CSV name and the CSV target (the name of the table   #####
##### you are inserting into).                                                   #####
##### The fuction sql_insert_statements_from_df() can also be taken in part to   #####
##### convert any pandas dataframe into SQL INSERT INTO statements.              #####


import pandas as pd
from pathlib import Path

def main():
    filename = input("input file name to read: ")
    target = input("input table name: ")
    df = pd.read_csv(Path.cwd() / filename, skiprows=0)
    input_statements = sql_insert_statements_from_df(df, target)
    with open(target + '.sql', 'w') as f:
        f.writelines(input_statements)

def sql_insert_statements_from_df(df, target):
    sql_statements = []
    for index, row in df.iterrows():
        this_statement = f"INSERT INTO {target} ({str(', '.join(df.columns))}) VALUES {str(tuple(row.values))};\n"
        this_statement = this_statement.replace("nan", 'NULL'.strip())
        sql_statements.append(this_statement)
    return sql_statements
    
if __name__ == "__main__":
    main()
