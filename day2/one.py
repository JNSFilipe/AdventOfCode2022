import pandas as pd

def get_points_for_sign_played(x):
    if x == 'X':
        return 1
    elif x == 'Y':
        return 2
    elif x == 'Z':
        return 3

def get_points_for_winning(a,x):
    winning = ((x=='X') and (a=='C')) or ((x=='Y') and (a=='A')) or ((x=='Z') and (a=='B'))
    drawing = ((x=='X') and (a=='A')) or ((x=='Y') and (a=='B')) or ((x=='Z') and (a=='C'))
    if winning:
        return 6
    elif drawing:
        return 3
    else:
        return 0

if __name__ == '__main__':

    df = pd.read_csv('./day2/input.txt', sep=' ', names=['P1', 'P2'])

    df['sign_points']    = df['P2'].apply(get_points_for_sign_played)
    df['winning_points'] = df.apply(lambda x: get_points_for_winning(x.P1, x.P2), axis=1)
    df['total_round_points'] = df['sign_points'] + df['winning_points']

    print(df.head())
    print()
    print(df['total_round_points'].sum())