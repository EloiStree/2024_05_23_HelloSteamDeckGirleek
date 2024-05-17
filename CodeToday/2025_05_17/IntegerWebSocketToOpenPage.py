import asyncio
import struct
import websockets
import webbrowser
from playsound import playsound
import os

# pip install --upgrade wheel
# pip install playsound
# pip install websockets
# pip install asyncio
# pip install struct
# pip install webbrowser


def function_play_sound(sound_file_path):
    
        try:
            playsound(sound_file_path,block=True)
        except:
            print("Error playing sound")


current_folder = os.getcwd()
print(f"Current execution folder path: {current_folder}")

def girleek_code_integer(integer_value):
    print(f"Received integer: {integer_value}")
    if(integer_value == 700):
        print("Pressing space")
    if(integer_value == 800):
        print("Releasing Space")

    if integer_value == 500:
        #function_play_sound('OhYeah.wav')
        print("Oh Yeah")
    if integer_value == 501:
        #function_play_sound('Aie.wav')
        print("Aie")
    if integer_value == 502:
        #function_play_sound('MiamMiam.wav')
        print("Miam Miam")
    if integer_value == 503:
        #function_play_sound('Pop.wav')
        print("Pop")

    if integer_value == 601:
        webbrowser.open('https://www.girleek.net')
    if integer_value == 602:
        webbrowser.open('https://translate.google.be/?hl=fr&sl=en&tl=fr&op=translate')
    if integer_value == 603:
        webbrowser.open('https://translate.google.be/?hl=fr&sl=fr&tl=en&op=translate')
    if integer_value == 604:
        webbrowser.open('https://lesjoiesducode.fr')
    if integer_value == 605:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')






## DONT TRY TO UNDERSTAND NOW......................
## WEB SOCKET SERVER CODE LISTENING TO INCOMING INT BYTES FROM CLIENT
## DONT TRY TO UNDERSTAND NOW......................

async def parse_message(message):
    try:
        # Attempt to unpack the message as an integer
        integer_value = struct.unpack('<i', message)[0]
        return integer_value
    except struct.error as e:
        print(f"Error parsing message: {e}")
        return None

async def handle_connection(websocket, path):
    async for message in websocket:
        # Parse the message
        integer_value = await parse_message(message)
        if integer_value is not None:
            response = f"Parsed integer: {integer_value}"
            girleek_code_integer(integer_value) 
        else:
            response = "Failed to parse message as integer."
        # Send the response back to the client
        await websocket.send(response)

async def main():
    async with websockets.serve(handle_connection, "localhost", 7073):
        print("WebSocket server started on ws://localhost:7073")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
