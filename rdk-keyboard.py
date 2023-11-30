import curses
import requests
import json
import argparse

def ascii_to_vk(code):
	# Map ASCII codes to virtual-key codes
	if 65 <= code <= 90:  # A-Z
		return code,chr(code)
	elif 48 <= code <= 57:  # 0-9
		return code,chr(code)
	elif code == 13:  # Enter
		return 13,'Enter'
	elif code == 10:  # Enter
		return 13,'Enter'
	elif code == 8:  # Backspace
		return 8,'Backspace'
	elif code == 9:  # Tab
		return 9,'Tab'
	elif code == curses.KEY_BACKSPACE:
		return 8,'Backspace'
	elif code == curses.KEY_HOME:
		return 36,'Home'
	# Arrow keys
	elif code == curses.KEY_LEFT:
		return 37,'Left'
	elif code == curses.KEY_UP:
		return 38,'Up'
	elif code == curses.KEY_RIGHT:
		return 39,'Right'
	elif code == curses.KEY_DOWN:
		return 40,'Down'
	# Esc key
	elif code == 27:  # Escape
		return 27,'Escape'
	# Add more key mappings as needed
	else:
		return None,'None'  # No corresponding virtual-key code

def main(stdscr):
	# make getch non-blocking
	stdscr.nodelay(True)

	while True:
		c = stdscr.getch()
		if c != -1:
			# Print key code
			stdscr.clear()
			virtual_keycode,keycode_str = ascii_to_vk(c)
			stdscr.addstr(keycode_str+'\n')
			stdscr.refresh()

			if(virtual_keycode!=None):
					# Send POST request
					headers = {'Content-Type': 'application/json'}
					data = {
						"jsonrpc": "2.0",
						"id": 3,
						"method": "org.rdk.RDKShell.1.injectKey",
						"params": {
							"keyCode": virtual_keycode
						}
					}
					response = requests.post('http://'+RDK_IP+'/jsonrpc', headers=headers, data=json.dumps(data))

					# Print response
					stdscr.addstr(str(response.json()))

parser = argparse.ArgumentParser(description="Keyboard for RDK")
parser.add_argument('IP', help='The RDK IP (mandatory). Ex: python3 rdk-keyboard.py 192.168.0.200', type=str)
parser.add_argument('--port', type=int, default=9998, help='RDK\'s Port number to connect (Default: 9998)')
args = parser.parse_args()
RDK_IP = args.IP + ":" + str(args.port)
curses.wrapper(main)
