# CLIMessagingScrapperApp
A simple messaging application that allows users to message each other. It can also scrape News and Nba Information for generating datasets. 


## Installing Dependencies
```
pip install requirements.txt 
npm install wscat
npm install -g localtunnel 
```
## Getting Your Server Up and Running Manually
```bash
cd src
flask --app app.py run
```

## Local Server will run at http://127.0.0.1:5000


```bash
wscat -c ws://127.0.0.1:5000/connect
```

## Port Forwarded Local Server:
```bash
lt --port 5000 --subdomain chat

wscat -c ws://chat.localtunnel.me/connect
```

## Using Makefiles
```makefile
#generates local server
make server

#deploys locally
make local

#deploys command line messaging scraper app 
make port 
make global

```

