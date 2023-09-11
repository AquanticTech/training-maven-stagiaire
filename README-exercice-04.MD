### Commandes Maven pour lister les goals et les cycles de vie

Pour Maven, la commande qui permet de lister les goals et les cycles de vie est :

```bash
mvn help:describe -Dcmd=compile
```

Cette commande affiche les informations sur le goal "compile". Si vous souhaitez obtenir des informations sur un autre goal ou phase, remplacez "compile" par le nom de la phase ou du goal souhaité.

Si vous voulez voir tous les goals d'un plugin spécifique, vous pouvez utiliser :

```bash
mvn help:describe -Dplugin=[nomDuPlugin]
```

Remplacez `[nomDuPlugin]` par le nom du plugin pour lequel vous souhaitez voir les goals. Par exemple, pour le plugin `maven-compiler-plugin`, la commande serait :

```bash
mvn help:describe -Dplugin=maven-compiler-plugin
```
