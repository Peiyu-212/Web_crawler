import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NewsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = 'AddNews'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.group_name, {"type": "message", "message": message}
        )

    # Receive message from group
    async def send_new_data(self, event):
        text = event["text"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"text": text}))
