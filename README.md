# REDIS + CELERY
Redis e Celery são ferramentas que podem ser usadas em conjunto para criar filas de tarefas distribuídas, permitindo que um sistema execute tarefas em várias máquinas. 
O Celery pode usar o Redis como broker, que é um mediador que enfileira as informações sobre as tarefas.
O Celery pode funcionar em modo multi-thread ou multi-process.
É possível subir múltiplos workers para lidar com múltiplas tarefas.
Tudo isso é possível através do WSL, que permite rodar o Linux no Windows.

# INSTALAÇÃO
No Windows, ativar o modo desenvolvedor: 
janela windows --> configurações --> para desenvolvedores --> ativar o modo desenvolvedor --> ativar o sudo

No terminal do Visual Studio Code (atenção: não é o do power shell):
- pip install wsl
- wsl --install
- wsl --install -d Ubuntu

Para ativar o wsl na máquina:
- wsl.exe. -d Ubuntu
- usuario: setor_desenvolvimento
- senha: @see

Para rodar o Celery no projeto Django:
- celery -A

Para fazer a venv dentro do wsl:
- sudo apt update && sudo apt install python3 -venv -y
- python3 -m venv venv
- source venv/bin/activate

ATENÇÃO
Será preciso baixar todas as dependências novamente:
PostgreSQL: 
-sudo apt update && sudo apt install postgresql postgresql-contrib libpq-dev -y

Ferramentas de compilação do WSL:
- sudo apt update && sudo apt install build-essential -y

Django: 
- pip install -r requirements.txt
- pip install django
- pip install django[celery] redis
- pip install python-dotenv
- pip install psycopg2-binary

Para iniciar o projeto (diariamente)
- no terminal digita wsl
- ativar a venv: source venv/bin/activate

Rodar o servidor: 
- python3 manage.py runserver


# Instalação do Docker dentro da WSL

Abra o terminal do WSL e execute os seguintes comandos para instalar o Docker:

Atualize os pacotes do sistema:
sudo apt update
sudo apt upgrade

Instale as dependências necessárias:
sudo apt install apt-transport-https ca-certificates curl software-properties-common

Adicione a chave GPG oficial do Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

Adicione o repositório Docker:
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Atualize o repositório e instale o Docker:
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

Inicie o serviço Docker:
sudo service docker start

Teste a instalação:
sudo docker --version
Isso deve exibir a versão do Docker instalada.

Adicionar seu usuário ao grupo docker para poder executar comandos Docker sem usar sudo:
sudo usermod -aG docker $USER
Depois disso, feche e abra o terminal novamente ou faça logout e login.

Passo 3: Usando o Docker no WSL
Agora que o Docker está instalado, você pode usar o Docker dentro do WSL como se estivesse em um ambiente Linux tradicional. 

Para abrir a página que administra os containers, digita no terminal:
sudo systemctl status docker
Se não estiver rodando, coloca:
sudo systemctl start docker

