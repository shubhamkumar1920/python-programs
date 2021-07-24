d = {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
def orangecap(d):
     runs={}
     for match in d:
      for player in d[match]:
          score=d[match][player]
          if player in runs:
            runs[player]+=score
          else:
            runs[player]=score
      highest_run=max(list(runs.values()))
      for each in runs:
        if runs[each]==highest_run:
          return tuple((each,highest_run))
      print(orangecap(d))