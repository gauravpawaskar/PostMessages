update /etc/hosts as following
```bash
127.0.0.1       xyz.com
127.0.0.1       1.xyz.com
127.0.0.1       2.xyz.com
127.0.0.1       3.xyz.com
127.0.0.1       chat.xyz.com
127.0.0.1       payment.xyz.com
```
Use any domain for xyz.com

Following commands to start
```bash
virtualenv postm
source postm/bin/activate
pip install flask
python3 main.py
```