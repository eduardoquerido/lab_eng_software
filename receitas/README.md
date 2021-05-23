# Configurações Projeto

## Utilizando Python 3.8.+


#### Criando Banco MySQL
$ mysql -u root

ou

$ sudo mysql

``` sql
mysql> CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'admin2021';
mysql> CREATE DATABASE receitas;
mysql> GRANT ALL PRIVILEGES ON receitas . * TO 'dt_admin'@'localhost';
```

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

#### Para aplicar as migrações

> flask db upgrade

#### Para rodar a aplicação

> flask run

	OBS: Para rodar a aplicação com guinicorn estando na pasta RAIZ do projeto que se encontra o módulo /receita/wsgi.py:

> gunicorn --bind 0.0.0.0:5000 wsgi:app

	OBS2: Se for necessário recriar as migrações, delete o diretório "migrations" e rode os seguintes comandos:

		$ flask db init
		$ flask db migrate
		$ flask db upgrade