# CLIMessagingApp
A simple messaging application that allows users to message each other


## Getting Your Server Up and Running Manually
```bash
cd ./phase1/Scripts
source activate
pip install requirements.txt 
npm install wscat
npm install -g localtunnel
cd src
flask --app app.py run
```

## Local Server will run at http://127.0.0.1:5000


```bash
wscat -c http://127.0.0.1:5000/connect
```

## Port Forwarded Local Server:
```bash
lt --port 5000 --subdomain chat

wscat -c https://chat.localtunnel.me/connect
```

