## Exercice : Installation de Nexus et déploiement d'un RPM avec Docker

### Objectif :
Dans cet exercice, vous allez installer Nexus OSS (Sonatype Nexus Repository Manager) sur Docker et déployer un paquet RPM dans votre dépôt Nexus.

### Prérequis :

1. **Docker** :
   - Assurez-vous d'avoir Docker installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis [le site officiel de Docker](https://www.docker.com/get-started).

2. **Espace disque** :
   - Nexus stockera tous ses dépôts et données dans un volume Docker. Assurez-vous d'avoir suffisamment d'espace disque.

3. **Port 8081 libre** :
   - Par défaut, Nexus s'exécute sur le port 8081. Assurez-vous que ce port est libre sur votre machine ou soyez prêt à le mapper sur un autre port lors du lancement du conteneur.

### Étapes :

1. **Télécharger l'image Docker de Nexus** :
   ```bash
   docker pull sonatype/nexus3
   ```

2. **Lancer un conteneur Nexus** :
   ```bash
   docker run -d -p 8081:8081 --name nexus -v nexus_data:/nexus-data sonatype/nexus3
   ```

   - `-p 8081:8081` : mappe le port 8081 du conteneur au port 8081 de l'hôte.
   - `-v nexus_data:/nexus-data` : persiste les données de Nexus en les stockant dans un volume Docker.

3. **Accéder à Nexus** :
   - Ouvrez un navigateur et accédez à `http://localhost:8081`.
   - Connectez-vous avec les identifiants par défaut : `admin` / `admin123`.

4. **Configurer un dépôt YUM (pour RPM)** :
   - Dans l'interface de Nexus, allez dans "Server administration and configuration" > "Repositories" > "Create repository".
   - Sélectionnez "yum (hosted)" et donnez-lui un nom, par exemple "my-rpm-repo".

5. **Déployer un RPM** :
   - Vous pouvez utiliser l'outil `curl` pour déployer votre RPM dans le dépôt Nexus :
     ```bash
     curl -u admin:admin123 --upload-file your-package.rpm http://localhost:8081/repository/my-rpm-repo/
     ```

### Conclusion :
À la fin de cet exercice, vous aurez installé Nexus sur Docker, configuré un dépôt YUM pour les paquets RPM et déployé un paquet RPM dans ce dépôt.
