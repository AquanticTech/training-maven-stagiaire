# Transformer un répertoire Markdown en site Maven

Pour transformer un répertoire contenant des fichiers markdown en un site Maven, suivez les étapes ci-dessous :

## 1. Ajouter le plugin Maven Site

Pour commencer, vous devez ajouter le plugin `maven-site-plugin` à votre `pom.xml`.

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-site-plugin</artifactId>
            <version>3.9.1</version>
        </plugin>
    </plugins>
</build>
```

## 2. Ajouter le plugin Markdown

Pour permettre à Maven de traiter les fichiers markdown, ajoutez le plugin `doxia-module-markdown` à la section `<dependencies>` de votre `pom.xml`.

```xml
<dependency>
    <groupId>org.apache.maven.doxia</groupId>
    <artifactId>doxia-module-markdown</artifactId>
    <version>1.9</version>
</dependency>
```

## 3. Configuration

Placez vos fichiers markdown dans le répertoire `src/site/markdown/`. Maven les traitera et générera un site web à partir de ces fichiers.

## 4. Générer le site

Exécutez la commande suivante pour générer le site :

```bash
mvn site
```

Après l'exécution de cette commande, vous trouverez le site généré dans le répertoire `target/site/`.

## 5. Visualiser le site

Ouvrez le fichier `target/site/index.html` dans votre navigateur pour visualiser le site généré.
