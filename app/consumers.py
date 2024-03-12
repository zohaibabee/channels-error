from channels.consumer import SyncConsumer,AsyncConsumer


class SyncChatConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("connected",event)
        self.send({
            "type":"websocket.accept"
        })
        
    # Receive message from client
    def websocket_receive(self, event):
        print('message recived',event)
        
        
    def websocket_disconnect(self,event):
        print('Disconnected',event)  
        
        
        
        
          
#---------------------------------------------------------------
# class AsyncChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("Connected",event)

#     async def websocket_receive(self, event):
#          print('message recived',event)
        
#     async def websocket_disconnect(self,event):
#          print('Disconnected',event)  