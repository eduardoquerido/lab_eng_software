# Configurações Projeto

## Utilizando Python 3.8.+

## PostgreSQL

#### Para instalar PostgreSQL no Linux
> sudo apt-get install postgresql postgresql-contrib

#### Para criar um superusuario no PostgreSQL
> sudo -u postgres createuser --superuser <name_of_user>

#### Para criar um banco utilizando o mesmo superusuario
> sudo -u <name_of_user> createdb <name_of_database>

##### Acessar o banco criado com o superusuario criado
> psql -U <name_of_user> -d <name_of_database>


## Virtualenv

#### Para baixar o virtualenv

> pip install virtualenv

#### Criar um diretório para o ambiente virtual

> mkdir receitas_env

#### Gerar o virtual env dentro da pasta de receitas_env

> virtualenv receitas

>> Obs: se houver problema é possivel criar o ambiente virtual com o seguinte comando: python -m venv receitas / python3 -m venv receitas

#### Para iniciar o ambiente virtual

> source /receitas_env/receitas/bin/activate

#### Para finalizar o ambiente virtual

> source /receitas_env/receitas/bin/deactivate


## Instalando dependências

> pip/pip3 install requirements.txt

>> Obs: Deve estar no mesmo diretório do arquivo


## Levantando a aplicação

#### Para a aplicação deve-se criar o banco chamado:

> sudo -u <name_of_user> createdb receitas

#### Para criar as migrações iniciais (após ter criado o banco)

> python manage.py db init

#### Para atualizar as migrações (após ter criado o banco)

> python manage.py db migrate

#### Para aplicar as migrações

> python manage.py db upgrade

#### Para rodar a aplicação

> python manage.py runserver