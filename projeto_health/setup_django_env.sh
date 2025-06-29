#!/bin/bash

echo "🔧 Criando ambiente virtual..."
python3 -m venv venv

echo "✅ Ativando ambiente virtual..."
source venv/bin/activate

echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install django python-decouple

echo "📝 Criando arquivo .env..."
cat <<EOF > .env
SECRET_KEY=django-insecure-^1am0w)yhc!uo)5yce-p$8hpl#r+vi@5kq%w#ay(_4venbgs+-
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST_USER=abdultrato@gmail.com
EMAIL_HOST_PASSWORD=CfCw@6205
EOF

echo "📁 Garantindo que .env está no .gitignore..."
if ! grep -qxF ".env" .gitignore; then
	echo ".env" >> .gitignore
fi

echo "✅ Ambiente configurado com sucesso!"
echo "➡ Execute 'source venv/bin/activate' para ativar o ambiente manualmente quando precisar."
