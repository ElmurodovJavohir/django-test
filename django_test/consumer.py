from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)("hello", self.channel_name)

        headers = dict(self.scope["headers"])

        self.user = None
        if b"user" in headers:
            self.user = str(headers[b"user"])

        if self.user:
            async_to_sync(self.channel_layer.group_send)(
                "hello",
                {"type": "chat_message", "message": f"{self.user} online bo'ldi"},
            )
            self.accept()

        else:
            # don't accept connection if user is not logged in
            self.close()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_send)(
            "hello",
            {"type": "chat_message", "message": f"{self.user} offline bo'ldi"},
        )
        async_to_sync(self.channel_layer.group_discard)("hello", self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            "hello",
            {"type": "chat_message", "message": f"{self.user} yozdi:{text_data}"},
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=message)
