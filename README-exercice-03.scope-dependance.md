## Exercice : Tester le Scope de Dépendances Maven

### Objectif :
Dans cet exercice, vous allez explorer les différents scopes de dépendances Maven (`compile`, `test`, `runtime`, `provided`) et observer leur comportement lors de la compilation, de l'exécution des tests et de l'exécution du projet.

### Étapes :

1. **Initialisation du Projet** :
   Créez un nouveau projet Maven en utilisant l'archétype `maven-archetype-quickstart`.

   ```bash
   mvn archetype:generate -DgroupId=com.example -DartifactId=dependency-scope-test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

2. **Ajout des Dépendances** :
   Ouvrez le fichier `pom.xml` généré et ajoutez les dépendances suivantes :

   ```xml
   <!-- Dépendance avec le scope 'compile' -->
   <dependency>
       <groupId>junit</groupId>
       <artifactId>junit</artifactId>
       <version>4.12</version>
       <scope>compile</scope>
   </dependency>

   <!-- Dépendance avec le scope 'test' -->
   <dependency>
       <groupId>org.mockito</groupId>
       <artifactId>mockito-core</artifactId>
       <version>3.3.3</version>
       <scope>test</scope>
   </dependency>

   <!-- Dépendance avec le scope 'runtime' -->
   <dependency>
       <groupId>com.google.code.gson</groupId>
       <artifactId>gson</artifactId>
       <version>2.8.6</version>
       <scope>runtime</scope>
   </dependency>

   <!-- Dépendance avec le scope 'provided' -->
   <dependency>
       <groupId>javax.servlet</groupId>
       <artifactId>javax.servlet-api</artifactId>
       <version>4.0.1</version>
       <scope>provided</scope>
   </dependency>
   ```

3. **Écriture du Code** :
   Dans le fichier `App.java` généré, essayez d'importer et d'utiliser une classe de chaque dépendance. Par exemple, utilisez `JUnit` pour un test simple, `Mockito` pour mocker un objet, `Gson` pour convertir un objet en JSON, et `Servlet` pour simuler une requête.

4. **Compilation et Tests** :
   Compilez le projet et exécutez les tests.

   ```bash
   mvn clean compile test
   ```

5. **Observations** :
    - Notez les erreurs, le cas échéant.
    - Essayez d'exécuter le projet avec `mvn exec:java` et observez les erreurs.
    - Réfléchissez à la raison pour laquelle certaines dépendances sont disponibles à certaines étapes et pas à d'autres.

### Conclusion :
À la fin de cet exercice, vous devriez avoir une compréhension claire de la manière dont les différents scopes de dépendances Maven affectent la disponibilité des dépendances à différentes étapes du cycle de vie du projet.
