make server: 
	flask --app app.py run
make local: 
	wscat -c http://127.0.0.1:5000/connect;
make global:
	lt --port 5000 --subdomain chat; wscat -c https://chat.localtunnel.me/connect;