# Exercice Exploratoire : Exploration du projet Spring PetClinic avec HTMX

## Objectif
Explorer le projet [Spring PetClinic avec HTMX](https://github.com/spring-petclinic/spring-petclinic-htmx) pour comprendre sa structure, ses fonctionnalités et ses composants clés.

## Étapes

### 1. Clonage et initialisation du projet
- Clonez le dépôt [spring-petclinic-htmx](https://github.com/spring-petclinic/spring-petclinic-htmx) sur votre machine locale.
- Ouvrez le projet dans votre IDE préféré et familiarisez-vous avec la structure du projet.

### 2. Exploration des composants principaux
- Examinez les packages principaux du projet : `model`, `owner`, `system`, `vet`. Chaque package représente un module fonctionnel du projet.
- Explorez les classes et interfaces clés dans chaque package, par exemple :
    - [PetClinicApplication.java](https://github.com/spring-petclinic/spring-petclinic-htmx/blob/main/src/main/java/org/springframework/samples/petclinic/PetClinicApplication.java)
    - [OwnerController.java](https://github.com/spring-petclinic/spring-petclinic-htmx/blob/main/src/main/java/org/springframework/samples/petclinic/owner/OwnerController.java)
    - [VetController.java](https://github.com/spring-petclinic/spring-petclinic-htmx/blob/main/src/main/java/org/springframework/samples/petclinic/vet/VetController.java)

### 3. Exploration des ressources et configurations
- Naviguez vers le répertoire `src/main/resources` et examinez les fichiers de configuration et les ressources.
- Familiarisez-vous avec les fichiers de configuration de la base de données, les propriétés de l'application et les templates.

### 4. Exécution et test du projet
- Suivez les instructions du fichier [readme.md](https://github.com/spring-petclinic/spring-petclinic-htmx/blob/main/readme.md) pour exécuter le projet localement.
- Testez les différentes fonctionnalités de l'application : ajout d'un propriétaire, ajout d'un animal de compagnie, prise de rendez-vous, etc.

### 5. Exploration des tests
- Naviguez vers le répertoire `src/test` et examinez les tests unitaires et d'intégration fournis avec le projet.
- Exécutez les tests pour vous assurer que tout fonctionne correctement.

### 6. Exploration des fichiers de configuration Maven et Gradle
- Examinez les fichiers de configuration Maven (`pom.xml`) et Gradle (`build.gradle`) pour comprendre les dépendances et les plugins utilisés.

### 7. Exploration avancée (optionnel)
- Si vous êtes familiarisé avec Spring Boot et HTMX, essayez de modifier certaines fonctionnalités ou d'ajouter de nouvelles fonctionnalités à l'application.
- Explorez les fichiers de style et les ressources statiques pour comprendre le design et l'interface utilisateur de l'application.

# Modification du projet Spring PetClinic avec HTMX pour la création d'un package RPM

## Étapes

### 1. Ajout du plugin `rpm-maven-plugin` dans `pom.xml`

Ajoutez la configuration suivante dans la section `<plugins>` de votre `pom.xml` :

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>rpm-maven-plugin</artifactId>
    <version>2.2.0</version>
    <executions>
        <execution>
            <goals>
                <goal>rpm</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <name>spring-petclinic-htmx</name>
        <version>1.0</version>
        <release>1</release>
        <group>Application/Internet</group>
        <description>Spring PetClinic with HTMX</description>
        <targetOS>linux</targetOS>
        <mappings>
            <mapping>
                <directory>/opt/spring-petclinic-htmx</directory>
                <sources>
                    <source>
                        <location>target/spring-petclinic-htmx-3.0.0-SNAPSHOT.jar</location>
                    </source>
                </sources>
            </mapping>
        </mappings>
    </configuration>
</plugin>
```

```bash 
mvn clean package rpm:rpm
```
### 3. Vérification du package RPM
Une fois la commande précédente terminée, le package RPM sera généré dans le répertoire target/rpm/spring-petclinic-htmx/RPMS/noarch/.

## 4. Installation du package RPM (optionnel)
Si vous souhaitez installer le package RPM sur une machine Linux, utilisez la commande suivante :

```
  sudo rpm -ivh target/rpm/spring-petclinic-htmx/RPMS/noarch/spring-petclini
```
