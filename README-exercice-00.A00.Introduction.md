## Exercice : Création, Compilation et Exécution d'une Classe Java

### Objectif :
Apprendre à créer une classe Java en local, la compiler avec `javac` et l'exécuter avec `java`.

### Étapes :

1. **Création de la classe `HelloWorld.java`**
    - Ouvrez votre éditeur de texte préféré.
    - Créez un nouveau fichier et nommez-le `HelloWorld.java`.
    - Dans ce fichier, ajoutez le code suivant :
      ```java
      public class HelloWorld {
          public static void main(String[] args) {
              System.out.println("Hello, World!");
          }
      }
      ```
    - Enregistrez et fermez le fichier.

2. **Compilation de la classe**
    - Ouvrez l'invite de commande ou le terminal.
    - Naviguez vers le répertoire où vous avez enregistré `HelloWorld.java` en utilisant la commande `cd`.
    - Compilez la classe en utilisant la commande suivante :
      ```bash
      javac HelloWorld.java
      ```
    - Si tout se passe bien, vous devriez voir un nouveau fichier `HelloWorld.class` dans le même répertoire.

3. **Exécution de la classe**
    - Toujours dans l'invite de commande ou le terminal, exécutez la classe compilée avec la commande :
      ```bash
      java HelloWorld
      ```
    - Vous devriez voir le message `Hello, World!` s'afficher à l'écran.

4. ** Voir le contenu du code généré**
    - Vous pouvez afficher le contenu du code généré par curiosité en faisant la commande 
   ```bash 
      javap -c -verbose HelloWorld
   ```

### Conclusion :
Félicitations ! Vous avez créé, compilé et exécuté avec succès une classe Java en utilisant les outils en ligne de commande.
Maven ne fait ni plus ni moins que compiler les fichiers .java en .class
tout en packageant le logiciel pour qu'il se lance partout et en gérant les dépendances.

