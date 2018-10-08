pour lancer le programme :

1) ajouter le fichier config.json avec cette structure :

{
  "mail_configuration" :
  {
    "smtp_ssl_host" : "XXX" ,
    "smtp_ssl_port" : XXX,
    "mail"          : "XXX",
    "password"      : "XXX",
    "targets_mail"  : "XXX"
  },
  "target_info":
  {
    "url" : "XXX",
    "payload" : "XXX",
    "headers" :
    {
      "content-type": "XXX",
      "cache-control": "XXX"
    },
    "path" : "XXXX",
    "target_string" : "XXX"
  }
}

2) lancer le stript "start.sh"




# TO DO :
1) completer le dockerfile
2) mettre à jour le Makefile
3) Ajouter les tests de non régression 
4) déployer et faire tourner 24h/24H sur une EC2.
