## Exercice : Utilisation de la librairie StringUtils dans une Application Java

### Objectif :
Dans cet exercice, vous apprendrez à utiliser la librairie `StringUtils` pour manipuler des chaînes de caractères, à compiler le code en faisant référence à cette librairie, et à générer un fichier JAR qui intègre la librairie.

### Étapes :

1. **Utilisation de StringUtils dans le code** :
    - Ouvrez votre éditeur de texte préféré.
    - Créez un nouveau fichier et nommez-le `HelloWorld.java`.
    - Ajoutez le code suivant :
      ```java
      import org.apache.commons.lang3.StringUtils;
 
      public class HelloWorld {
          public static void main(String[] args) {
              String message = "Hello World";
              String upperCaseMessage = StringUtils.upperCase(message);
              System.out.println(upperCaseMessage);
          }
      }
      ```
    - Enregistrez et fermez le fichier.

2. **Téléchargement de la librairie StringUtils** :
    - Vous pouvez télécharger la librairie `StringUtils` (qui fait partie de Apache Commons Lang) depuis le site officiel d'Apache Commons.
    - Pour cet exercice, supposons que vous ayez téléchargé le fichier `commons-lang3-x.x.x.jar` et l'ayez enregistré dans le répertoire courant.
    - La page de référence : https://commons.apache.org/proper/commons-lang/download_lang.cgi
    - Le lien de téléchargement : https://dlcdn.apache.org//commons/lang/binaries/commons-lang3-3.13.0-bin.zip

3. **Compilation du code avec référence à la librairie** :
    - Ouvrez l'invite de commande ou le terminal.
    - Compilez le fichier `HelloWorld.java` en faisant référence à la librairie :
      ```bash
      javac -cp commons-lang3-3.13.0.jar HelloWorld.java
      ```

4. **Génération du fichier JAR intégrant la librairie** :
    - Créez un manifeste personnalisé nommé `custom-manifest.txt` avec le contenu suivant :
      ```
      Main-Class: HelloWorld
      Class-Path: commons-lang3-3.13.0.jar
      ```
      Assurez-vous d'ajouter une nouvelle ligne à la fin.
    - Générez le fichier JAR :
      ```bash
      jar cvfm HelloWorld.jar custom-manifest.txt HelloWorld.class
      ```

5. **Exécution du fichier JAR** :
    - Pour exécuter le fichier JAR, utilisez la commande :
      ```bash
      java -jar HelloWorld.jar
      ```

### Conclusion :
Vous avez appris à utiliser une librairie externe dans votre code Java, à compiler le code en faisant référence à cette librairie, et à générer un fichier JAR qui intègre la librairie. L'utilisation correcte du `Classpath` est essentielle pour assurer le bon fonctionnement de votre application.
