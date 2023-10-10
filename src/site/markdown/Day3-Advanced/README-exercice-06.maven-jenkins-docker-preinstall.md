## Prérequis pour lancer Jenkins sur Docker

### Prérequis :

1. **Docker** :
    - Assurez-vous d'avoir Docker installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis [le site officiel de Docker](https://www.docker.com/get-started).

2. **Espace disque** :
    - Jenkins stocke toutes ses données dans un volume Docker. Assurez-vous d'avoir suffisamment d'espace disque pour stocker vos jobs, configurations, et builds.

3. **Port 8080 libre** :
    - Par défaut, Jenkins s'exécute sur le port 8080. Assurez-vous que ce port est libre sur votre machine ou soyez prêt à le mapper sur un autre port lors du lancement du conteneur.

### Étapes pour lancer Jenkins sur Docker :

1. **Télécharger l'image Docker de Jenkins** :
   ```bash
   docker pull jenkins/jenkins:lts
   ```

2. **Lancer un conteneur Jenkins** :
   ```bash
   docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts
   ```

    - `-p 8080:8080` : mappe le port 8080 du conteneur au port 8080 de l'hôte.
    - `-p 50000:50000` : mappe le port 50000, utilisé pour la communication maître-agent.
    - `-v jenkins_home:/var/jenkins_home` : persiste les données de Jenkins en les stockant dans un volume Docker.

3. **Accéder à Jenkins** :
    - Ouvrez un navigateur et accédez à `http://localhost:8080`.
    - Lors du premier lancement, Jenkins vous demandera le mot de passe administrateur initial. Vous pouvez le récupérer en exécutant la commande suivante :
      ```bash
      docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
      ```

4. **Configuration initiale** :
    - Suivez les étapes de l'assistant de configuration pour installer les plugins recommandés et configurer un utilisateur administrateur.

### Conclusion :
Une fois ces étapes terminées, vous devriez avoir une instance de Jenkins en cours d'exécution sur Docker, prête à être utilisée pour vos projets d'intégration continue.
