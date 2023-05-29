import websocket

def on_open(ws):
    print("Opened WebSocket connection")

def on_message(ws, message):
    print("Received message: %s" % message)

def on_error(ws, error):
    print("Error: %s" % error)
    
# Create a WebSocket client
ws = websocket.WebSocketApp("wss://rawwater-ahl1phuiph.shellweplayaga.me/live/websocket?_csrf_token=MDgxIw8RcQ8cYDs0HSEMJT4ZDSMQNStRapgB8pG_U4kmIPtuOmJNS_s4&_track_static%5B0%5D=https%3A%2F%2Frawwater-ahl1phuiph.shellweplayaga.me%2Fdatabase%2F&_track_static%5B1%5D=https%3A%2F%2Frawwater-ahl1phuiph.shellweplayaga.me%2Fdatabase%2F&_mounts=0&_live_referer=undefined&vsn=2.0.0",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error)

# Start the WebSocket client
ws.run_forever()

ws.send("Hello!")
