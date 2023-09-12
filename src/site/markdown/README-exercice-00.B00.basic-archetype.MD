
# exercice-01 : HelloWorld basique avec 3 étapes 
- Générattion d'un projet à partir d'Archetype 
- Correction et débuggage 
- Mise en place de Build 

## 1/ Exercice d'utilisation de maven archetype

---

### step01 : Génération du projet
Maven permet de générer des projets à partir de template.

**Commande Maven :** `mvn archetype:generate`

- **`mvn`** : C'est l'outil de ligne de commande Maven. Il est utilisé pour exécuter diverses tâches Maven.
- **`archetype:generate`** : C'est une commande Maven qui permet de générer un nouveau projet Maven à partir d'un archétype (un modèle de projet).

---
**Paramètres :**

1. **`-DgroupId=com.example`**
    - **`groupId`** : Identifie de manière unique votre projet dans l'ensemble du système de construction. Il est souvent basé sur le nom de domaine inversé de votre organisation.
    - **`com.example`** : Dans cet exemple, le `groupId` est défini comme `com.example`.

2. **`-DartifactId=helloworld`**
    - **`artifactId`** : Nom du jar sans version. Il est utilisé pour nommer le jar construit (par exemple, `helloworld.jar`).
    - **`helloworld`** : Dans cet exemple, le `artifactId` est défini comme `helloworld`.

3. **`-DarchetypeArtifactId=maven-archetype-quickstart`**
    - **`archetypeArtifactId`** : Identifie le modèle de projet que vous souhaitez utiliser.
    - **`maven-archetype-quickstart`** : C'est un archétype de base fourni par Maven pour créer un simple projet Java.

4. **`-DinteractiveMode=false`**
    - **`interactiveMode`** : Détermine si l'utilisateur doit être interrogé pour des informations supplémentaires lors de la génération du projet.
    - **`false`** : Dans cet exemple, le mode interactif est désactivé, ce qui signifie que Maven ne posera pas de questions supplémentaires et utilisera les valeurs fournies.

---

**Résumé :**
La commande génère un nouveau projet Maven avec le `groupId` `com.example`, le `artifactId` `helloworld`, en utilisant l'archétype `maven-archetype-quickstart`, et le tout sans mode interactif.

---
### Step02 : Test  de compilation et génération Jar

Tester la commande suivante : 
`mvn clean package`

####  Vous obtenez une erreur, vous vous souvenez du problème de version de JDK ? 
Modifier votre *pom.xml* en ajoutant ceci :
```xml
   <properties>
       <maven.compiler.source>1.8</maven.compiler.source>
       <maven.compiler.target>1.8</maven.compiler.target>
   </properties>
```

#### Tentez une exécution 
`java -jar target/votrejar.jar`

Vous obtenez une erreur, `Problème de manifest, vous vous souvenez ?`

**Ajoutez ou modifiez la configuration du `maven-jar-plugin`** :
Dans votre `pom.xml`, assurez-vous d'avoir le plugin `maven-jar-plugin` configuré comme suit :

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
                           <addClasspath>true</addClasspath>
                           <classpathPrefix>lib/</classpathPrefix>
                           <mainClass>com.example.App</mainClass>
                       </manifest>
                   </archive>
               </configuration>
           </plugin>
       </plugins>
   </build>
   ```
Remarque : Remplacez `com.example.HelloWorld` par le nom complet de votre classe principale, y compris le nom du package.

2. **Reconstruisez le projet** :
   Après avoir ajouté ou modifié la configuration ci-dessus, reconstruisez votre projet avec la commande :

   ```bash
   mvn clean package
   ```

   Une fois la construction terminée, vous devriez pouvoir exécuter votre JAR sans rencontrer l'erreur `no main manifest attribute`.

----
### Step03 : Lancement du Jar 

ça y est vous avez votre super projet hellow world qui compile, en revanche, quand vous lancez le jar vous obtenez de la façon suivante :
`java -jar ./target/helloworlld-1.0-SNAPSHOT.jar`

Vous obtenez quelque chose comme :
`no main manifest attribute, in target/helloworld-1.0-SNAPSHOT.jar`

Mais d'où cela vient-il ? 

Cela vient du problème de manifest qui ne spécifie pas de classe principale car dans le pom.xml ce n'est pas spécifié.
Vous pouvez donc réaliser la modification suivante :
----
#### Step04 : Liste les archétypes Maven disponibles 

Pour générer une liste d'archetype et de modèle de projet, vous pouvez utilisez la commande 
`mvn archetype:generate -Dfilter=org.apache.maven.archetypes`

Cela va vous donner une liste de projets de départs 
```
1: remote -> org.apache.maven.archetypes:maven-archetype-archetype (An archetype which contains a sample archetype.)
2: remote -> org.apache.maven.archetypes:maven-archetype-j2ee-simple (An archetype which contains a simplified sample J2EE application.)
3: remote -> org.apache.maven.archetypes:maven-archetype-marmalade-mojo (-)
4: remote -> org.apache.maven.archetypes:maven-archetype-mojo (An archetype which contains a sample a sample Maven plugin.)
5: remote -> org.apache.maven.archetypes:maven-archetype-plugin (An archetype which contains a sample Maven plugin.)
6: remote -> org.apache.maven.archetypes:maven-archetype-plugin-site (An archetype which contains a sample Maven plugin site. This archetype can be layered upon an
    existing Maven plugin project.)
7: remote -> org.apache.maven.archetypes:maven-archetype-portlet (An archetype which contains a sample JSR-268 Portlet.)
8: remote -> org.apache.maven.archetypes:maven-archetype-profiles (-)
9: remote -> org.apache.maven.archetypes:maven-archetype-quickstart (An archetype which contains a sample Maven project.)
10: remote -> org.apache.maven.archetypes:maven-archetype-simple (An archetype which contains a simple Maven project.)
11: remote -> org.apache.maven.archetypes:maven-archetype-site (An archetype which contains a sample Maven site which demonstrates some of the supported document types like
    APT, XDoc, and FML and demonstrates how to i18n your site. This archetype can be layered
    upon an existing Maven project.)
12: remote -> org.apache.maven.archetypes:maven-archetype-site-simple (An archetype which contains a sample Maven site.)
13: remote -> org.apache.maven.archetypes:maven-archetype-site-skin (An archetype which contains a sample Maven Site Skin.)
14: remote -> org.apache.maven.archetypes:maven-archetype-webapp (An archetype which contains a sample Maven Webapp project.)
```

Vous pouvez encore avoir une liste plus complète avec uniquement la commande

`mvn archetype:generate`

Il y en a 3000 ..... donc vous avez largement le choix du modèle de projet que vous générez.


