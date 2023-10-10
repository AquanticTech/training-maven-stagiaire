## Exercice : Création et personnalisation d'un site Maven

### Objectif :
Dans cet exercice, vous allez créer et personnaliser un site pour votre projet Maven. Un site Maven est un moyen de générer une documentation complète pour votre projet, y compris des rapports sur le code, la couverture des tests, les dépendances, et bien d'autres.

### Étapes :

1. **Initialisation du projet Maven** :
   Si vous n'avez pas déjà un projet Maven, créez-en un en utilisant l'archétype `maven-archetype-quickstart` :
   ```bash
   mvn archetype:generate -DgroupId=com.example -DartifactId=mywebsite -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

2. **Ajout du plugin `maven-site-plugin`** :
   Dans votre `pom.xml`, ajoutez le plugin `maven-site-plugin` dans la section `<build><plugins>` :
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-site-plugin</artifactId>
       <version>3.9.1</version>
   </plugin>
   ```

3. **Création de la structure du site** :
   Dans le répertoire principal de votre projet, créez un répertoire `src/site`. À l'intérieur, créez un autre répertoire `markdown` pour vos fichiers markdown.

4. **Rédaction de contenu** :
   Dans `src/site/markdown`, créez un fichier `index.md` et ajoutez du contenu, par exemple :
   ```markdown
   # Bienvenue sur mon site Maven

   Ceci est la page d'accueil de mon projet.
   ```

5. **Personnalisation du skin** :
   Pour personnaliser l'apparence de votre site, vous pouvez utiliser un skin différent. Par exemple, pour utiliser le skin `fluido`, ajoutez la dépendance suivante à votre `pom.xml` :
   ```xml
   <dependency>
       <groupId>org.apache.maven.skins</groupId>
       <artifactId>maven-fluido-skin</artifactId>
       <version>1.9.2</version>
   </dependency>
   ```
(!) (astuce ) il se peut que la version ne soit pas la bonne :-) à vous trouver l'erreur,
regardez par ici : https://mvnrepository.com/artifact/org.apache.maven.skins/maven-fluido-skin


   Et dans la section `<build><plugins>`, configurez le `maven-site-plugin` pour utiliser ce skin :
   ```xml
   <configuration>
       <skin>fluido</skin>
   </configuration>
   ```

6. **Génération du site** :
   Exécutez la commande suivante pour générer le site :
   ```bash
   mvn site
   ```

   Une fois la génération terminée, le site sera disponible dans le répertoire `target/site`.

7. **Visualisation du site** :
   Ouvrez le fichier `target/site/index.html` dans votre navigateur pour voir votre site Maven personnalisé.

### Conclusion :
À la fin de cet exercice, vous aurez créé un site Maven personnalisé pour votre projet, avec une apparence personnalisée et du contenu rédigé en markdown.
