python3 -m virtualenv .env
pip3 install --upgrade -r requirements.txt
source /home/arnaud/TD5/.env/bin/activate
if test -f "main.py"; then
	    echo "main.py exists."
fi
python3 main.py
