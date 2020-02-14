# SPS/CLI Scrips #

Este projeto consiste em um conjunto de **Scripts/Ferramentas** para o uso no cotidiano da **Assitência Estudantil da UnB**. Estes permitem realizar **registros de atendimentos, reaver informações armazenadas, grava-lás em arquivos de saída e enviá-las facilmente via email pelo terminal**.

Estas ferramentas foram concebidas para trabalharem de forma integrada com o **Bash**, tendo sido testadas e desenvolvidas a partir de uma versão básica do Debian. O objetivo é fornecer uma ferramenta prática e funcional para lidar com as demandas e necessidades cotidianas do trabalho sem exigir muito tempo de desenvolvimento, manutenção e correção de erros. Nesse sentido este pacode de scripts foi pensado para ser executado em sistemas GNU/Linux.

Para gestão dos profissionais, aproveitamos os recursos do próprio sistema operacional. Assim a ideia é que os profissionais sejam cadastrados com o comando **adduser** e acessem o shell via **ssh**. Estes Scripts/Ferramentas seriam instalados em uma máquina virtual ou um servidor local e que os acessos seriam efetuados por cada profissional a partir de sua própria estação de trabalho.

Os dados, no momento, estão sendo estruturados em arquivos de texto no formato JSON.

# Dependências #

## Python ##

- docopt
- colored

## Base do sistema ##

- python3
- rclone
- zip
- ccrypt
- nano
- nodejs
- git
- pandoc
- wkhtmltopdf

# Instalação #

### [1] Instalar os programas base necessários.
Eles provavelmente estão disponíveis via gerenciador de pacotes de sua respectiva distribuição.

No **Debian**:

- sudo apt install python3 **rclone** zip ccrypt nano **nodejs** git

Os pacotes destacados devem, preferencialmente, ser instalados em suas versões mais recentes.

### [2] Instalar os módulos adicionais do python3.

- sudo pip3 install docopt colored

### [3] Escolher o local da instalação do SPS/CLI e clonar este repositório no local.

- git clone *http://www.github.com/bwb0de/sps_cli.git*

### [4] Navegar até a pasta onde o projeto foi clonado e acessar a pasta 'cli'.

### [5] Executar o script de instalação './cli-install'.

### [6] Fazer o 'logout' e o 'login'...