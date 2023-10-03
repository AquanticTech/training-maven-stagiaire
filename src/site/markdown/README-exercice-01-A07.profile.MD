# Utilisation des profils 

## Utilisations courantes des profils Maven

Les profils Maven sont un puissant outil dans Maven qui permet de configurer différents aspects de la construction de votre projet en fonction de l'environnement ou d'autres facteurs. Voici quelques utilisations courantes des profils Maven :

1. **Configuration spécifique à l'environnement**  
   Vous pouvez avoir des configurations différentes pour les environnements de développement, de test et de production. Par exemple, vous pourriez vouloir utiliser une base de données H2 en développement, mais PostgreSQL en production.


2. **Activation de plugins spécifiques**  
   Certains plugins peuvent être nécessaires uniquement dans certains environnements ou sous certaines conditions. Avec les profils, vous pouvez activer ou désactiver ces plugins selon les besoins.


3. **Gestion des dépendances**  
   Dans certains cas, vous pourriez vouloir utiliser différentes versions d'une dépendance ou même différentes dépendances en fonction de l'environnement ou de la plateforme.


4. **Filtrage des ressources**  
   Comme mentionné dans l'exercice précédent, les profils peuvent être utilisés pour filtrer différentes ressources en fonction du profil actif.


5. **Paramétrage de propriétés**  
   Les profils peuvent être utilisés pour définir différentes propriétés qui peuvent ensuite être utilisées dans votre fichier `pom.xml` ou dans votre code.


6. **Activation basée sur le système d'exploitation**  
   Vous pouvez avoir des profils qui sont activés en fonction du système d'exploitation sur lequel la construction est exécutée. Par exemple, vous pourriez avoir un profil pour Windows et un autre pour Linux.


7. **Activation basée sur la présence ou l'absence d'une propriété**  
   Vous pouvez activer un profil en fonction de la présence ou de l'absence d'une propriété système ou d'une propriété définie par l'utilisateur.


8. **Activation basée sur la version de Java**  
   Si votre projet doit être construit avec différentes versions de Java, vous pouvez utiliser des profils pour gérer cela.


9. **Exécution de tests spécifiques**  
   Vous pouvez utiliser des profils pour exécuter un ensemble spécifique de tests en fonction du profil actif.


10. **Gestion des répertoires de déploiement**  
    Si vous déployez votre application dans différents répertoires ou serveurs en fonction de l'environnement, les profils peuvent être utilisés pour gérer cela.


# Exercice sur l'utilisation des Profils Maven

# Objectif de l'exercice
L'objectif de cet exercice est d'apprendre comment utiliser les profils Maven pour personnaliser la génération du site d'un projet Maven en fonction de différents environnements ou besoins.

## Prérequis
- Connaissance de base de Maven.
- Un projet Maven existant avec un fichier `pom.xml`.
- Maven installé sur votre système.

## Etape 0 : Créer un projet maven simple

`mvn archetype:generate -DgroupId=com.example -DartifactId=my-maven-project -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
`

## Étape 1 : Configuration du fichier `pom.xml`
1. Ouvrez votre projet Maven existant.
2. Modifiez le fichier `pom.xml` pour inclure un plugin Maven Site. Vous pouvez utiliser le plugin Maven Site par défaut pour cet exercice.

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-site-plugin</artifactId>
            <version>3.9.1</version>
            <configuration>
                <skip>${site.skip}</skip>
            </configuration>        </plugin>
    </plugins>
</build>
```

## Étape 2 : Création de profils Maven
Ajoutez deux profils Maven dans le fichier pom.xml. L'un sera destiné à la génération du site pour le développement, et l'autre pour la production.
Mettez les profils avant la partie `<build>` du fichier `pom.xml`.

```xml
<profiles>
    <profile>
        <id>dev</id>
        <properties>
            <site.skip>true</site.skip>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-site-plugin</artifactId>
                    <configuration>
                        <reportPlugins>
                            <plugin>
                                <groupId>org.apache.maven.plugins</groupId>
                                <artifactId>maven-project-info-reports-plugin</artifactId>
                            </plugin>
                        </reportPlugins>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </profile>
    <profile>
        <id>prod</id>
        <properties>
            <site.skip>false</site.skip>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-site-plugin</artifactId>
                    <configuration>
                        <reportPlugins>
                            <plugin>
                                <groupId>org.apache.maven.plugins</groupId>
                                <artifactId>maven-project-info-reports-plugin</artifactId>
                            </plugin>
                            <!-- Ajoutez d'autres plugins pour la production si nécessaire -->
                        </reportPlugins>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

## Étape 3 : Génération du site avec les profils
1. Ouvrez un terminal dans le répertoire de votre projet.
2. Utilisez la commande Maven pour générer le site en spécifiant le profil souhaité. Par exemple, pour générer le site en utilisant le profil de développement, exécutez :

```bash
mvn site -Pdev
```
Ou pour le profil de production :

```bash
mvn site -Pprod
```

## Étape 4 : Vérification des résultats

1. Après avoir exécuté la commande correspondant au profil, accédez au répertoire `target/site` de votre projet.
2. Vérifiez les différences entre les sites générés en utilisant les deux profils. 
3. Les plugins et les informations incluses dans le site peuvent différer en fonction du profil.

## Conclusion
Cet exercice vous a permis de découvrir comment utiliser les profils Maven pour personnaliser la génération du site d'un projet en fonction des besoins spécifiques à chaque environnement. Les profils Maven sont utiles pour gérer les configurations, les plugins et les dépendances en fonction des différentes phases de développement et de déploiement de votre projet.
