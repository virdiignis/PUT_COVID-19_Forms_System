yum install python38
update-alternatives --config python
update-alternatives --config python3
yum install gcc
yum install python38-devel
pip3 install -r requirements.txt
yum install redis
systemctl enable redis
