import pandas as pd
from one import get_points_for_sign_played, get_points_for_winning

def get_sign_from_outcome(a, o):
    if a == 'A':
        if o == 'X': # lose
            return 'Z'
        elif o == 'Y': # draw
            return 'X'
        elif o == 'Z': # win
            return 'Y'
    elif a == 'B':
        if o == 'X': # lose
            return 'X'
        elif o == 'Y': # draw
            return 'Y'
        elif o == 'Z': # win
            return 'Z'
    elif a == 'C':
        if o == 'X': # lose
            return 'Y'
        elif o == 'Y': # draw
            return 'Z'
        elif o == 'Z': # win
            return 'X'

if __name__ == '__main__':

    df = pd.read_csv('./day2/input.txt', sep=' ', names=['P1', 'Outcome'])

    df['P2'] = df.apply(lambda x: get_sign_from_outcome(x.P1, x.Outcome), axis=1)

    df['sign_points']    = df['P2'].apply(get_points_for_sign_played)
    df['winning_points'] = df.apply(lambda x: get_points_for_winning(x.P1, x.P2), axis=1)
    df['total_round_points'] = df['sign_points'] + df['winning_points']

    print(df.head())
    print()
    print(df['total_round_points'].sum())