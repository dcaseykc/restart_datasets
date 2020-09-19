import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('all_data_M_2019.xlsx')
    states = list(set(df[df['area_type'] == 2]['area_title']))
    counties = df[(df['area_type'] == 4) & (df['naics'] == '000000')][
        ['area', 'area_title', 'occ_code', 'occ_title', 'o_group', 'tot_emp']]
    for state in states:
        state_df = df[df['area_title'] == state][['occ_code', 'occ_title', 'o_group', 'tot_emp', 'area']]
        st = state.title().replace(' ', '') + '.csv'
        state_df.to_csv(st)
