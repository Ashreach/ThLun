if ! ls | grep -q ".venv"; then
  python3 -m venv .venv
fi

if [ -z "$VIRTUAL_ENV" ]; then
  source .venv/bin/activate
fi

pip install .
clear
echo -e "\e[36mλ ~/Ashreach/ThLun \e[33mpython3 test.py \e[0m イ (test.sh)"
python3 test.py