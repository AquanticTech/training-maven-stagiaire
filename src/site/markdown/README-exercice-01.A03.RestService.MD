## 🚀 Création d'un module REST Hello World

### Création et initialisation du service

Créer un répertoire restService qui contient le fichier `pom.xml` suivant
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.example</groupId>
    <artifactId>rest-service</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>rest-service</name>
    <description>Module de service REST pour dire bonjour</description>

    <properties>
        <java.version>11</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>

```

### Créer l'application
Dans le répertoire src/main/java, créer la classe App.java dans le package `com.example.restService`
```java
package com.example.restservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Créer le contrôleur Springboot qui va renvoyer Hello World

Avec ce code, une fois que vous démarrez l'application, vous pouvez accéder à
`http://localhost:8080/hello` pour voir le message "Hello World.

N'oubliez pas d'ajouter ce module à votre projet Maven parent pour qu'il soit reconnu comme un sous-module.
Vous pouvez le faire en ajoutant une section <modules> dans le pom.xml de votre projet parent et en y listant le nom de l'artifactId de ce module.


```java
package com.example.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello World.";
    }
}
```

### Lancement de l'application springBoot

Pour lancer une application Spring Boot avec Maven, vous pouvez utiliser le plugin spring-boot-maven-plugin.
Voici la commande pour démarrer l'application :
```bash
mvn spring-boot:run

```

### Formatage pour que cela renvoie un objet exploitable par GraphQL ou en Json
Pour renvoyer un JSON adapté à GraphQL, nous devons structurer la réponse pour qu'elle soit facilement interrogeable par une requête GraphQL. Voici comment vous pouvez modifier le service pour renvoyer un JSON :

#### Créez un modèle pour la réponse :
```java
package com.example.restservice;

public class GreetingResponse {
private String greeting;

    public GreetingResponse(String greeting) {
        this.greeting = greeting;
    }

    public String getGreeting() {
        return greeting;
    }

    public void setGreeting(String greeting) {
        this.greeting = greeting;
    }
}
```

#### Modifiez le contrôleur pour renvoyer le modèle :
```java
package com.example.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public GreetingResponse sayHello() {
        return new GreetingResponse("Hello World M. RASATAVOHARY");
    }
}
```

Avec ces modifications, lorsque vous accédez à http://localhost:8080/hello, vous obtiendrez une réponse JSON comme celle-ci :
```json
{
"greeting": "Hello World M. RASATAVOHARY"
}
```

Cette structure est plus adaptée à GraphQL car elle renvoie un objet avec des champs nommés plutôt qu'une simple
chaîne de caractères. Si vous aviez un serveur GraphQL, vous pourriez alors interroger spécifiquement le champ
greeting ou d'autres champs que vous pourriez ajouter à l'avenir.

Exécutez cette commande à la racine du module (là où se trouve le pom.xml du module) pour démarrer l'application.
Une fois l'application démarrée, elle sera accessible à l'adresse `http://localhost:8080/hello` comme mentionné
précédemment.

### Structuration pour contextualiser et ajouter du multi-langue

Construisez un JSON GraphQL plus élaboré qui intègre des variations de la salutation "Hello" selon différents pays,
en adaptant la formulation en fonction des contextes spécifiques.

D'accord, voici comment vous pouvez structurer le service pour renvoyer le JSON complexe basé sur les salutations dans différents pays et situations :

#### Modèles pour la réponse :

#### GreetingSituation.java :

```java
package com.example.restservice;

public class GreetingSituation {
private String context;
private String greeting;

    public GreetingSituation(String context, String greeting) {
        this.context = context;
        this.greeting = greeting;
    }

    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public String getGreeting() {
        return greeting;
    }

    public void setGreeting(String greeting) {
        this.greeting = greeting;
    }
}
```

#### CountryGreeting.java :

```java
package com.example.restservice;

import java.util.List;

public class CountryGreeting {
private String country;
private String language;
private List<GreetingSituation> situations;

    public CountryGreeting(String country, String language, List<GreetingSituation> situations) {
        this.country = country;
        this.language = language;
        this.situations = situations;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public List<GreetingSituation> getSituations() {
        return situations;
    }

    public void setSituations(List<GreetingSituation> situations) {
        this.situations = situations;
    }
}
```

#### Contrôleur pour renvoyer le modèle :

##### HelloController.java :

```java
package com.example.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
public class HelloController {

    @GetMapping("/greetings")
    public List<CountryGreeting> getGreetings() {
        return Arrays.asList(
            new CountryGreeting("France", "French", Arrays.asList(
                new GreetingSituation("Formal", "Bonjour"),
                new GreetingSituation("Informal", "Salut")
            )),
            new CountryGreeting("Spain", "Spanish", Arrays.asList(
                new GreetingSituation("Formal", "Buenos días"),
                new GreetingSituation("Informal", "Hola")
            )),
            new CountryGreeting("Japan", "Japanese", Arrays.asList(
                new GreetingSituation("Formal", "こんにちは (Konnichiwa)"),
                new GreetingSituation("Informal", "やあ (Yaa)")
            ))
        );
    }
}
```

Avec ce code, lorsque vous accédez à [http://localhost:8080/greetings](http://localhost:8080/greetings),
vous obtiendrez la structure JSON complexe des salutations dans différents pays et situations.

### Ajout d'une route qui permet de récupérer des éléments en fonction de la langue

#### Ajout d'une Route

Ajoutez une route qui prend en compte la langue et la situation comme paramètres et renvoie la salutation correspondante.

#### Mise à jour du contrôleur

**Modifiez le fichier `HelloController.java` pour intégrer la nouvelle route :**

```java
package com.example.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

@RestController
public class HelloController {

    private final List<CountryGreeting> greetings = Arrays.asList(
        new CountryGreeting("France", "French", Arrays.asList(
            new GreetingSituation("Formal", "Bonjour"),
            new GreetingSituation("Informal", "Salut")
        )),
        new CountryGreeting("Spain", "Spanish", Arrays.asList(
            new GreetingSituation("Formal", "Buenos días"),
            new GreetingSituation("Informal", "Hola")
        )),
        new CountryGreeting("Japan", "Japanese", Arrays.asList(
            new GreetingSituation("Formal", "こんにちは (Konnichiwa)"),
            new GreetingSituation("Informal", "やあ (Yaa)")
        ))
    );

    @GetMapping("/greetings")
    public List<CountryGreeting> getGreetings() {
        return greetings;
    }

    @GetMapping("/greeting")
    public String getGreetingByLanguageAndSituation(
            @RequestParam String language,
            @RequestParam String situation) {
        for (CountryGreeting countryGreeting : greetings) {
            if (countryGreeting.getLanguage().equalsIgnoreCase(language)) {
                for (GreetingSituation greetingSituation : countryGreeting.getSituations()) {
                    if (greetingSituation.getContext().equalsIgnoreCase(situation)) {
                        return greetingSituation.getGreeting();
                    }
                }
            }
        }
        return "Salutation non trouvée pour la langue et la situation spécifiées.";
    }
}
```

Avec cette mise à jour, vous pouvez accéder à la route [http://localhost:8080/greeting?language=French&situation=Formal](http://localhost:8080/greeting?language=French&situation=Formal)
pour obtenir la salutation "Bonjour".

Si vous fournissez une langue ou une situation non reconnue, le service renverra "Salutation non trouvée pour la langue et la situation spécifiées.".


### Ajout d'une dépendance qui permet d'exposer une route Swagger de l'API REST

Le module expose deux routes REST que l'on peut documenter au format openAPI de la façon suivante :
```yml
openapi: 3.0.0
info:
  version: "1.0.0"
  title: "Hello Service API"
  description: "API pour obtenir des salutations basées sur la langue et la situation."

paths:
  /greetings:
    get:
      summary: "Obtenir toutes les salutations"
      description: "Renvoie une liste de salutations pour différents pays et situations."
      responses:
        '200':
          description: "Liste des salutations par pays"
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/CountryGreeting'

  /greeting:
    get:
      summary: "Obtenir une salutation spécifique"
      description: "Renvoie une salutation basée sur la langue et la situation fournies."
      parameters:
        - name: language
          in: query
          description: "Langue pour laquelle obtenir la salutation."
          required: true
          schema:
            type: string
        - name: situation
          in: query
          description: "Situation pour laquelle obtenir la salutation (par exemple, 'Formal' ou 'Informal')."
          required: true
          schema:
            type: string
      responses:
        '200':
          description: "Salutation basée sur la langue et la situation"
          content:
            text/plain:
              schema:
                type: string

components:
  schemas:
    GreetingSituation:
      type: object
      properties:
        context:
          type: string
          description: "Contexte de la salutation (par exemple, 'Formal' ou 'Informal')."
        greeting:
          type: string
          description: "Texte de la salutation."
    CountryGreeting:
      type: object
      properties:
        country:
          type: string
          description: "Nom du pays."
        language:
          type: string
          description: "Langue du pays."
        situations:
          type: array
          items:
            $ref: '#/components/schemas/GreetingSituation'

```
Si vous copiez / coller ce code dans la partie édition de code de https://editor.swagger.io/, vous pourrez visualiser la route associée.

#### Documentation Swagger

#### Intégration de Swagger à Spring Boot

Pour tester les routes avec Swagger, suivez ces étapes pour intégrer Swagger à votre projet Spring Boot :

#### 1. Ajouter les dépendances à `pom.xml` :

```xml
<!-- Swagger dependencies -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-boot-starter</artifactId>
    <version>3.0.0</version>
</dependency>
```

### 2. Configurer Swagger

Créez une classe de configuration pour Swagger, par exemple `SwaggerConfig.java` :

```java
package com.example.restservice;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.restservice"))
                .paths(PathSelectors.any())
                .build();
    }
}
```

### 3. Lancer votre application Spring Boot

Si vous utilisez Maven, exécutez la commande suivante à la racine de votre projet :

```bash
mvn spring-boot:run
```

### 4. Accéder à l'interface Swagger UI

Ouvrez votre navigateur et accédez à :

```
http://localhost:8080/swagger-ui/
```
Vous verrez l'interface Swagger UI avec vos routes listées. Vous pouvez cliquer sur chaque route pour voir les détails et même tester les routes directement depuis l'interface.

## Ajout d'une Route pour Afficher les Options

Pour faciliter l'utilisation des endpoints, vous pouvez ajouter une route qui affiche les options possibles de langue et
de situation. Voici comment procéder :

### 1. Mise à jour du contrôleur `HelloController.java` :

```java
// ... (autres imports)
import java.util.Map;
//import java.util.stream.Collectors;

public class HellowWorld{
    // ... (début de la classe HelloController)
    @GetMapping("/options")
    public Map<String, List<String>> getAvailableOptions() {
        Map<String, List<String>> options = greetings.stream()
                .collect(Collectors.toMap(
                        CountryGreeting::getLanguage,
                        countryGreeting -> countryGreeting.getSituations().stream()
                                .map(GreetingSituation::getContext)
                                .collect(Collectors.toList())
                ));
        return options;
    }
}
```

### 2. Explication :

La nouvelle route `/options` renvoie un objet JSON où chaque clé est une langue disponible et
chaque valeur est une liste des situations disponibles pour cette langue. Par exemple, le résultat pourrait ressembler
à ceci :

\```json
{
"French": ["Formal", "Informal"],
"Spanish": ["Formal", "Informal"],
"Japanese": ["Formal", "Informal"]
}
\```

### 3. Utilisation :

Après avoir ajouté cette route, vous pouvez accéder à `http://localhost:8080/options` pour obtenir la liste des
langues et des situations disponibles. Cela facilite l'utilisation des autres endpoints car les utilisateurs peuvent
d'abord consulter les options disponibles

##  🚀 Création d'un module Maven pour afficher le contenu du service REST

### 1. Initialisation du module Maven
Créez un nouveau module Maven en utilisant l'archétype `maven-archetype-webapp`.

```bash
mvn archetype:generate -DgroupId=com.example -DartifactId=jspmodule -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```

### 2. Ajout des dépendances
Dans le fichier `pom.xml` du module, ajoutez les dépendances nécessaires pour Spring Boot, JSP et le client REST.

```xml
<dependencies>
    <!-- Spring Boot Starter Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- JSTL pour les tags JSP -->
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>jstl</artifactId>
    </dependency>
    <!-- Spring Boot Starter Data Rest pour le client REST -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-rest</artifactId>
    </dependency>
</dependencies>
```

### 3. Configuration de Spring Boot
Assurez-vous que votre classe principale étend `SpringBootServletInitializer` pour prendre en charge les JSP.

Dans votre module exercice-03.restService, par exemple écrivez :
```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

@SpringBootApplication
public class App extends SpringBootServletInitializer {

    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
```


### 4. Création de la page JSP
Dans le répertoire `src/main/webapp/WEB-INF/views/`, créez un fichier `greeting.jsp` pour afficher le contenu du service REST.
Voici le code la page JSP
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>${message}</h1>
</body>
</html>
```


### 5. Contrôleur Spring Boot
Créez un contrôleur pour récupérer les données du service REST et les transmettre à la page JSP.
Voici le code de ce contrôleur
```java
package com.example.restservice;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class GreetingController {

    @GetMapping("/greeting-view")
    public String getGreeting(Model model) {
        // Ici, je suppose que vous avez un service ou une méthode pour obtenir le message.
        // Pour cet exemple, je vais simplement utiliser une chaîne statique.
        String greetingMessage = "Hello from Spring Boot!";
        model.addAttribute("message", greetingMessage);
        return "greeting";
    }
}
```


### 6. Configuration des vues
Dans `src/main/resources`, ajoutez ou modifiez le fichier `application.properties` pour configurer le préfixe et le suffixe des vues.

```properties
spring.mvc.view.prefix=/WEB-INF/views/
spring.mvc.view.suffix=.jsp
```

### 7. Exécution
Lancez votre application Spring Boot et accédez à la route appropriée pour voir le contenu du service REST affiché à l'aide de la page JSP.


## Génération de fichiers `.jar` et `.war` pour votre application Spring Boot

### 1. Mise à jour du fichier `pom.xml`

#### 1.1. Ajout de la dépendance `spring-boot-starter-tomcat`

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-tomcat</artifactId>
    <scope>provided</scope>
</dependency>
```

Cette dépendance garantit que Tomcat n'est pas inclus dans le fichier `.jar` car il est déjà fourni par le conteneur
lors de l'exécution du fichier `.war`.

#### 1.2. Configuration du plugin `spring-boot-maven-plugin`

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                    <configuration>
                        <classifier>jar</classifier>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

Le `<classifier>jar</classifier>` garantit que le fichier `.jar` est généré avec un suffixe `-jar`.

### 2. Génération des fichiers

Exécutez la commande Maven suivante :

```bash
mvn clean package
```

Après l'exécution, vous devriez voir deux fichiers dans le répertoire `target` :

- `your-artifact-id.jar` : Le fichier `.jar` exécutable.
- `your-artifact-id-war.jar` : Le fichier `.jar` avec le suffixe `-jar`.
- `your-artifact-id.war` : Le fichier `.war` pour le déploiement.

### 3. Exécution

Pour exécuter le fichier `.jar` :

```bash
java -jar target/your-artifact-id.jar
```

Pour déployer le fichier `.war`, copiez-le dans le répertoire `webapps` de Tomcat et démarrez le serveur.

> **Note** : Remplacez `your-artifact-id` par l'ID d'artefact réel de votre projet.

