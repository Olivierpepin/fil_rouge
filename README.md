# Mise en place Infrasructure Cyptomonnaies

Le rapport de la version actuelle est disponible dans */documents/*.
<img src="/etc/images/fil_rouge.png" width="800" height="750">

# Table of Contents
1. [Sources de donées](#sources)
2. [Nettoyage de données](#nettoyage)
3. [Stockage sous Elastic Search](#ES)
    1.  [Test connexion Power BI](#BI)

# Sources de données <a name="sources"></a>

Les données historiques ont été récupérées sur messari : [Messari](https://messari.io/).
Les données en temps réel proviennet des channels des Websockets de Binance sur 10 cryptomonnaies à savoir :
(ADA, BNB, BTC, DOGE, DOT, ETH, LINK, LTC, SOL, XRP)

# Nettoyage de données <a name="nettoyage"></a>

Nous utilisons Logstash de la suite Elastic Search pour intégrer notre donnée historique via des fichiers .YML

<img src="/etc/images/yml_logstash.png" width="800" height="750">

Les données en temps réel sont récupérer des websockets, transformer en documents via des scripts Python et envoyer à Elastic Search

<img src="/etc/images/websocket.png" width="800" height="750">

# Stockage sous Elastic Search <a name="ES"></a>

Par simplification sur la version 0.1, les serveurs ES sont installés en local pour chaque développeur afin de maitriser l'intégralité des process du projet. Il suffit de se rendre sur le site d'Elastic : [Elastic](https://www.elastic.co/fr/) pour récupérer Elastic Search / Kibana et Logstash.

Il suffit de décompresser les fichiers et run les services (par console ou par .bat)

<img src="/etc/images/elastic.png" width="800" height="750">

Par defaut : Elastic Serach est sur le port 9200 et Kibana sur le 5601

<img src="/etc/images/kibana.png" width="800" height="750">

## Test connexion BI <a name="BI"></a>

Nous devons faire la mise en place de la connexion avec Power BI. Il y a plusieurs solutions possible mais nous avons retenu une requête HTTP avec autentification d'utilisateur.

<img src="/etc/images/bi_auth.png" width="800" height="750">