# enovy-simple-demo
Simple envoy front/edge proxy example 

**Installations:**
**Envoy (https://www.envoyproxy.io/docs/envoy/latest/start/install):**
1) sudo apt update
2) sudo apt install apt-transport-https gnupg2 curl lsb-release
3) curl -sL 'https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key' | sudo gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg
4) echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check
5) echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/getenvoy.list
6) sudo apt update
7) sudo apt install -y getenvoy-envoy

**Python venv for services:**
python3 -m venv venv


**Running services:**
1) Activate python venv by running following command
2) "source venv/bin/activate"
3) Navigate to book_service/stationaries service
4) To install required package, run "pip install -r requirements.txt"
5) Run "python app.py" to start service

**Running envoy:**
1) Naviagate to envoy-simple demo
2) Run "envoy -c <path to config file>" e.g. envoy -c stationay-envoy-demo.yaml

**Accessing service via envoy proxy:**
1) Run "curl -v localhost:9001/stationaries". This should return response from stationaries service.
2) Run "curl -v localhost:9001/books". This should return response from books service.
3) Alternatively, request could be made using browser as well. (Note: port 9001 should be allowed to be accessed from requesting machine).
