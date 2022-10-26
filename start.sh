echo "Cloning Repo...."
git clone https://github.com/Annumit/MdiskSearchBot.git /MdiskSearchBot
cd /MdiskSearchBot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
