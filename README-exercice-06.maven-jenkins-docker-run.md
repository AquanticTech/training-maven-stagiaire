## Exercice : Intégration de Maven, Jenkins et Docker

### Objectif :
Dans cet exercice, vous allez configurer un pipeline d'intégration continue avec Jenkins qui construit un projet Maven et le déploie dans un conteneur Docker.

### Prérequis :
- Avoir Docker installé.
- Avoir Jenkins installé avec le plugin Docker.
- Avoir un projet Maven prêt à être construit.

### Étapes :

1. **Préparation du Dockerfile** :
   Dans le répertoire racine de votre projet Maven, créez un `Dockerfile` pour définir comment votre application sera exécutée dans un conteneur Docker.

   ```Dockerfile
   FROM openjdk:11-jre-slim
   COPY target/my-app-1.0-SNAPSHOT.jar /usr/app/my-app.jar
   CMD ["java", "-jar", "/usr/app/my-app.jar"]
   ```

2. **Configuration de Jenkins** :
    - Lancez Jenkins et connectez-vous.
    - Créez un nouvel "Item" de type "Pipeline".
    - Dans la section "Pipeline", choisissez "Pipeline script from SCM" et sélectionnez "Git". Entrez l'URL de votre dépôt Git contenant le projet Maven.
    - Dans le script de pipeline, ajoutez les étapes suivantes :

   ```groovy
   pipeline {
       agent any

       stages {
           stage('Build') {
               steps {
                   sh 'mvn clean install'
               }
           }
           stage('Docker Build') {
               steps {
                   script {
                       docker.build("my-app:latest")
                   }
               }
           }
           stage('Docker Run') {
               steps {
                   script {
                       docker.image("my-app:latest").run("-p 8080:8080")
                   }
               }
           }
       }
   }
   ```

3. **Exécution du Pipeline** :
    - Exécutez le pipeline Jenkins que vous venez de configurer.
    - Jenkins clonera votre dépôt, exécutera le build Maven, construira une image Docker avec le JAR généré et exécutera cette image.

4. **Vérification** :
    - Une fois le pipeline terminé, accédez à `http://localhost:8080` dans votre navigateur. Vous devriez voir votre application en cours d'exécution depuis un conteneur Docker.

### Conclusion :
À la fin de cet exercice, vous aurez configuré un pipeline d'intégration continue qui utilise Maven pour construire votre application, Docker pour la conteneuriser, et Jenkins pour automatiser le processus.
