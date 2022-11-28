from groupy.client import Client

def send(tk,id,message):
    #W9bfnlX5HPPUtH47BDviALDoKd10SWk7wNfd2CNN    
    #90585988
    client = Client.from_token(tk)    
    group = client.groups.get(id)    
    group.post(text=message)    