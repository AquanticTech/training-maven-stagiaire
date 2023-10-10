# Exercice Maven : Construire un Assembly avec le plugin `maven-assembly-plugin`

## Objectif
L'objectif de cet exercice est de vous familiariser avec la création d'un assembly dans Maven en utilisant le plugin `maven-assembly-plugin` et d'intégrer des fichiers ressources.

## Prérequis
- Avoir Maven installé sur votre machine.

## Étapes

### 1. Création du projet parent

1. Ouvrez un terminal et naviguez vers le répertoire de votre choix.
2. Créez un nouveau projet Maven avec le packaging `pom` :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=assembly-project -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false -Dpackaging=pom
   ```

### 2. Ajout de modules

Ajoutez deux modules : un module `moduleA` et un module `moduleB`.

1. Naviguez vers le répertoire du projet parent `assembly-project`.
2. Créez le module `moduleA` :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=moduleA -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```
3. Créez le module `moduleB` :
   ```bash
   mvn archetype:generate -DgroupId=com.formation -DartifactId=moduleB -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

### 3. Ajout de fichiers ressources

1. Dans le répertoire `assembly-project`, créez un dossier `resources`.
2. Ajoutez quelques fichiers de ressources (par exemple, `config.properties`, `application.yml`, etc.) dans ce dossier.

### 4. Configuration du plugin `maven-assembly-plugin`

Dans le fichier `pom.xml` du projet parent, ajoutez la configuration suivante pour le plugin `maven-assembly-plugin` :

```xml
<build>
    <plugins>
        <plugin>
            <artifactId>maven-assembly-plugin</artifactId>
            <version>3.3.0</version>
            <configuration>
                <descriptors>
                    <descriptor>src/main/assembly/assembly.xml</descriptor>
                </descriptors>
            </configuration>
            <executions>
                <execution>
                    <id>make-assembly</id>
                    <phase>package</phase>
                    <goals>
                        <goal>single</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### 5. Mise à jour du descripteur d'assembly

Dans le répertoire `src/main/assembly`, mettez à jour le fichier `assembly.xml` pour inclure les fichiers de ressources :

```xml
<assembly xmlns="http://maven.apache.org/ASSEMBLY/2.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/ASSEMBLY/2.1.0 http://maven.apache.org/xsd/assembly-2.1.0.xsd">
    <id>assembly-id</id>
    <formats>
        <format>zip</format>
    </formats>
    <includeBaseDirectory>false</includeBaseDirectory>
    <moduleSets>
        <moduleSet>
            <includes>
                <include>com.formation:moduleA</include>
                <include>com.formation:moduleB</include>
            </includes>
            <binaries>
                <outputDirectory>modules</outputDirectory>
                <unpack>false</unpack>
            </binaries>
        </moduleSet>
    </moduleSets>
    <fileSets>
        <fileSet>
            <directory>${project.basedir}/resources</directory>
            <outputDirectory>/resources</outputDirectory>
            <includes>
                <include>*.*</include>
            </includes>
        </fileSet>
    </fileSets>
</assembly>
```

### 6. Construction de l'assembly

1. Dans le terminal, naviguez vers le répertoire du projet parent `assembly-project`.
2. Exécutez la commande suivante pour construire l'assembly :
   ```bash
   mvn clean package
   ```

Après avoir exécuté cette commande, vous devriez trouver un fichier `.zip` dans le répertoire `target` du projet parent. Ce fichier `.zip` est l'assembly qui contient les modules `moduleA` et `moduleB`, ainsi que les fichiers de ressources.

Félicitations ! Vous avez réussi à construire un assembly en composant différentes ressources avec Maven en utilisant le plugin `maven-assembly-plugin`.
