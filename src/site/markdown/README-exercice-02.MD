### Exercice 02 

####  🚎 Objectifs

L'objectif est d'utiliser les archetypes de Maven pour explorer les possibilités offertes par Maven.
Nous partons ici de l'archetype  :

⦿ **org.apache.maven.archetypes:maven-archetype-j2ee-simple**

==> An archetype which contains a simplified sample J2EE application.*

#### Step01 : Generate the Archetype Skeleton 

Pour générer le squelette de l'archetype nous saissons : 
`mvn archetype:generate -Dfilter=org.apache.maven.archetypes:`

Puis nous suivions le menu 

#### Step02 : Arrêtons-nous un instant sur ce qui a été généré 

##### Description du contenu de ce qui a été généré

1. **ear** :
   - **Type** : Module EAR (Enterprise Archive)
   - **Description** : 
     - Contient l'artefact EAR final qui regroupe tous les autres modules (EJBs, WARs, etc.). 
     - L'EAR est utilisé pour déployer l'application sur un serveur d'applications J2EE.

2. **ejbs** :
   - **Type** : Module EJB (Enterprise JavaBeans)
   - **Description** : 
     - Contient les beans d'entreprise (EJBs) qui définissent la logique métier de l'application.

3. **primary-source** :
   - **Type** : Module Java
   - **Description** : 
     - Il s'agit probablement d'un module de base ou d'une bibliothèque contenant des classes Java communes ou des sources principales utilisées dans l'application.

4. **projects** :
   - **Type** : Conteneur de modules
   - **Description** : 
     - Un répertoire contenant d'autres sous-modules. Dans votre arborescence, il contient un module `logging`.

     - **logging** :
       - **Type** : Module Java
       - **Description** : Contient les classes et les utilitaires liés à la journalisation.

5. **servlets** :
   - **Type** : Conteneur de modules
   - **Description** : 
     - Un répertoire contenant des sous-modules liés aux servlets.

   - **servlet** :
     - **Type** : Module WAR (Web Application Archive)
     - **Description** : Contient l'application web, y compris les servlets, les JSPs, et d'autres ressources web. `
     - Le WAR est utilisé pour déployer l'application web sur un serveur.

🎁 Chaque **module** contient généralement les répertoires suivants :
- 🧰 **src/main/java** : Contient le code source Java.
- 🧰 **src/test/java** : Contient les tests unitaires.
- 🧰 **target** : Contient les artefacts générés, comme les JARs, WARs, EARs, et d'autres fichiers générés pendant le cycle de vie de la construction Maven.
- 🧰 **pom.xml** : Le fichier POM (Project Object Model) de Maven qui définit le module, ses dépendances, plugins, et d'autres configurations.

L'arborescence générée est typique d'une application J2EE multi-modules avec Maven. 
Chaque module a un objectif spécifique et peut être construit et déployé indépendamment, mais ils sont tous regroupés sous un projet parent pour faciliter la gestion et la construction.






