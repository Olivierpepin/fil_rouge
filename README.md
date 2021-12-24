# Mise en place Infrastructure Cyptomonnaies (Version 0.1)

Le rapport de la version actuelle est disponible dans */etc/rapports*.<br><br><br>
<img src="/etc/images/fil_rouge.png" width="693" height="400">
<br>
# Table of Contents
1. [Sources de données](#sources)
2. [Nettoyage de données](#nettoyage)
3. [Stockage sous Elastic Search](#ES)
    1.  [Test connexion Power BI](#BI)
    2.  [Test connexion Jupyter](#Jupyter)
4. [Visualisation & Analyses](#Visu)
    1. [Kibana](#Kibana)
    2. [Power BI](#Viz_BI)
    3. [Jupyter](#Viz_Jup)
5. [Améliorations à venir pour la v 0.2 et ultérieurs](#Version)

# Sources de données <a name="sources"></a>

Les données historiques ont été récupérées sur messari : [Messari](https://messari.io/).<br>
Les données en temps réel proviennet des channels des Websockets de Binance sur 10 cryptomonnaies à savoir :<br>
(ADA, BNB, BTC, DOGE, DOT, ETH, LINK, LTC, SOL, XRP)

# Nettoyage de données <a name="nettoyage"></a>

Nous utilisons Logstash de la suite Elastic Search pour intégrer notre donnée historique via des fichiers .YML

<img src="/etc/images/yml_logstash.png" width="689" height="528">

Les données en temps réel sont récupérées par des websockets, transformer en documents via des scripts Python<br> et envoyer à Elastic Search.
<br><br>
<img src="/etc/images/websockets.png" width="669" height="568">

# Stockage sous Elastic Search <a name="ES"></a>

Par simplification sur la version 0.1, les serveurs ES sont installés en local pour chaque développeur afin de maitriser l'intégralité des process du projet. Il suffit de se rendre sur le site d'Elastic ([Elastic](https://www.elastic.co/fr/)) pour récupérer Elastic Search / Kibana et Logstash.

Il suffit de décompresser les fichiers et run les services (par console ou par .bat)

<img src="/etc/images/elastic.png" width="498" height="200">
<br>
Par defaut : Elastic Serach est sur le port 9200 et Kibana sur le 5601.
<br><br>
<img src="/etc/images/kibana_service.png" width="641" height="386">

## Test connexion BI <a name="BI"></a>

Nous devons faire la mise en place de la connexion avec Power BI. Il y a plusieurs solutions possible mais nous avons retenu une requête HTTP avec autentification d'utilisateur.

<img src="/etc/images/bi_auth.png" width="701" height="318">

## Test connexion Jupyter <a name="Jupyter"></a>

Après avoir monter jupyter, nous utilisons lab ainsi qu'une librairie Elasticsearch pour récupérer le contenu de nos index. La requête est envoyé directement en localhost sur le service par défaut d'ES. Nous avons une gestion des droits, il nous donc une authentification. Dans cet exemple : nous récuperons l'ensemble des données de l'index "ada_historical" que nous envoyons dans un Data Frame.
<br><br>
<img src="/etc/images/jupyter.png" width="674" height="426">

# Visualisation & Analyses<a name="Visu"></a>

Chaque logiciel de visualisation / analyses à des utilisateurs différents. Kibana est principalement utilisé pour de la gestion en temps réel, Power BI pour du reporting et Jupyter avec Pandas (et Plotly pour la création de graphs) pour de l'analyses / ML.

## Kibana <a name="Kibana"></a>

Il est possible de créer des visualisations complexe de manière simple sous Kibana. Chaque visualisation est indépendante et peu s'intégrer à un dashboard. Pour la gestion du temps réel, il suffit de créer un dashboard, définir une fênetre d'analyse des données et une fréquence de rafraichissement.

<img src="/etc/images/kibana_rt.png" width="932" height="375">

## Power BI <a name="Viz_BI"></a>

Après une création des liaisons des tables (Power Bi fonctionne sous un modèle relationnel), il suffit de mettre en place les mesures désirées afin de pouvoir établir les graphs et reporting. Le logiciels est puissant sur la gestion et la mise en forme des champs ainsi que sur la possibilité de création des graphs.

<img src="/etc/images/tree_map.png" width="874" height="409">

## Jupyter <a name="Viz_Jup"></a>

Nous avons utilisés Jupyter avec comme librairies MatplotLib, Numpy, Pandas et Plotly pour produire une étude portant sur la capitalisation boursière, le prix et la volatilité des cryptomonnaies. L'étude est entièrement disponible dans */etc/rapports*. (page 26)

<img src="/etc/images/vol_crypto.png" width="905" height="485">

# Amélioration v 0.2 et ultérieurs<a name="Version"></a>

• Ajout de Stable Coin (USDT / USDC)<br>
• Amélioration de la stabilité des Websockets / MAJ des scripts de query API<br>
• Gestion des index ES via Index Lifecycle Management (ILM)<br>
• Gestion des replicas ES<br>
• Approfondir les analyses Pandas et le forecasting<br>
• Utilisation de query de type POST via ES<br>
• Utilisation d’un modèle Long Short Term Memory (pour la v 0.3)<br>
