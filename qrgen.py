import requests
import sys
import time
from colorama import Fore, Style, init

init(convert=True, autoreset=True)

if __name__ == '__main__':
	args = sys.argv

	if len(args) < 4:
		print('Usage: py qrgen.py [filename] [size (example: 512x512)] [data]')

	try:
		url = 'https://api.qrserver.com/v1/create-qr-code'
		data = ' '.join(args[3:])
		size = args[2]
		print(Fore.GREEN + f'Data: {data}' + f'\nSize: {size}')
		
		if ' ' in data:
			data = '%20'.join(data.split())
		
		r = requests.get(f'{url}/?size={size}&data={data}')
		
		if r.status_code == 200:
			fn = args[1]
			with open(f'{fn}.png', 'wb') as f:
				f.write(r.content)
				f.close()
			print(Fore.CYAN + f'\nSaved to "{fn}.png".')
	except IndexError:
		pass