# Exercice Maven : Création d'un JAR HelloWorld

## Objectif
L'objectif de cet exercice est de créer un projet Maven qui génère un JAR exécutable. Lors de l'exécution de ce JAR, le message "HelloWorld" doit être affiché sur la ligne de commande.

## Instructions

### 1. Créez un nouveau projet Maven.
```bash
mvn archetype:generate -DgroupId=com.votre.nom -DartifactId=nom-du-projet -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

### 2. Configurez votre projet pour qu'il génère un JAR exécutable.
Ajoutez le plugin `maven-jar-plugin` et `maven-shade-plugin` dans votre `pom.xml` :
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-jar-plugin</artifactId>
            <version>3.2.0</version>
            <configuration>
                <archive>
                    <manifest>
                        <mainClass>chemin.vers.votre.ClassePrincipale</mainClass>
                    </manifest>
                </archive>
            </configuration>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>3.2.4</version>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals>
                        <goal>shade</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```
### maven-jar-plugin

Le `maven-jar-plugin` est un plugin Maven utilisé pour construire un JAR à partir des classes compilées d'un projet. Il permet de spécifier le point d'entrée pour l'application, d'ajouter des ressources supplémentaires et de définir d'autres métadonnées pour le JAR. Ce plugin est essentiel pour empaqueter les applications Java pour leur distribution.

##### Caractéristiques principales :

- Génération de JAR à partir des classes compilées.
- Possibilité de définir une classe principale pour le JAR exécutable.
- Ajout de ressources supplémentaires au JAR.
- Configuration des métadonnées du manifeste.

---

#### maven-shade-plugin

Le `maven-shade-plugin` est un autre plugin Maven qui permet de créer un JAR "ombragé" (ou "fat JAR"). Ce JAR contient toutes les dépendances nécessaires pour exécuter l'application, ce qui le rend autonome. Le plugin offre également la possibilité de renommer les paquets des dépendances pour éviter les conflits.

##### Caractéristiques principales :

- Création d'un JAR autonome avec toutes les dépendances.
- Possibilité de renommer les paquets des dépendances pour éviter les conflits.
- Filtrage des dépendances pour inclure/exclure des éléments spécifiques.
- Transformation des ressources et des classes.

### 3. Ajoutez le code nécessaire pour afficher "HelloWorld" lors de l'exécution du JAR.
```java
package com.votre.nom;

public class App {
    public static void main(String[] args) {
        System.out.println("HelloWorld");
    }
}
```

### 3.1 - Erreur Source option 7 is not longer supporter, use 8 or Later
Pour résoudre l'erreur `[ERROR] Source option 7 is no longer supported. Use 8 or later.` dans un projet Maven, vous devez définir la version source et cible de Java dans le fichier `pom.xml` de votre projet.

Ajoutez ou mettez à jour la configuration du plugin `maven-compiler-plugin` dans la section `<build><plugins>` de votre `pom.xml` :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.0</version>
            <configuration>
                <source>8</source>
                <target>8</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Cela indique à Maven d'utiliser Java 8 comme version source et cible lors de la compilation de votre projet. Vous pouvez ajuster les valeurs `8` à une version ultérieure si nécessaire.


### 4. Configurez le `pom.xml` pour permettre le packaging en snapshot et en release.
```xml
<distributionManagement>
    <snapshotRepository>
        <id>nexus-snapshots</id>
        <url>https://nexus2.zonova.io/repository/maven-snapshots/</url>
    </snapshotRepository>
    <repository>
        <id>nexus-releases</id>
        <url>https://nexus2.zonova.io/repository/maven-releases/</url>
    </repository>
</distributionManagement>
```

### 5. Configuration du Settings.xml

Pour générer un fichier `settings.xml` par défaut avec Maven, vous pouvez utiliser la commande suivante :

```bash
mvn help:effective-settings
```

Cette commande affichera le `settings.xml` effectif qui est utilisé par Maven. Si vous souhaitez sauvegarder ce contenu dans un fichier, vous pouvez rediriger la sortie vers un fichier, par exemple :

```bash
mvn help:effective-settings > ~/settings.xml
```

Cela créera un fichier `settings-default.xml` dans le répertoire courant avec le contenu du `settings.xml` effectif.

Notez que cette commande affiche le `settings.xml` fusionné à partir de l'emplacement global (généralement dans le répertoire d'installation de Maven) et de l'emplacement utilisateur (généralement `~/.m2/settings.xml`). Si vous n'avez pas encore de `settings.xml` dans votre répertoire `~/.m2/`, la sortie sera simplement le `settings.xml` global par défaut.

### 6. Configuration des accès aux repository
Configurez Maven pour envoyer les artifacts vers un repository Nexus.
Assurez-vous d'avoir les informations d'identification pour Nexus dans votre fichier `settings.xml` de Maven.

Dans le fichier settings situé à ~/.m2/settings.xml,
ajouter les informations de connexion au serveur.
```xml
<servers>
    <server>
        <id>nexus-snapshots</id>
        <username>admin</username>
        <password>password</password>
    </server>
    <server>
        <id>nexus-releases</id>
        <username>admin</username>
        <password>password</password>
    </server>
</servers>
```
**Note** : Pour des raisons de sécurité, il est recommandé de chiffrer les mots de passe dans le fichier `settings.xml` en utilisant le cryptage Maven. Assurez-vous également de ne pas exposer le fichier `settings.xml` contenant des mots de passe en clair.

Pour chiffrer un mot de passe avec Maven :
```bash
mvn --encrypt-password <votre_mot_de_passe>
```

Si c'est la première fois que vous utilisez le chiffrement Maven, chiffrer également un "mot de passe maître" :
```bash
mvn --encrypt-master-password <votre_mot_de_passe_maître>
```

Ensuite, créez ou mettez à jour le fichier `settings-security.xml` dans `~/.m2/` :
```xml
<settingsSecurity>
    <master>{jSMOWnoPFgsHVpMvz5VrIt5kRbzGpI8u+9EF1iFQyJQ=}</master>
</settingsSecurity>
```

Remplacez la valeur entre les balises `<master>` par le mot de passe maître chiffré généré.

