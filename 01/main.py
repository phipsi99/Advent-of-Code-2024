from pathlib import Path

def do_main():
    with open(Path('01/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    point_sum = 0

    import pandas as pd

    data = []

    for line_index, line in enumerate(lines):
        x, y = line.split("   ")
        
        data.append({
            "x": x.strip(),
            "y": y.strip()
        })

    # Create the DataFrame from the data list
    df = pd.DataFrame(data)

    df_sorted_x = df.sort_values(by='x')
    df_sorted_y = df.sort_values(by='y')

    df_sorted_xy = pd.DataFrame({
        'x': df_sorted_x['x'].values,
        'y': df_sorted_y['y'].values
    })

    df_sorted_xy['diff'] = abs(df_sorted_xy['x'].astype(float) - df_sorted_xy['y'].astype(float))

    sum = df_sorted_xy['diff'].sum()
    
    print(sum)

    sum2  = 0

    for num in df_sorted_xy['x']:
        count = (df_sorted_xy['y'].astype(float) == int(num)).sum()
        sum2 += count *  int(num)

    print( sum2)

    

    


if __name__ == '__main__':
    do_main()