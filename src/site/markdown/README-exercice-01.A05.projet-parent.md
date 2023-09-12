# Exercice Maven : Utilisation des dépendances et des modules

## Objectif
L'objectif de cet exercice est de vous familiariser avec la création de projets Maven, l'utilisation des dépendances et la combinaison de plusieurs projets en un seul projet parent.

## Étape 1 : Créer un premier projet "Hello World"

1. Ouvrez un terminal et naviguez vers le répertoire de votre choix.
2. Exécutez la commande suivante pour créer un nouveau projet Maven :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=hello-world-1 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```
3. Naviguez vers le répertoire `hello-world-1` et ouvrez le fichier `App.java` dans le répertoire `src/main/java/com/formation`.
4. Modifiez le fichier pour qu'il affiche "Hello World from Project 1!" :
   ```java
   public class App {
       public static void main(String[] args) {
           System.out.println("Hello World from Project 1!");
       }
   }
   ```

## Étape 2 : Créer un second projet "Hello World"

1. Retournez au répertoire parent et exécutez la commande suivante pour créer un second projet Maven :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=hello-world-2 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```
2. Naviguez vers le répertoire `hello-world-2` et ouvrez le fichier `App.java`.
3. Modifiez le fichier pour qu'il affiche "Hello World from Project 2!" :
   ```java
   public class App {
       public static void main(String[] args) {
           System.out.println("Hello World from Project 2!");
       }
   }
   ```

## Étape 3 : Combiner les deux projets dans un projet parent

1. Retournez au répertoire parent et créez un nouveau dossier nommé `parent-project`.
2. À l'intérieur de `parent-project`, créez un fichier `pom.xml`.
3. Dans ce fichier `pom.xml`, définissez-le comme un projet parent et ajoutez `hello-world-1` et `hello-world-2` comme modules. Voici un exemple de contenu pour le `pom.xml` :
   ```xml
   <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>
       <groupId>com.formation</groupId>
       <artifactId>parent-project</artifactId>
       <version>1.0-SNAPSHOT</version>
       <packaging>pom</packaging>
       <modules>
           <module>../hello-world-1</module>
           <module>../hello-world-2</module>
       </modules>
   </project>
   ```

## Étape 4 : Générer un build pour le projet parent

1. Dans le terminal, naviguez vers le répertoire `parent-project`.
2. Exécutez la commande suivante pour générer un build pour le projet parent :
   ```bash
   mvn clean install
   ```
3. Une fois la commande terminée, vous devriez voir les builds des deux projets enfants ainsi que du projet parent dans le répertoire `target` de chaque projet.

Félicitations ! Vous avez maintenant combiné deux projets Maven en un seul projet parent, ajouté du code pour chacun et généré un build pour le projet parent.
