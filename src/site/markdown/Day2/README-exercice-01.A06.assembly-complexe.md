# Exercice : Recréation d'une arborescence de ressources complexe avec le plugin `assembly` de Maven

## Objectif

Créer un projet Maven et utiliser le plugin `assembly` pour recréer une arborescence de ressources complexe dans une archive de sortie.

## Étapes

### 1. Initialisation du projet

- Créez un nouveau projet Maven en utilisant l'archétype `maven-archetype-quickstart`.
- Naviguez vers le répertoire du projet et ouvrez le fichier `pom.xml`.

### 2. Configuration du plugin `maven-assembly-plugin`

- Ajoutez la configuration suivante pour le plugin `maven-assembly-plugin` dans le fichier `pom.xml` :

```xml

<build>
    <plugins>
        <plugin>
            <artifactId>maven-assembly-plugin</artifactId>
            <version>3.3.0</version>
            <configuration>
                <descriptors>
                    <descriptor>src/main/assembly/complex-structure.xml</descriptor>
                </descriptors>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 3. Création de l'arborescence de ressources complexe

Dans le répertoire src/main/resources, créez l'arborescence suivante :

   ```
   ├── config
   │   ├── dev
   │   │   └── application-dev.properties
   │   └── prod
   │       └── application-prod.properties
   ├── data
   │   └── sample-data.csv
   └── templates
   └── email-template.html
```

### 4. Configuration du fichier assembly.xml

- Dans le répertoire src/main/assembly, créez un fichier nommé complex-structure.xml.
- Ajoutez la configuration suivante pour recréer l'arborescence de ressources :

```xml
<assembly>
    <id>complex-structure</id>
    <formats>
        <format>zip</format>
    </formats>
    <fileSets>
        <fileSet>
            <directory>src/main/resources/config</directory>
            <outputDirectory>/config</outputDirectory>
        </fileSet>
        <fileSet>
            <directory>src/main/resources/data</directory>
            <outputDirectory>/data</outputDirectory>
        </fileSet>
        <fileSet>
            <directory>src/main/resources/templates</directory>
            <outputDirectory>/templates</outputDirectory>
        </fileSet>
    </fileSets>
</assembly>
```   

### 5. Exécution de l'assemblage

Dans le terminal, exécutez la commande suivante pour créer l'archive avec l'arborescence complexe :

   ```
   mvn clean package assembly:single 
   ```

### 6. Vérification

Dans le répertoire target, vous devriez voir une archive .zip nommée complex-structure.
Extrayez cette archive et vérifiez que l'arborescence de ressources complexe a été correctement recréée.

