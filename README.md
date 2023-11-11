# ue19_labo09-10
Interrogation d'un service d'API public.

Ici j'interroge le service d'API "FreeToGame" grâce à mon application que j'ai crée en python. Pour commencer, j'importe le module "requests". J'ai utilisé ce module car il était spécifié dans l'énoncé. Si l'on imaginait que ce n'étais pas le cas, on pourrait se jusfier en disant que le module "requests" possède une large documentation, si l'on a le moindre problème, on peut facilement trouver notre réponse sur internet. On pourrait également dire qu'il a une bonne détection des erreurs HTTP. Comme vous allez le voir dans le code, j'utilise la méthode "raise_for_status()" afin de vérifier si ma requête HTTP a réussi. 

Le module "requests" n'est pas installée par défaut dans la librairie python, il va donc falloir l'installer afin de vérifier que l'application fonctionne. Cela est très simple ; ouvrer un terminal et inscrivez ceci : 
$ python -m pip install requests

Si vous êtes sous pycharm, vous pouvez également suivre ce procédé : 
- Ouvrez votre Pycharm sur un projet
- Cliquer sur "Python Packages" en bas à droite
- tapez "requests" dans la barre de recherche
- cliquer dessus et vous verrez le bouton "install package"

Dans les deux cas, votre module devrait être installé et vous devriez être en mesure de faire fonctionner le code.
