## Exercice : Création d'une application Maven avec StringUtils et tests unitaires

### Objectif :
Dans cet exercice, vous allez créer une application Maven qui utilise la classe `StringUtils` de Apache Commons Lang pour manipuler une chaîne de caractères. Vous générerez également un JAR exécutable et ajouterez un test unitaire pour votre application.

### Étapes :

1. **Initialisation du projet Maven** :
   Créez un nouveau projet Maven en utilisant l'archétype `maven-archetype-quickstart` :
   ```bash
   mvn archetype:generate -DgroupId=com.example -DartifactId=myapp -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

2. **Ajout de la dépendance** :
   Dans le fichier `pom.xml` de votre projet, ajoutez la dépendance pour `commons-lang3` :
   ```xml
   <dependency>
       <groupId>org.apache.commons</groupId>
       <artifactId>commons-lang3</artifactId>
       <version>3.12.0</version>
   </dependency>
   ```

3. **Création de la classe HelloWorld** :
   Dans le répertoire `src/main/java/com/example`, créez une classe `HelloWorld` :
   ```java
   package com.example;

   import org.apache.commons.lang3.StringUtils;

   public class HelloWorld {
       public String getGreeting() {
           return StringUtils.capitalize("hello world");
       }

       public static void main(String[] args) {
           HelloWorld helloWorld = new HelloWorld();
           System.out.println(helloWorld.getGreeting());
       }
   }
   ```

4. **Génération d'un JAR exécutable** :
   Modifiez votre `pom.xml` pour inclure le plugin `maven-jar-plugin` et `maven-shade-plugin` pour créer un JAR exécutable :
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
                           <mainClass>com.example.HelloWorld</mainClass>
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

   Exécutez la commande suivante pour générer le JAR :
   ```bash
   mvn clean package
   ```

5. **Mise à jour de la version de Java** :
   L'erreur que vous avez rencontrée est due à l'utilisation d'une version obsolète de Java pour la compilation. Pour résoudre ce problème, vous devez spécifier une version de Java prise en charge dans votre `pom.xml`.

   Ajoutez ou modifiez la section `properties` de votre `pom.xml` pour spécifier la version de Java que vous souhaitez utiliser (par exemple, Java 8) :

   ```xml
   <properties>
       <maven.compiler.source>1.8</maven.compiler.source>
       <maven.compiler.target>1.8</maven.compiler.target>
   </properties>
   ```

   Avec cette modification, Maven utilisera Java 8 pour la compilation, ce qui devrait résoudre l'erreur.

   Une fois cette modification effectuée, essayez de reconstruire votre projet avec la commande :
   ```bash
   mvn clean package
   ```

   Si tout se passe bien, vous ne devriez plus voir l'erreur et votre projet devrait être compilé avec succès.


6. **Ajout d'un test unitaire** :
   Dans le répertoire `src/test/java/com/example`, créez une classe `HelloWorldTest` :
   ```java
   package com.example;

   import org.junit.Assert;
   import org.junit.Test;

   public class HelloWorldTest {
       @Test
       public void testGetGreeting() {
           HelloWorld helloWorld = new HelloWorld();
           Assert.assertEquals("Hello world", helloWorld.getGreeting());
       }
   }
   ```

   Exécutez les tests avec la commande :
   ```bash
   mvn test
   ```

7. Vous allez obtenir une erreur en raison de la librairie JUnit de départ, modifiez votre pom.xml
avec le contenu suivant : 
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>myapp</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>myapp</name>
  <url>http://maven.apache.org</url>
  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
  </properties>
  <dependencies>
    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.12.0</version>
    </dependency>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-jar-plugin</artifactId>
        <version>3.2.0</version>
        <configuration>
          <archive>
            <manifest>
              <mainClass>com.example.HelloWorld</mainClass>
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
</project>
```
8. ** Relancez les commandes maven pour pouvoir compiler / builder**
```bash
mvn clean install
mvn clean package 
java -jar ./target/votrejar.jar
```

### Conclusion :
À la fin de cet exercice, vous aurez créé une application Maven simple qui utilise `StringUtils` pour manipuler des chaînes de caractères, généré un JAR exécutable et ajouté un test unitaire pour votre application.
