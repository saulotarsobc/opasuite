# OPA SUITE + PYTHON + MONGODB

![image](https://user-images.githubusercontent.com/23584038/133458335-1026ebd5-29a2-485b-baf9-34370136e3cd.png)

![image](https://user-images.githubusercontent.com/23584038/133458485-4d4691e6-cd1a-469e-bdd5-bb61eb518a77.png)

![image](https://user-images.githubusercontent.com/23584038/133458691-c5ce6afb-d21a-4392-b284-6a801bf07ba0.png)

## ZABBIX-AGENT

> no servidor Opa Suite...

```sh
apt update
apt install zabbix-agent
```

```sh
service zabbix-agent status
```

![print grafana](./recursos/img/service%20zabbix-agent%20status.png)

> Edite o arquivo '/etc/zabbix/zabbix_agentd.conf'

```sh
nano /etc/zabbix/zabbix_agentd.conf
```

> Altere a linha "# EnableRemoteCommands=0" para "EnableRemoteCommands=1"

![-](./recursos/img/enable_remote_config.png)

> Libere o IP ou rede do seu Zabbix server

![-](./recursos/img/redes_permitidas.png)

> Reinicie o serviço do zabbix-agent no Opa Suite

```sh
service zabbix-agent restart
```

> No Zabbix Server faça o teste de comunicação com o Zabbix Agent instalado no servidor Opa Suite

```sh
zabbix_get -s ip_do_opa_suite -k "system.run[echo Funcionando...]"
```

![-](./recursos/img/teste_zabbix_agent.png)

## PYTHON

> PIP

- PIP é um sistema de gerenciamento de pacotes padrão usado para instalar e gerenciar pacotes de software escritos em Python. Vamos instala-lo.

```sh
apt install python3-pip
```

> Instalação das bibliotecas pymongo

```sh
pip3 install pymongo
```

> Criar um diretório para salvar o script

```sh
mkdir /home/scripts
nano /home/scripts/opaSuite.py
```

> Copie o código em python e cole no servidor

- [Script em Python](https://github.com/saulotarsobc/opasuite_zabbix_py#saulo-costa---telegram)

> Teste se o script está retornando os dados do MondoDB

```sh
python3 /home/scripts/opaSuite.py getCanais
```

> Vai retornar o json com os canais cadastrados no seu Opa Suite

![-](./recursos/img/teste_script_python.png)

<!-- ![-](./recursos/img/teste_zabbix_agent.png) -->

## ZABBIX

### Alguns detalhes sobre o template

> Contador de usuarios ativos

```js
$[?(@.status == "A")].length()
```

> Contador de usuarios online

```js
$[?(@.online == "on")].length()
```

> Contador de Atendimento por Usuários

```js
// macros
{#NOME} -> $.nome
{#ID_ATENDENTE} -> $._id.oid

//pre processsamento do prototipo de item
$[?(@.id_atendente.oid == "{#ID_ATENDENTE}")].length()
```

> Contador de atendimentos por canal

```js
$[?(@.canal == "whatsapp")].length()
$[?(@.canal == "messenger")].length()
$[?(@.canal == "pabx")].length()
```

> Contador de atendimentos por Setor/Departamento

```js
{#DEPARTAMENTO} -> $.nome
{#ID_DEPARTAMENTO} -> $._id.oid

//pre processsamento do prototipo de item
$[?(@.setor.oid == "{#ID_DEPARTAMENTO}")].length()
```

## GRAFANA

1) Contador de usuários
   1) Total ativos
   2) Total online
2) Contador de atendimentos
   1) Aguardando atendimentos
      1) Por setor/departamento
      2) Por canal
   2) Em atendimento
      1) Por setor/departamento
      2) Por canal
      3) Por usuário

## [Saulo Costa - Telegram](https://t.me/saulos2costa/ "telegram")

> Obtenha...

- [Script em Python](https://t.me/saulos2costa/ "telegram")

- [Dashboard do Grafana](https://t.me/saulos2costa/ "telegram")

- [Template do Zabbix](https://t.me/saulos2costa/ "telegram")
