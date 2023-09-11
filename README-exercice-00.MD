### Installation and Use of MAVEN

Maven is a powerful project management tool widely used in the Java ecosystem. It simplifies the build process, 
dependency management, and project documentation. To get started with Maven, one must first install / Setup Maven on their system. 
The installation process is straightforward, involving downloading the Maven binary, configuring environment variables, 
and verifying the installation. Once installed, developers can leverage Maven's robust features to streamline their development 
and Delivery workflow.

#### Installation Strategy 

We can adopt two differents strategy to use Maven :
- Install it on a Hosts with a specific OS version (Windows / MacOsx / Linux - Ubuntu , .... )
- Install it on a Guest  and use a VM tools ( VMWare / VirtualBox / Vagrant )
- Use container to build  ( Docker , redhat Container .... )
- Use a Wrapper that is included in Maven's basic and general project 


### Maven Installation Strategies Details 

#### 1. Install on a Host with a Specific OS Version (Windows / macOS / Linux - Ubuntu, etc.)
- **Description**: Traditional method of installing Maven directly on the host machine's OS.
- **Advantages**:
    - Direct access to Maven commands without intermediary layers.
    - Typically faster performance with no virtualization overhead.
- **Disadvantages**:
    - Potential conflicts with other software or system settings.
    - Limited to the host's OS; multiple OS testing requires multiple machines or dual-boot setups.

#### 2. Install on a Guest using VM Tools (VMWare / VirtualBox / Vagrant)
- **Description**: Maven is installed inside a virtual machine (VM) on a host system, providing an isolated environment.
- **Advantages**:
    - Test and build on multiple OS versions without multiple physical machines.
    - Isolation prevents system-wide issues and conflicts.
- **Disadvantages**:
    - Performance overhead due to virtualization.
    - More system resources (RAM, storage) needed for VMs.

#### 3. Use Container to Build (Docker, RedHat Container, etc.)
- **Description**: Containers package code and dependencies for quick, reliable runs across computing environments. Maven can run inside a container.
- **Advantages**:
    - Lightweight compared to VMs.
    - Consistent environments between development, testing, and production.
    - Easily shareable and version-controlled with tools like Docker Hub.
- **Disadvantages**:
    - Requires knowledge of containerization principles and tools.
    - Some advanced configurations might be more complex than direct OS installation.

#### 4. Use a Wrapper Included in Maven's Basic and General Project
- **Description**: Maven Wrapper is a shell script used to automatically download and install a specific Maven version, allowing users to build projects without having Maven installed and present on the path.
- **Advantages**:
    - Ensures everyone on a project uses the same Maven version.
    - Simplifies setup for new project contributors.
- **Disadvantages**:
    - An extra layer to manage, though lightweight.
    - Requires initial project setup with the Maven Wrapper.

**Conclusion of Installation Strategy**: The best Maven strategy largely depends on the project's specific requirements, the existing infrastructure,
and the team's familiarity with the mentioned tools. Each approach has its merits, and the choice should align with the broader
goals of the development workflow.

### Installing Maven on Windows

#### Prerequisites:
- **Java**: Ensure you have a JDK installed. Maven requires Java to run. Check by opening a command prompt and typing:
  ```
  java -version
  ```

#### Steps:

1. **Download Maven**:
  - Visit the official [Apache Maven website](https://maven.apache.org/download.cgi) to download the latest Maven zip file.

2. **Extract the Zip File**:
  - Extract the downloaded zip file to a directory of your choice, e.g., `C:\Program Files\Apache\Maven`.

3. **Set Environment Variables**:
  - **MAVEN_HOME**: Set this to the path where you extracted Maven, e.g., `C:\Program Files\Apache\Maven`.
  - **Path**: Append `%MAVEN_HOME%\bin` to your existing Path variable. This allows you to run the `mvn` command from any location in the command prompt.

4. **Verify Installation**:
  - Open a new command prompt and type:
    ```
    mvn -version
    ```
  - This should display the version of Maven you installed, confirming that the installation was successful.

**Note**: If you encounter any issues, ensure that your `JAVA_HOME` environment variable is set correctly and that Maven's bin directory is correctly added to the system's Path.
(Note: In the actual Markdown, you'll only need one backtick (`) for code blocks. I've used the escape sequence here to display it correctly for you.)

### Installing Maven on Linux - debian / ubuntu 

#### Prerequisites:
- **Java**: Ensure you have a JDK installed. Maven requires Java to run. Check by opening a terminal and typing:
  ```
  java -version
  ```

#### Steps:

1. **Update Package Repositories**:
  - Before installing Maven, it's a good practice to update the package repositories:
    ```
    sudo apt update
    ```

2. **Install Maven**:
  - Use the package manager to install Maven:
    ```
    sudo apt install maven
    ```

3. **Verify Installation**:
  - Check the installed version to ensure Maven was installed correctly:
    ```
    mvn -version
    ```
  - This should display the version of Maven you installed, confirming that the installation was successful.

4. **(Optional) Configure Environment Variables**:
  - If you need to set specific environment variables or configurations:
    - **MAVEN_HOME**: Set this to the path where Maven is installed, typically `/usr/share/maven`.
    - **Path**: Ensure that Maven's bin directory (`/usr/share/maven/bin`) is in the system's Path.

**Note**: The above steps use `apt`, which is the package manager for Debian-based distributions like Ubuntu. If you're using a different distribution like Fedora or CentOS, replace `apt` with the appropriate package manager, such as `yum` or `dnf`.

### Installing Maven on RedHat (RHEL-based distributions)

#### Prerequisites:
- **Java**: Ensure you have a JDK installed. Maven requires Java to run. Check by opening a terminal and typing:
  ```
  java -version
  ```

#### Steps:

1. **Update Package Repositories**:
  - Before installing Maven, it's a good practice to update the package repositories:
    ```
    sudo yum update
    ```

2. **Install Maven**:
  - Use the package manager to install Maven:
    ```
    sudo yum install maven
    ```

3. **Verify Installation**:
  - Check the installed version to ensure Maven was installed correctly:
    ```
    mvn -version
    ```
  - This should display the version of Maven you installed, confirming that the installation was successful.

4. **(Optional) Configure Environment Variables**:
  - If you need to set specific environment variables or configurations:
    - **MAVEN_HOME**: Set this to the path where Maven is installed. This can typically be `/usr/share/maven`.
    - **Path**: Ensure that Maven's bin directory (`/usr/share/maven/bin`) is in the system's Path.

**Note**: The steps provided use `yum`, which is the package manager for RedHat and other RHEL-based distributions. If you're using a newer version of RedHat or CentOS, you might be using `dnf` instead of `yum`. Adjust the commands accordingly.


### Installing Maven on macOS

#### Prerequisites:
- **Java**: Ensure you have a JDK installed. Maven requires Java to run. Check by opening a terminal and typing:
  ```
  java -version
  ```

#### Steps:

1. **Install Homebrew** (if not already installed):
  - Homebrew is a popular package manager for macOS. If you don't have it installed, you can set it up with:
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ``

2. **Install Maven using Homebrew**:
  - With Homebrew installed, you can easily install Maven:
    ```
    brew install maven
    ```

3. **Verify Installation**:
  - Check the installed version to ensure Maven was installed correctly:
    ```
    mvn -version
    ```
  - This should display the version of Maven you installed, confirming that the installation was successful.

**Note**: Using Homebrew simplifies the installation process for many packages on macOS, including Maven. If you prefer manual installation or using another method, you can download Maven directly from the official [Apache Maven website](https://maven.apache.org/download.cgi) and set up the environment variables accordingly.


### Installing Maven using a Maven Wrapper 

Le Maven Wrapper est un excellent outil pour garantir que tous les utilisateurs d'un projet utilisent la même version de Maven, sans nécessiter une installation globale de Maven. Voici comment procéder à son installation et à son utilisation :

#### Étape 1 : Naviguer vers le répertoire du projet

Ouvrez un terminal et naviguez vers le répertoire de votre projet :

```bash
cd /chemin/vers/votre/projet
```

#### Étape 2 : Générer le Maven Wrapper

Dans le terminal, exécutez la commande suivante pour générer le Maven Wrapper dans votre projet :

```bash
mvn wrapper:wrapper
```

#### Étape 3 : Utiliser Maven via le Wrapper

Une fois le wrapper généré, vous pouvez utiliser Maven via le wrapper avec les commandes suivantes :

- Pour les systèmes Unix/Linux/Mac :

```bash
./mvnw clean install
```

- Pour Windows :

```bash
mvnw.cmd clean install
```

> **Note** : La première fois que vous exécutez `./mvnw` (ou `mvnw.cmd` sur Windows), le wrapper téléchargera automatiquement la version appropriée de Maven pour votre projet et la stockera dans le répertoire `.m2/wrapper` de votre répertoire utilisateur.

### Utiliser Maven avec Docker

Utiliser Maven avec une image Docker est une pratique courante pour garantir que votre environnement de build est toujours cohérent, peu importe où vous exécutez votre build. Voici les étapes pour utiliser Maven avec une image Docker:

#### 1. Choisir une image Maven officielle de Docker Hub
- Rendez-vous sur [Docker Hub](https://hub.docker.com/) et recherchez l'image officielle de Maven. Vous pouvez choisir la version qui vous convient le mieux, par exemple `maven:3.6-jdk-11`.

#### 2. Écrire un Dockerfile
Créez un fichier nommé `Dockerfile` dans le répertoire racine de votre projet Maven. Voici un exemple de contenu pour ce fichier:

```Dockerfile
FROM maven:3.6-jdk-11
WORKDIR /app
COPY . /app
CMD ["mvn", "clean", "install"]
```

Ce Dockerfile utilise l'image Maven que vous avez choisie, définit un répertoire de travail, copie votre projet Maven dans l'image, et exécute la commande `mvn clean install` par défaut.

#### 3. Construire l'image Docker
Dans le répertoire racine de votre projet, exécutez la commande suivante pour construire votre image Docker:

```bash
docker build -t exercice-00.docker-maven .
```

Ceci construira une image Docker avec le tag ` exercice-00.docker-maven`.

#### 4. Exécuter Maven à l'intérieur d'un conteneur Docker
Pour exécuter Maven à l'intérieur d'un conteneur Docker, utilisez la commande suivante:

```bash
docker run --rm -v "$(pwd)":/app  exercice-00.docker-maven
```

Cette commande exécute la commande par défaut (`mvn clean install`) à l'intérieur d'un conteneur Docker. 

L'option `-v "$(pwd)":/app` monte votre répertoire de projet actuel dans le conteneur, ce qui permet à Maven d'accéder à votre code source.

#### 5. (Optionnel) Exécuter d'autres commandes Maven
Si vous souhaitez exécuter d'autres commandes Maven, vous pouvez le faire en ajoutant la commande à la fin de la commande `docker run`. Par exemple:

```bash
docker run --rm -v "$(pwd)":/app  exercice-00.docker-maven mvn test
```

Ceci exécutera la commande `mvn test` à l'intérieur du conteneur Docker.

#### 6. Nettoyage
Une fois que vous avez terminé, vous pouvez supprimer l'image Docker que vous avez créée pour libérer de l'espace:

```bash
docker rmi  exercice-00.docker-maven
```

En suivant ces étapes, vous pouvez facilement utiliser Maven à l'intérieur d'un conteneur Docker, garantissant ainsi que votre environnement de build est toujours cohérent.


