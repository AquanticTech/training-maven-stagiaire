## Exercice : Utilisation du plugin Maven Surefire

### Objectif :
Intégrer et utiliser le plugin Maven Surefire pour exécuter des tests unitaires dans un projet Maven.

### Instructions :

1. **Création d'un nouveau projet Maven**
    - Si vous n'avez pas encore de projet Maven, créez-en un en utilisant l'archétype `maven-archetype-quickstart`.
      ```bash
      mvn archetype:generate -DgroupId=com.votreentreprise -DartifactId=mon-projet-test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
      ```

2. **Ajout du plugin Surefire**
    - Ouvrez le fichier `pom.xml` de votre projet.
    - Ajoutez la configuration du plugin Surefire dans la section `<plugins>` de votre `pom.xml`.
      ```xml
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.0.0-M5</version>
      </plugin>
      ```

3. **Écriture d'un test unitaire simple**
    - Dans le répertoire `src/test/java`, créez une nouvelle classe de test nommée `MaClasseTest`.
    - Ajoutez le code suivant pour créer un test unitaire simple :
      ```java
      import org.junit.Assert;
      import org.junit.Test;
 
      public class MaClasseTest {
 
          @Test
          public void monTestSimple() {
              Assert.assertTrue(true);
          }
      }
      ```

4. **Exécution des tests**
    - Dans votre terminal, naviguez jusqu'au répertoire racine de votre projet.
    - Exécutez la commande suivante pour lancer les tests :
      ```bash
      mvn test
      ```

5. **Vérification**
    - Assurez-vous que le test s'exécute avec succès et que vous voyez un message indiquant que le test a réussi.

### Questions :

1. Quel est le rôle du plugin Maven Surefire ?
2. Comment spécifier une version spécifique du plugin Surefire dans le `pom.xml` ?
3. Comment exécuter un test unitaire spécifique au lieu de tous les tests ?
