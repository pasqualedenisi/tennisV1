print("""
****************************
* TENNIS GAME TRACKER - v1 *
****************************
""".strip())

points = {
    'R': 0,
    'S': 0,
}

end=False
print("Running score: love-all")
while(not end):
    winner=input()
    if winner.lower()=='r':
        points['R']+=1
    elif winner.lower()=='s':
        points['S']+=1
    else:
        print("Wrong value ignored!")

    if points['R']==0: #valorizziamo i punti
        receiverPoint="love"
    elif points['R']==1:
        receiverPoint="15"
    elif points['R']==2:
        receiverPoint="30"
    else:
        receiverPoint="40"
    if points['S']==0:
        servingPoint="love"
    elif points['S']==1:
        servingPoint="15"
    elif points['S']==2:
        servingPoint="30"
    else:
        servingPoint="40"

    if points['R']>=3 or points['S']>=3: #almeno uno >= 3
        if points['R']==points['S']: #parita
            print("Running score: deuce")
        elif points['R'] >= 3 and points['S'] >= 3: #entrambi >= di tre
            if abs(points['R'] - points['S']) == 2: #vittoria
                end = True
                if points['R']>points['S']:
                    print("End of the game: Receiver player win")
                else:
                    print("End of the game: Serving player win")
            else: #vantaggio
                if points['R']>points['S']:
                    print("Running score: ad-out")
                elif points['R']<points['S']:
                    print("Running score: ad-in")
        else: #uno >=3 e l'altro no
            if abs(points['R'] - points['S']) >= 2:
                if points['R']>3: #vittoria
                    end = True
                    print("End of the game: Receiver player win")
                elif points['S']>3: #vittoria
                    end = True
                    print("End of the game: Serving player win")
                else:  #punteggio
                    print("Running score: %s-%s" % (servingPoint, receiverPoint))
            else: #punteggio
                print("Running score: %s-%s" % (servingPoint, receiverPoint))
    else: #entrambi < 3
        if points['S']==points['R']: #parita
            print("Running score: %s-all"%servingPoint)
        else: #punteggio
            print("Running score: %s-%s"%(servingPoint,receiverPoint))