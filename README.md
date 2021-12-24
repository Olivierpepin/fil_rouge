# Mise en place Infrasructure Cyptomonnaies

Le rapport de la version actuelle est disponible dans */etc/rapports*.
<img src="/etc/images/fil_rouge.png" width="1600" height="800">

# Table of Contents
1. [Sources de donées](#sources)
2. [Nettoyage de données](#nettoyage)
3. [Stockage sous Elastic Search](#ES)
    1.  [Test connexion Power BI](#BI)
    2.  [Test connexion Jupyter](#Jupyter)
4. [Visualisation & Analyses](#Visu)
    1. [Kibana](#Kibana)
    2. [Power BI](#Viz_BI)
    3. [Jupyter](#Viz_Jup)

# Sources de données <a name="sources"></a>

Les données historiques ont été récupérées sur messari : [Messari](https://messari.io/).
Les données en temps réel proviennet des channels des Websockets de Binance sur 10 cryptomonnaies à savoir :
(ADA, BNB, BTC, DOGE, DOT, ETH, LINK, LTC, SOL, XRP)

# Nettoyage de données <a name="nettoyage"></a>

Nous utilisons Logstash de la suite Elastic Search pour intégrer notre donnée historique via des fichiers .YML

<img src="/etc/images/yml_logstash.png" width="800" height="750">

Les données en temps réel sont récupérer des websockets, transformer en documents via des scripts Python et envoyer à Elastic Search.

<img src="/etc/images/websockets.png" width="800" height="750">

# Stockage sous Elastic Search <a name="ES"></a>

Par simplification sur la version 0.1, les serveurs ES sont installés en local pour chaque développeur afin de maitriser l'intégralité des process du projet. Il suffit de se rendre sur le site d'Elastic : [Elastic](https://www.elastic.co/fr/) pour récupérer Elastic Search / Kibana et Logstash.

Il suffit de décompresser les fichiers et run les services (par console ou par .bat)

<img src="/etc/images/elastic.png" width="498" height="200">

Par defaut : Elastic Serach est sur le port 9200 et Kibana sur le 5601

<img src="/etc/images/kibana_service.png" width="641" height="386">

## Test connexion BI <a name="BI"></a>

Nous devons faire la mise en place de la connexion avec Power BI. Il y a plusieurs solutions possible mais nous avons retenu une requête HTTP avec autentification d'utilisateur.

<img src="/etc/images/bi_auth.png" width="701" height="318">

## Test connexion Jupyter <a name="BI"></a>

Après avoir monter jupyter, nous utilisons Jupyter lab ainsi qu'une librairie Elasticsearch pour récupérer le contenu de nos index. La requête est envoyé directement en localhost sur le service par défaut d'ES. Nous avons une gestion des droits, il nous donc une authentification. Dans cet exemple : nous récuperons l'ensemble des données de l'index "ada_historical" que nous envoyons dans un Data Frame.

<img src="/etc/images/jupyter.png" width="674" height="426">

# Visualisation & Analyses<a name="Visu"></a>

Chaque logiciels de visualisation / analyses a des utilisateurs différents. Kibana est principalement utilisé pour de la gestion en temps réel, Power BI pour du reporting et Jupyter avec Pandas (et Plotly pour la création de graphs) pour de l'analyses / ML.

## Kibana <a name="Kibana"></a>

Il est possible de créer des visualisation complexe de manière simple sous Kibana. Chaque visualisation est indépendante et peu s'intégrer à un dashboard. Pour la gestion du temps réel, il suffit de créer un dashboard, de définir une fênetre d'analyse des données et une fréquence de rafraichissement.

<img src="/etc/images/kibana_rt.png" width="1400" height="562">

## Power BI <a name="Viz_BI"></a>

Après une création des liaisons des tables (Power Bi fonctionne sous un modèle relationnel), il suffit de créer les mesures désirées afin de pouvoir établir les graphs et reporting. Le logiciels est puissant sur la gestion et la mise en forme des champs ainsi que sur la possibilité de création des graphs.

<img src="/etc/images/tree_map.png" width="1311" height="614">

## Jupyter <a name="Viz_Jup"></a>

Nous avons utilisés Jupyter avec comme librairie MatplotLib, Numpy, Pandas et Plotly pour produire une étude portant sur la capitalisation boursière, le prix et la volatilité des cryptomonnaies. L'étude est entièrement disponible dans */etc/rapports*. (page 26)

<img src="/etc/images/vol_crypto.png" width="1358" height="727">

