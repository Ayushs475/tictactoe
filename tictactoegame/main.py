from flask import Flask,jsonify,request
from day3_3 import player_request,table

app = Flask(__name__)

list1=[]

@app.route('/player',methods=["POST"])
def player():
    request_data=request.get_json()
    player1_name=request_data['player1']
    player1_symbol=request_data['symbol1']
    player2_name=request_data['player2']
    player2_symbol=request_data['symbol2']
    list1.append(player1_name)
    list1.append(player1_symbol)
    list1.append(player2_name)
    list1.append(player2_symbol)
    
    return 'ok'
    
@app.route('/winner',methods=["POST"]) 
def winner():
        
    winner=player_request(list1[0],list1[1],list1[2],list1[3])
    
    

    if winner == list1[1]:
        return f"Players_Names = {list1[0], list1[2]} \n" \
               f"Players_Symbol = {list1[1], list1[3]} \n" \
               f"The winner of the game 'TIC-Tac-Toa' is '{list1[0]}' "
    if winner == list1[2]:
        return f"Players_Names = {list1[0], list1[2]} \n" \
               f"Players_Symbol = {list1[1], list1[3]} \n" \
               f"The winner of the game 'TIC-Tac-Toa' is '{list1[2]}' "   
               
    if '_' not in table: 
        return f"tie"
                       
               
               
if __name__ == "__main__": 
    
   app.run(host="0.0.0.0", port=3000, debug=True)