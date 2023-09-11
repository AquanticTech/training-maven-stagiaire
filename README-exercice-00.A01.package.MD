## Exercice : Packaging, Extraction et Exploration d'un fichier JAR

### Objectif :
Apprendre à packager un fichier `.class` dans un fichier `.jar`, extraire le contenu du fichier `.jar` et comprendre le contenu du manifeste.

### Étapes :

1. **Packaging du fichier `.class` dans un fichier `.jar`**
    - Assurez-vous d'être dans le répertoire contenant le fichier `HelloWorld.class`.
    - Utilisez la commande suivante pour packager la classe `HelloWorld` dans un fichier JAR :
      ```bash
      jar cvf HelloWorld.jar HelloWorld.class
      ```
    - Après avoir exécuté cette commande, vous devriez voir un fichier `HelloWorld.jar` dans le même répertoire.

2. **Extraction du contenu du fichier `.jar`**
    - Créez un nouveau répertoire pour extraire le contenu du fichier JAR :
      ```bash
      mkdir extracted-jar
      ```
    - Naviguez vers le répertoire `extracted-jar` :
      ```bash
      cd extracted-jar
      ```
    - Utilisez la commande suivante pour extraire le contenu du fichier `HelloWorld.jar` :
      ```bash
      jar xvf ../HelloWorld.jar
      ```
    - Vous devriez maintenant voir le fichier `HelloWorld.class` ainsi qu'un répertoire `META-INF` dans le répertoire `extracted-jar`.

3. **Exploration du contenu du manifeste**
    - Naviguez vers le répertoire `META-INF` :
      ```bash
      cd META-INF
      ```
    - Affichez le contenu du fichier `MANIFEST.MF` :
      ```bash
      cat MANIFEST.MF
      ```
    - Vous devriez voir quelque chose comme ceci :
      ```
      Manifest-Version: 1.0
      Created-By: [version] ([provider])
      ```

### Explication du contenu du manifeste :
Le fichier `MANIFEST.MF` est le manifeste du fichier JAR. Voici une brève explication de son contenu :
- `Manifest-Version` : indique la version du manifeste. La valeur standard est `1.0`.
- `Created-By` : spécifie la version du JDK et le fournisseur qui ont été utilisés pour créer le JAR.

### Conclusion :
Félicitations ! Vous avez appris à packager un fichier `.class` dans un fichier `.jar`, à extraire son contenu et à comprendre le rôle du manifeste dans un fichier JAR.


🚀 Maintenant, essayez de lancer comme habituellement la commande que vous connaissez
`java - jar HelloWorld.jar`

## Erreur "no main manifest attribute" Expliquée

Vous allez obtenir quelque chose comme :
`no main manifest attribute, in HelloWorld.jar`

C'est normal ! 



Lorsque vous rencontrez l'erreur "no main manifest attribute" en essayant d'exécuter un fichier JAR avec la commande `java -jar my.jar`, cela signifie que le fichier JAR ne contient pas d'attribut `Main-Class` dans son manifeste. L'attribut `Main-Class` indique à la JVM quelle classe contenant la méthode `main` doit être exécutée lors du lancement du JAR.

### Détails :

1. **Le Manifeste** :
   - Chaque fichier JAR contient un fichier manifeste, généralement situé dans `META-INF/MANIFEST.MF`.
   - Ce fichier manifeste contient des métadonnées sur le JAR, telles que la version du manifeste, l'auteur, etc.

2. **L'attribut Main-Class** :
   - Si vous souhaitez exécuter un fichier JAR comme une application autonome (c'est-à-dire sans spécifier explicitement la classe principale), le manifeste doit inclure un attribut `Main-Class`.
   - Cet attribut indique la classe qui contient la méthode `public static void main(String[] args)` à exécuter.
   - Par exemple, si votre classe principale est `HelloWorld`, le manifeste devrait contenir :
     ```
     Main-Class: HelloWorld
     ```

### Solution :
Pour résoudre cette erreur, assurez-vous d'inclure l'attribut `Main-Class` dans le manifeste lors de la création du fichier JAR.

## Modifier le Manifeste pour Exécuter le fichier JAR avec Succès

Si vous souhaitez exécuter un fichier JAR en utilisant la commande `java -jar`, vous devez vous assurer que le manifeste du JAR spécifie correctement la classe principale à exécuter. Voici comment vous pouvez le faire :

### Étapes :

1. **Créer un fichier manifeste personnalisé** :
   - Ouvrez votre éditeur de texte préféré.
   - Créez un nouveau fichier et nommez-le `custom-manifest.txt`.
   - Ajoutez la ligne suivante, en remplaçant `HelloWorld` par le nom de votre classe principale :
     ```
     Main-Class: HelloWorld
     ```
   - Assurez-vous d'ajouter une nouvelle ligne à la fin du fichier (c'est une exigence pour les fichiers manifeste).
   - Enregistrez et fermez le fichier.

2. **Créer le fichier JAR avec le manifeste personnalisé** :
   - Utilisez la commande suivante pour créer le fichier JAR en incluant le manifeste personnalisé :
     ```bash
     jar cvfm HelloWorld.jar custom-manifest.txt HelloWorld.class
     ```

3. **Exécuter le fichier JAR** :
   - Maintenant, vous devriez être en mesure d'exécuter le fichier JAR avec la commande :
     ```bash
     java -jar HelloWorld.jar
     ```

### Conclusion :
En incluant l'attribut `Main-Class` dans le manifeste, vous indiquez à la JVM quelle classe elle doit exécuter lors du lancement du fichier JAR. Assurez-vous toujours que cet attribut est correctement défini si vous
