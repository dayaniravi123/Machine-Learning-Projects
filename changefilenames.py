import os
import pandas as pd
os.chdir("/Users/arpankorat/Desktop/sartorius-cell-instance-segmentation")

with open('train.csv') as f:
    df = pd.read_csv(f)

    li = list(set(zip(df.id, df.cell_type)))

    x = []
    ast_count = 0
    shs_count = 0
    cort_count = 0
    for count, filename in enumerate(os.listdir('train')):
        if li[count][1] == 'astro':
            dst = f"astro{str(ast_count)}.png"
            ast_count += 1
            src = f"{'train'}/{filename}"
            dst = f"{'train'}/{dst}"
            os.rename(src, dst)
        elif li[count][1] == 'shsy5y':
            dst = f"shsy5y{str(shs_count)}.png"
            shs_count += 1
            src = f"{'train'}/{filename}"
            dst = f"{'train'}/{dst}"
            os.rename(src, dst)
        elif li[count][1] == 'cort':
            dst = f"cort{str(cort_count)}.png"
            cort_count += 1
            src = f"{'train'}/{filename}"
            dst = f"{'train'}/{dst}"
            os.rename(src, dst)
