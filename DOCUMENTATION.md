# SPS/CLI Scrips - Documentação

Este arquivo tem por finalidade fornecer sobre estruturação/organização desse pacote de recursos em especial para aqueles que desejarem modificar o código para uma configuração mais adequada aos seus interesses.

O pacote **SPS/CLI Scrips** está organizado em dois grandes grupos de arquivos: 'cli' e 'www'.

A pasta '**cli**' guarda todos os comandos/scripts do shell, além de suas dependências ('python_modules'). Ao instalar o pacote no sistema, a pasta em questão deverá ser adicionada ao PATH do sistema para que os comandos possam ser adequadamente usados.

Há dois arquivos de configuração geral, 'cli_base.py', localizado dentro da pasta 'python_modules', e 'global_config.json', localizado na pasta 'config'.

Em '**cli_base.py**', a definição mais importante e necessária é a '**app_root_folder**' que indica o caminho para a base do aplicativo. Esta pasta geralmente conincide com o caminho onde o repositório git foi clonado. Esta variável poderá assumir valores diferente para hosts distintos caso tenha-se interesse de utilizar diferentes instalações independentes, mas que troquem informações de dados mediante o mecanismo de envio de fragmentos.

Em '**global_config.json**', o fundamental é entender a estrutura do arquivo JSON. Os valores são registrados com duas chaves aninhadas. A primeira chave corresponde ao *hostname* da máquina, aninhado a cada hostname, deve-se enunciar as chaves e valores correspondentes. As variáveis padrão já definidas são: 'send_email_automaticaly', 'work_with_fragments', 'situacoes_email_automatico'. Caso a chave 'send_email_automaticaly' seja definida como **true**, os usuarios serão comunicados via email quando ocorrerem atendimentos de tipo pré-definidos em 'situacoes_email_automatico'.

A chave 'work_with_fragments' deve ser definida como **false** no host principal e como **true** para todos os demais hosts periféricos. O sistema de fragmentos dos hosts periféricos envia os dados registrados de forma criptografada ao serviço de disco virtual (nuvem) configurado. Este mecanismo de envio/verificação de fragmentos é feito via *rclone* para aconta configurada. Dois arquivos serão necessários para o funcionamento do sistema de fragmentos: 

* 'ccrypt-key': as informações deste arquivo serão utilizadas para criptografar os arquivos enviados à nuvem, o arquivo deve ser igual em todas as máquinas. 
* 'rclone...': este é uma cópia do arquivo de configuração do 'rclone' com o token de acesso ao serviço configurado, ele será utilizado para autenticar, enviar e receber os fragmentos.

Estes devem ser criados dentro da pasta 'cli/seguranca'.

Além desses arquivos, a pasta 'formularios' guarda os arquivos com a estrutura dos questionários a serem renderizados no shell. **É necessário criar um link simbólico desta pasta dentro da pasta 'www' para que os mesmos instrumentais estejam acessíveis na versão web da aplicação.

A pasta '**www**' guarda todos os arquivos necessários à versão web da aplicação, escrita em Node.JS. 
