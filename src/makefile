make server: 
	flask --app app.py run
make local: 
	wscat -c http://127.0.0.1:5000/connect
make port:
	lt --port 5000 --subdomain chat 
make global:
	wscat -c ws://chat.loca.lt/connect