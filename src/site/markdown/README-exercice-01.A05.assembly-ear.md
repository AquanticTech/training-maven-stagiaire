# Exercice Maven : Construire un Assembly de type EAR

## Objectif
L'objectif de cet exercice est de vous familiariser avec la création d'un assembly de type EAR dans Maven en composant différentes ressources.

## Prérequis
- Avoir Maven installé sur votre machine.
- Avoir une connaissance de base des projets Java EE.

## Étapes

### 1. Création du projet parent

1. Ouvrez un terminal et naviguez vers le répertoire de votre choix.
2. Créez un nouveau projet Maven avec le packaging `pom` :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=ear-project -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false -Dpackaging=pom
   ```

### 2. Ajout de modules

Ajoutez deux modules : un module `web` pour une application web et un module `ejb` pour les beans EJB.

1. Naviguez vers le répertoire du projet parent `ear-project`.
2. Créez le module `web` :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=web-module -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
   ```
3. Créez le module `ejb` :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=ejb-module -DarchetypeArtifactId=maven-archetype-ejb -DinteractiveMode=false
   ```

### 3. Configuration du plugin `maven-ear-plugin`

Dans le fichier `pom.xml` du projet parent, ajoutez la configuration suivante pour le plugin `maven-ear-plugin` :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-ear-plugin</artifactId>
            <version>3.2.0</version>
            <configuration>
                <version>8</version>
                <defaultLibBundleDir>lib</defaultLibBundleDir>
                <modules>
                    <webModule>
                        <groupId>com.formation</groupId>
                        <artifactId>web-module</artifactId>
                        <contextRoot>/webapp</contextRoot>
                    </webModule>
                    <ejbModule>
                        <groupId>com.formation</groupId>
                        <artifactId>ejb-module</artifactId>
                    </ejbModule>
                </modules>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 4. Construction de l'assembly EAR

1. Dans le terminal, naviguez vers le répertoire du projet parent `ear-project`.
2. Exécutez la commande suivante pour construire l'assembly EAR :
   ```bash
   mvn clean package
   ```

Après avoir exécuté cette commande, vous devriez trouver un fichier `.ear` dans le répertoire `target` du projet parent. Ce fichier `.ear` est l'assembly qui contient les modules `web` et `ejb`.

Félicitations ! Vous avez réussi à construire un assembly de type EAR en composant différentes ressources avec Maven.
