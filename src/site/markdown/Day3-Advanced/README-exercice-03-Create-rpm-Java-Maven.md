# Exercice : Création d'un package RPM à partir d'un code source Java avec Maven

## Objectif

Votre mission est de créer un package RPM pour une application Java simple utilisant Maven. Cette application affichera simplement "Bonjour, RPM !" lorsqu'elle sera exécutée.

## Instructions

0. **Lancer un conteneur en ligne de commande avec Centos:7**
  - Créer un fichier `Dockerfile` suivant :
```dockerfile
From centos:7
RUN curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | \
    JABBA_COMMAND="install 1.17.0 -o /jdk" bash
RUN echo "enabled=0" >> /etc/yum/pluginconf.d/subscription-manager.conf
RUN yum install -y rpm-build rpmdevtools maven
RUN rpmdev-setuptree
CMD ["/bin/bash"]
```
  - Construire l'image docker avec la commande suivante :
```bash
    docker build -t rhel7-rpm .
```

  - Lancer l'image docker avec la commande suivante :
```bash
    docker run -it --name rhel7-rpm -v /home/$(whoami)/rpmbuild:/root/rpmbuild rhel7-rpm 
 ```


1. **Préparation de l'environnement si une machine virtuelle** :
   - Installez les outils nécessaires pour la création de packages RPM et Maven. Sur une distribution basée sur Red Hat, vous pouvez utiliser les commandes suivantes :
     ```
     sudo yum install rpm-build rpmdevtools maven
     ```

2. **Configuration de l'environnement de construction RPM** :
   - Exécutez la commande suivante pour créer l'arborescence nécessaire :
     ```
     rpmdev-setuptree
     ```

3. **Création du projet Maven** :
   - Utilisez la commande suivante pour générer un squelette de projet Maven :
     ```
     mvn archetype:generate -DgroupId=com.example -DartifactId=hello-rpm -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
     ```
   - Accédez au répertoire `hello-rpm` et remplacez le contenu du fichier `App.java` par :
     ```java
     public class App {
         public static void main(String[] args) {
             System.out.println("Bonjour, RPM !");
         }
     }
     ```
     
  - Attention, souvenez-vous qu'il faut modifier le fichier pom.xml et ajouter le plugin de génération du jar de la façon suivante : 
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
                                <mainClass>com.votrepackage.VotreClassePrincipale</mainClass>
                            </manifest>
                        </archive>
                    </configuration>
                </plugin>
            </plugins>
        </build>
  ```
 
   - Compilez et packagez l'application avec Maven :
     ```
     mvn clean package
     ```

4. **Création du fichier SPEC** :
   - Dans le répertoire `~/rpmbuild/SPECS`, créez un fichier nommé `hello-rpm.spec` avec le contenu suivant :
     ```spec
     Name: hello-rpm
     Version: 1.0
     Release: 1%{?dist}
     Summary: Une application Java simple pour dire bonjour avec Maven

     License: GPLv3+
     URL: http://example.com/hello-rpm
     Source0:  hello-rpm-1.0-SNAPSHOT.jar

     %description
     Une application Java simple qui affiche "Bonjour, RPM !" et est packagée avec Maven.

     %install
     mkdir -p %{buildroot}/opt/hello-rpm
     cp %{SOURCE0} %{buildroot}/opt/hello-rpm

     %files
     /opt/hello-rpm/hello-rpm-1.0-SNAPSHOT.jar


     %post
     echo "Merci d'avoir installé hello-rpm !"

     %changelog
     # let's skip this for now lol

     ```

5. **Création du package RPM** :
   - Placez le fichier `hello-rpm-1.0.jar` (généré dans le répertoire `target` de votre projet Maven) dans le répertoire `~/rpmbuild/SOURCES`.
   - Dans le répertoire `~/rpmbuild/SPECS`, exécutez la commande suivante pour créer le package RPM :
     ```
     rpmbuild -ba hello-rpm.spec
     ```

6. **Vérification** :
   - Vous devriez trouver votre package RPM dans le répertoire `~/rpmbuild/RPMS`.

## Question bonus

Comment pourriez-vous inclure des dépendances externes dans votre projet Maven et vous assurer qu'elles sont également packagées dans le RPM ?

---

# Réponse

Vous avez déjà la réponse détaillée dans les instructions ci-dessus. Pour la question bonus, voici une réponse possible :

Pour inclure des dépendances externes dans votre projet Maven, vous pouvez les ajouter dans la section `<dependencies>` du fichier `pom.xml` de votre projet. Maven téléchargera et utilisera ces dépendances lors de la compilation. Pour vous assurer qu'elles sont également packagées dans le RPM, vous pouvez utiliser le plugin `maven-assembly-plugin` pour créer un JAR "fat" (un JAR qui inclut toutes les dépendances). Ensuite, vous pouvez ajuster le fichier SPEC pour inclure ce JAR "fat" dans le package RPM.
