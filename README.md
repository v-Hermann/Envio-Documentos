# Projeto-facul 🐘α

#### Comandos do Git 

###### Adquirir repositório

$ git clone https://github.com/v-Hermann/Projeto-facul.git

-baixar do repositório remoto

==========================================================================

###### Commit

$ git add . 

-prepara todos os arquivos editados para o commit

$ git commit -m "commit message"

$ git push

-enviar o conteúdo do repositório local para o repositório remoto

==========================================================================

###### Atualizar meu repositório local

$ git pull origin main

-this will sync your main to the central repo

-sincronizar o repositório local, com a versão mais recente do repo remoto

==========================================================================

#### Comandos do django

$ py manage.py makemigrations

$ py manage.py migrate

$ py manage.py createsuperuser

$ py manage.py runserver

$ py manage.py startapp "nome"

==========================================================================

Bugs:
- Arrumar bug de cadastro, unique username Check✔
- Arrumar bug de direcionamento para página errada pós-login Check✔ 
- Ajustar preview do envio
- Ajustar preview da aprovação
- Renomear arquivo ao salvar Check✔ 
- Apagar documentos desaprovados Check✔ 
- Consertar e melhorar salvamento definitivo Check✔ 
- Arrumar bug que não carrega o documento para ser reenviado quando ele é deletado via document.delete()

Features:
- Ajustar backend para aceitar envio de arquivo apenas quando foram enviados todos os necessários(Já foi implementado com js, mas tem que adequar o backend)
- Implementar arquivos opcionais (Exemplo: Certidão de Casamento e de filhos (menores de 14 anos); CPF dos dependentes (caso tenha); Certificado de Reservista (masculino))
- Melhor mensagens sobre o envio de documentos
- Dar uma resposta por que o arquivo foi desaprovado
- Enviar emails com todas as atualizações da situação do usuário
- Criar grupo de usuários
- Implementar a página de reabrir processo, separado do sistema de aprovação também Check✔
- Privar acesso as páginas (@login_required, @user_passes_test)
- Liberar acesso apenas para o usuário devido
- Implementar mais botões de retorno
- Organizar e renomear as URLs
- Renomear os arquivos do projeto para padronização
- Front-End agrádavel e explicativo
- Pesquisar medidas de segurança
- Limitar tamanho de arquivo Check✔ 
