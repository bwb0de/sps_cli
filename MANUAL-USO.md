# SPS/CLI Scrips - Manual de Uso

## Visão geral
O aplicativo em questão trata-se de um conjunto de scripts que tem por finalidade proporcionar o registro e controle das atividades desenvolvidas pelas profissionais do Serviço de Programas Sociais da Faculdade UnB Planaltina (SPS-FUP). Dessa forma a ferramenta foi concebida como um conjunto de comandos que executam funções de registro, edição e processamento de dados. O objetivo é fornecer uma ferramenta prática e funcional para lidar com as demandas e necessidades cotidianas do trabalho sem exigir muito tempo de desenvolvimento, manutenção e correção de erros.

Estes scripts foram concebidos para trabalharem em conjunto com as ferramentas do shell do linux, no caso específico o BASH, de forma a aproveitar as funcionalidades já disponíveis no shell bem como o ambiente multitarefa da linha de comando e todas suas ferramentas nativas.

O pacote de comandos SPS-CLI foi escrito em Python3 e testado em uma versão básica do Debian. Alguns recursos utilizados pelos scripts são exclusivos para sistemas operacionais que utilizem o linux ou estejam de acordo com as especificações POSIX. Dessa forma, não há garantias de que a ferramenta funcione nos sistemas Windows ou MAC.

Para gestão dos profissionais e acesso ao sistema, aproveitamos os recursos do próprio Debian dentre os quais o openssh-server e o ambiente multitarefa nativo. A ideia é que a ferramenta seja instalada em uma máquina virtual com o Debian Base de forma que os acessos sejam efetuados por cada profissional a partir de sua própria estação de trabalho, via terminal.

Os dados, no momento, estão sendo estruturados em arquivos de texto no formato JSON, na mesma máquina virtual. Este formato foi escolhido em virtude das funções de processamento e quantificação de informações previamente escritas. O formato texto também permite backup e edição de forma fácil.

## Conhecendo e entendendo a linha de comando
A linha de comando ou shell constitui uma interface interativa (Command Line Interface – CLI) em modo texto puro. A priori, em uma CLI, não é possível renderizar imagens ou fazer uso de recursos como o mouse. O método de entrada (input) ocorre por meio do uso do teclado. 

As ações ou tarefas em uma CLI são executadas e acompanhadas mediante comandos. Comandos são programas binários, scripts ou funções que executam um conjunto de instruções podendo retornar informações durante ou ao final do processamento. Os comandos são executados quando escrevemos (ou chamamos) seu nome e teclamos a tecla ENTER ou RETURN.

Por exemplo, ao escrevermos os comando pwd e teclarmos ENTER, na linha subsequente obteremos uma resposta do shell que nos mostrará o caminho no sistema de arquivos até o diretório ou pasta em que estamos no momento da execução desse comando.

Alguns comandos exigem argumentos e quando são executados sem estes emitem uma mensagem de orientação ao usuário para que ele/a possa (re)utilizá-lo de forma adequada.

No shell, o comando e os argumentos são separados por espaços em branco. Um argumento que possua informações que contenham espaços em branco pode ser utilizado desde que seja escrito entre aspas.

### Exemplos:
* comando arguento1 argumento2
* comando "argumento1 com espaços" argumento2 

Além dos argumentos, comandos podem aceitar bandeiras (flags) ou opções. As bandeiras são reconhecidas pelo uso do símbolo “-” ou “--” antes do argumento. Bandeiras com apenas “-” geralmente são seguidas por um único caractere. Caso exista mais de um caractere após o “-”, estes caracteres serão considerados como múltiplas opções ativadas simultâneamente.

### Os exemplos abaixo são equivalentes:
* comando -abc
* comando -a -b -c

Algumas bandeiras podem possuir nome extenso, neste caso elas serão precedidas de “--”. A maioria dos comandos possui uma opção de ajuda representada, por padrão, por “-h” ou “--help”.

### Os exemplos abaixo em geral são equivalentes, eles exibem uma ajuda sobre o uso de um comando:
* comando -h
* comando --help

Os caracteres utilizados no comando ou como argumentos fazem distinção entre os modos maiúsculo ou minúsculo, assim “-a” é diferente de “-A” e comando é diferente de COMANDO. Por padrão os comandos do shell são todos escritos em letra minúscula. As opções, entretanto, podem variar entre maiúsculo e minúsculo.

### Os exemplos a seguir não são equivalentes:
* comando -h
* comando -H
* Comando -h
* COMANDO -h

## Comandos básicos da linha de comando, shell BASH
As distribuições GNU/Linux, como o Debian, possuem na base do sistema um conjunto de ferramentas para os mais variados usos. Há vários tipos de shell que podem integrar ou serem instalados ou removidos das distribuições, dentre os quais o ash, bash, zsh, entre outros. De forma geral há compatibilidade entre os comandos dos distintos tipos de shell, entretanto alguns recursos específicos, especialmente em scripts mais longos e complexos, podem exigir pequenos ajustes para que sejam executados adequadamente. Cada shell possui também recursos próprios que permitem uma experiência de usuário distinta como registro de histórico de comandos, cores ou recursos diversos como autocompletar comandos. 

O BASH () geralmente é o shell padrão nas diferentes distribuições GNU/Linux. Dessa forma, embora também aplicáveis aos outros tipos de shell, os comandos apresentados a seguir terão como  base de referência o escopo do BASH.

Dessa forma, a título de breve informação, seguem exemplos elementares de comandos  usados na linha de comando. Para entender melhor o funcionamento de cada um deles, recomendo o uso da opção de ajuda ‘-h’ ou ‘--help’. Para conhecer mais comandos ou saber mais como utilizar todo o potencial do shell, pesquise na internet por “Tutorial BASH” ou “Shell Scripting”.

Os comandos estarão em negrito. À direita uma breve descrição. Em alguns casos serão apresentados exemplos. Recomendo que a medida que você leia os comandos, utilize um terminal para praticar e observar os resultados.

* **ssh**: realiza uma conexão com servidor Secure Shell (SSH) remoto.    
*Exemplo*:
    * **ssh laura@ip_do_host** (faz uma conexão com o servidor ‘ip_do_host’ a partir da conta de usuário ‘laura’)

* **pwd**: mostra o nome do diretório de trabalho atual.

* **ls**: exibe os arquivos do diretório atual.    
*Exemplos*:
    * **ls -l** (exibe os arquivos em formato de lista, mostra informações além do nome do arquivo)
    * **ls -a** (exibe inclusive arquivos ocultos do diretório atual)
    * **ls -al** (ambas as opções anteriores combinadas, exibe arquivos ocultos em lista detalhada)
    * **ls a\*** (exibe os arquivos do diretório atual que possuam a inicial ‘a’)
    * **ls \*.jpg** (exibe os arquivos do diretório atual que possuam o final ‘.jpg’)

* **cd**: muda para o diretório alvo.

* **cp**: copia o arquivo alvo para o destino especificado.    
*Exemplo*:
    * **cp estatisticas.txt backup/estatisticas_1-2019.txt** (realiza uma cópia do arquivo ‘estatisticas.txt’ para dentro da pasta ‘backup’ e define o novo nome do arquivo copiado para ‘estatisticas_1-2019.txt’)

* **mv**: move/renomeia o arquivo alvo para o destino ou novo nome definido.    
*Exemplo*:
    * **mv tabela1.txt tb1.txt** (renomeia o arquivo ‘tabela1.txt’ para ‘tb1.txt’)
    * **mv estatisticas.txt backup/estatisticas.txt** (move o arquivo ‘estatisticas.txt’ da pasta atual para dentro da pasta ‘backup’)

* **mkdir**: cria um diretório ou pasta.

* **rm**: remove/apaga um arquivo ou diretório.    
*Exemplos*:
    * **rm -fR documentos_antigos** (apaga a pasta ‘documentos_antigos’ e todo o seu conteúdo)
    * **rm lista_estudantes.txt** (apaga o arquivo indicado, no caso ‘lista_estudantes.txt’)
    * **rm \*** (apaga todos os arquivos do diretório atual)
    * **rm \*.txt** (apaga todos os arquivos que possuam o final ‘.txt’)    

* **cat**: mostra o conteúdo do arquivo alvo.    
*Exemplo*:
    * **cat lista_atendimentos.txt** (exibe todo o conteúdo de ‘lista_atendimentos.txt’)

* **grep**: mostra as linhas do arquivo alvo em que haja corespondência com o padrão apresentado.
*Exemplo*:
    * **grep 14/0009786 lista_atendimentos.txt** (mostra todas as linhas em que a sequência de caracteres ‘14/0009786’ esteja presente)

* **less**: encapsula a saída de dados ou o conteúdo de um arquivo alvo em uma tela que pode ser rolada para cima e para baixo. É preferível utilizar o less em contraposição ao cat nos casos em que a quantidade de linhas do arquivo/saída de dados for superior que a quantidade de linhas do terminal. Ao pressionar a tecla ‘q’, o comando é finalizado.

* **nano**: abre um editor de texto. A combinação de teclas ctrl+o permite salvar o conteúdo do arquivo editado e ctrl+x finaliza o programa.
*Exemplo*:
    * **nano 2019-06-03_relatorio.txt** (cria ou abre o arquivo ‘2019-06-03_relatorio.txt’ com o editor de texto)

* **exit**: executa logout.

Há muito mais comandos úteis no shell para serem utilizados, entretanto este não é o objetivo deste documento. Além disso esses comandos podem ser combinados entre si de forma a proporcionar resultados ainda mais interessantes. Veja adiante o conceito de pipelines e os caracteres de redirecionamento de fluxo.

## Comandos/scripts SPS-CLI
Os comandos descritos nessa parte não são nativos do shell, são exatamente as ferramentas que foram criadas para facilitar o registro, o resgate e o processamento das informações do cotidiano da atividade do SPS. Eles foram concebidos para serem utilizados de forma integradas com shell e podem ser potencializados mediante o uso de pipelines ou redirecionamento de fluxo.
No momento, os scripts escritos são:

* **novo**: adiciona novos registros nos arquivos de dados, conforme a estrutura e informações dos formulários pré-definidos.    
*Uso*:    
    * novo ( usr | usuario ) \<identificador\>    
    * novo ( atd | atendimento ) \<identificador\>    
    * novo ( sei | processo ) \<identificador\> \<assunto\>    
    * novo ( res | resposta-de-processo )    
    * novo ( est | estudo ) \<identificador\>    
    * novo ( pro | profissional ) \<uid\>    
    * novo ( dbc | campo-db ) \<arquivo_db\> \<coluna\> [\<lista-ops\>]     
    * novo ( dbi | inserir-info ) ( mesclado | aninhado ) \<arquivo_db\> \<formulario\>     
    * novo ( opt | inserir-op) \<coluna\> \<opcao\> \<formulario\>    

* **lst**: lista informações registradas nos arquivos de dados.    
*Uso*:    
    * lst ( usr | estudantes ) [\<marcador\>]    
    * lst ( atd | atendimentos )    
    * lst ( tag | marcadores )     
    * lst ( sei | processos )     
    * lst ( pnd | processos )    
    * lst ( est | estudos )     
    * lst ( pro | profissionais )    

* **sendeml**: Envia e-mails a partir das informações da linha de comando ou redirecionando a saída.    
*Uso*:    
    * sendeml ( wrt | escrever ) \<destinatario\> \<assunto\> [\<mensagem\>]    
    * sendeml ( get | get-from ) \<destinatario\> \<assunto\> [\<mensagem\>]    

