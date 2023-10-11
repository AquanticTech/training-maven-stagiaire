# Exercice : Utilisation du fichier `assembly.xml` avec Maven

## Objectif

Créer un projet Maven simple et utiliser le fichier `assembly.xml` pour filtrer et préparer le contenu d'un fichier de sortie.

## Étapes

### 1. Initialisation du projet

- Créez un nouveau projet Maven en utilisant l'archétype `maven-archetype-quickstart`.
- Naviguez vers le répertoire du projet et ouvrez le fichier `pom.xml`.

### 2. Ajout de la dépendance `maven-assembly-plugin`

- Dans le fichier `pom.xml`, ajoutez la dépendance pour le plugin `maven-assembly-plugin`.

### 3. Création du fichier `assembly.xml`

- Dans le répertoire `src/main/assembly`, créez un fichier nommé `assembly.xml`.
- Dans ce fichier, ajoutez la configuration suivante :

```xml

<assembly>
    <id>filtered-content</id>
    <formats>
        <format>zip</format>
    </formats>
    <fileSets>
        <fileSet>
            <directory>src/main/resources</directory>
            <outputDirectory>/</outputDirectory>
            <filtered>true</filtered>
            <includes>
                <include>**/*.properties</include>
            </includes>
        </fileSet>
    </fileSets>
</assembly>
```

### 4. Création d'un fichier de propriétés

Dans le répertoire src/main/resources, créez un fichier nommé app.properties.
Ajoutez quelques propriétés de test, par exemple :

   ```bash
   
   app.name=Mon Application
   app.version=${project.version}
   ```

### 5. Configuration du filtrage dans pom.xml

Dans le fichier pom.xml, ajoutez la configuration suivante pour activer le filtrage :

   ```xml   

<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <filtering>true</filtering>
        </resource>
    </resources>
</build>
```

### 6. Exécution de l'assemblage

Dans le terminal, exécutez la commande suivante pour créer l'archive filtrée :

   ```
   mvn clean package assembly:single
   ```

### 7. Vérification

Dans le répertoire target, vous devriez voir une archive .zip nommée filtered-content.
Extrayez cette archive et vérifiez le contenu du fichier app.properties.
Les propriétés doivent être filtrées avec les valeurs correctes, par exemple `app.version` doit afficher la version de votre projet.


