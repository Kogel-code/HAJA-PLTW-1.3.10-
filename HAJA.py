team_name = 'HAJA'
strategy_name = 'Betray When Betrayed'
strategy_description = 'Will bretray if last move of opponent was betray'


def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history[-1:]:
        return 'b'
    else:   
        return 'c' 