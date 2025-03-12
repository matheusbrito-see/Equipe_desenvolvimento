-----REDIS + CELERY-------
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
