## Exercice : Gestion des Dépendances Optionnelles et Transitives avec Maven

### Objectif :
Dans cet exercice, vous allez explorer la gestion des dépendances optionnelles et transitives avec Maven, ainsi que comprendre l'impact des scopes sur ces dépendances.

### Étapes :

1. **Initialisation du Projet** :
   Créez un nouveau projet Maven en utilisant l'archétype `maven-archetype-quickstart`.

   ```bash
   mvn archetype:generate -DgroupId=com.example -DartifactId=dependency-management-test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

2. **Ajout d'une Dépendance Optionnelle** :
   Ajoutez une dépendance à votre projet et marquez-la comme optionnelle.

   ```xml
   <dependency>
       <groupId>org.apache.commons</groupId>
       <artifactId>commons-lang3</artifactId>
       <version>3.12.0</version>
       <optional>true</optional>
   </dependency>
   ```

   Les dépendances optionnelles ne sont pas transmises à des projets dépendants. Elles sont utiles pour les situations où une fonctionnalité est disponible seulement si une bibliothèque est présente.

3. **Ajout d'une Dépendance avec des Dépendances Transitives** :
   Ajoutez une dépendance qui a ses propres dépendances (dépendances transitives).

   ```xml
   <dependency>
       <groupId>com.google.guava</groupId>
       <artifactId>guava</artifactId>
       <version>30.1-jre</version>
   </dependency>
   ```

   Maven gère automatiquement les dépendances transitives. Si `guava` dépend d'autres bibliothèques, Maven les téléchargera et les ajoutera à votre classpath.

4. **Gestion des Scopes avec les Dépendances Transitives** :
   Si une dépendance transitive a un scope différent de la dépendance principale, Maven utilisera le scope le plus restrictif. Par exemple, si votre dépendance principale a un scope `compile` et la dépendance transitive a un scope `test`, Maven utilisera le scope `test` pour la dépendance transitive.

5. **Observations** :
    - Exécutez `mvn dependency:tree` pour voir l'arbre des dépendances de votre projet.
    - Notez les dépendances optionnelles et les dépendances transitives.
    - Essayez de changer le scope de vos dépendances et observez comment cela affecte l'arbre des dépendances.

### Conclusion :
À la fin de cet exercice, vous devriez avoir une compréhension approfondie de la manière dont Maven gère les dépendances optionnelles et transitives, ainsi que de l'impact des scopes sur ces dépendances.
