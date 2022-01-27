echo ">> FETCHING UPSTREAM REPO..."
git clone https://github.com/AnonymousBoy1025/AnonymousMusic /AnonymousMusic
echo ">> INSTALLING REQUIREMENTS..."
cd /AnonymousMusic
pip3 install -U -r requirements.txt
echo ">> STARTING ANONYMOUS MUSIC USERBOT..."
clear
echo "
‌ٖٖٖٖٖٖٜٖٖٖٖٖٖٜٖٖٖٖٖٖٜٖٖٖٖٖٖٜٖٖٖٖٖٖ𓆩🖤𓆪ــــﮩـــــﮩــ٨ﮩﮩANONYMOUSــــﮩــ٨ﮩﮩ ﮩﮩ٨ــﮩــــ𓆩🖤𓆪 ‌ٖٖٖٖٖٖٜٖٖٖٖٖٖٜٖٖٖٖٖٖٜٖٖٖٖٖٖٜٖٖٖٖ[🇮🇳]
» Anonymous Music Started Successfully !
"
python3 main.py
