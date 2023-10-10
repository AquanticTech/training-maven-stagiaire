### Commandes Maven pour lister les goals et les cycles de vie

Pour Maven, la commande qui permet de lister les goals et les cycles de vie est :

```bash
mvn help:describe -Dcmd=compile
```

Cette commande affiche les informations sur le goal "compile". Si vous souhaitez obtenir des informations sur un autre goal ou phase, remplacez "compile" par le nom de la phase ou du goal souhaité.

Si vous voulez voir tous les goals d'un plugin spécifique, vous pouvez utiliser :

```bash
mvn help:describe -Dplugin=[nomDuPlugin]
```

Remplacez `[nomDuPlugin]` par le nom du plugin pour lequel vous souhaitez voir les goals. Par exemple, pour le plugin `maven-compiler-plugin`, la commande serait :

```bash
mvn help:describe -Dplugin=maven-compiler-plugin
```

### Cheatsheet de commandes classique Maven avec les plugins associés 

L'objectif de la liste ci-dessous est d'être le plus exhaustif possilbe afin que cette liste puisse service de référentiel maven aux stagiaires.


1. `mvn clean` : Nettoie le répertoire `target`, supprimant les fichiers et dossiers générés précédemment.
2. `mvn validate` : Valide que le projet est correct et que toutes les informations nécessaires sont disponibles.
3. `mvn compile` : Compile les sources du projet.
4. `mvn test` : Exécute les tests unitaires en utilisant un framework de test approprié.
5. `mvn package` : Emballe le code compilé dans un format distribuable, comme un JAR.
6. `mvn verify` : Effectue des vérifications pour s'assurer que le package est valide et répond à des critères de qualité.
7. `mvn install` : Installe le package dans le dépôt local Maven, pour une utilisation en tant que dépendance dans d'autres projets localement.
8. `mvn deploy` : Copie le package final dans un dépôt Maven distant pour le partager avec d'autres développeurs et projets.
9. `mvn site` : Génère la documentation du site pour le projet.
10. `mvn site:deploy` : Déploie la documentation générée sur un serveur spécifique.
11. `mvn integration-test` : Exécute les tests d'intégration sur le code.
12. `mvn site:stage` : Prépare le site pour le déploiement en staging.
13. `mvn help:describe` : Affiche des informations détaillées sur les éléments de configuration du projet.
14. `mvn dependency:tree` : Affiche l'arbre des dépendances du projet.
15. `mvn dependency:list` : Liste toutes les dépendances utilisées dans le projet.
16. `mvn dependency:analyze` : Analyse les dépendances du projet et rapporte celles qui sont inutilisées ou déclarées mais non utilisées.
17. `mvn dependency:purge-local-repository` : Supprime les dépendances du projet du dépôt local et les re-télécharge.
18. `mvn dependency:copy` : Copie une dépendance spécifique dans un emplacement spécifié.
19. `mvn archetype:generate` : Génère un nouveau projet à partir d'un archetype.
20. `mvn release:prepare` : Prépare le projet pour une release.
21. `mvn release:perform` : Effectue la release après sa préparation.
22. `mvn release:clean` : Nettoie les fichiers générés lors de la préparation de la release.
23. `mvn repository:purge` : Purge le dépôt local de certains artefacts.
24. `mvn javadoc:javadoc` : Génère la documentation Javadoc du code source.
25. `mvn javadoc:test-javadoc` : Génère la documentation Javadoc pour le code de test.
26. `mvn eclipse:eclipse` : Génère les fichiers nécessaires pour importer le projet dans Eclipse.
27. `mvn eclipse:clean` : Supprime les fichiers générés pour Eclipse.
28. `mvn idea:idea` : Génère les fichiers nécessaires pour importer le projet dans IntelliJ IDEA.
29. `mvn idea:clean` : Supprime les fichiers générés pour IntelliJ IDEA.
30. `mvn enforcer:enforce` : Exécute les règles d'application définies.
31. `mvn enforcer:display-info` : Affiche les informations système et les propriétés du projet.
32. `mvn versions:set` : Modifie les versions des artefacts.
33. `mvn versions:commit` : Confirme les modifications de version.
34. `mvn versions:revert` : Rétablit les versions d'origine.
35. `mvn versions:display-dependency-updates` : Affiche les mises à jour de dépendance disponibles.
36. `mvn versions:display-plugin-updates` : Affiche les mises à jour de plugin disponibles.
37. `mvn versions:lock-snapshots` : Verrouille les snapshots à une version spécifique.
38. `mvn versions:unlock-snapshots` : Déverrouille les snapshots.
39. `mvn versions:use-latest-releases` : Modifie le POM pour utiliser les dernières versions des dépendances.
40. `mvn versions:use-latest-snapshots` : Modifie le POM pour utiliser les derniers snapshots des dépendances.
41. `mvn versions:use-latest-versions` : Modifie le POM pour utiliser les dernières versions (release ou snapshot) des dépendances.
42. `mvn versions:use-next-releases` : Modifie le POM pour utiliser la prochaine version release des dépendances.
43. `mvn versions:use-next-snapshots` : Modifie le POM pour utiliser la prochaine version snapshot des dépendances.
44. `mvn versions:use-next-versions` : Modifie le POM pour utiliser la prochaine version (release ou snapshot) des dépendances.
45. `mvn versions:use-releases` : Modifie le POM pour utiliser la version release des dépendances si elle est disponible.
46. `mvn versions:use-latest-versions` : Modifie le POM pour utiliser la dernière version des dépendances.
47. `mvn versions:resolve-ranges` : Résout les plages de versions dans les dépendances.
48. `mvn versions:set-property` : Définit une propriété à la dernière version.
49. `mvn scm:checkout` : Effectue un checkout à partir du système de contrôle de version.
50. `mvn scm:update` : Met à jour les sources à partir du système de contrôle de version.
51. `mvn scm:checkin` : Effectue un checkin dans le système de contrôle de version.
52. `mvn scm:add` : Ajoute des fichiers au système de contrôle de version.
53. `mvn scm:status` : Affiche le statut du système de contrôle de version.
54. `mvn scm:tag` : Crée une étiquette dans le système de contrôle de version.
55. `mvn scm:branch` : Crée une branche dans le système de contrôle de version.
56. `mvn scm:diff` : Affiche les différences dans le système de contrôle de version.
57. `mvn scm:export` : Exporte les sources à partir du système de contrôle de version.
58. `mvn scm:bootstrap` : Crée un nouveau projet à partir du système de contrôle de version.
59. `mvn scm:changelog` : Génère un journal des modifications à partir du système de contrôle de version.
60. `mvn scm:edit` : Active l'édition de fichiers dans le système de contrôle de version.
61. `mvn scm:unedit` : Désactive l'édition de fichiers dans le système de contrôle de version.
62. `mvn scm:validate` : Valide que le projet est dans le système de contrôle de version.
63. `mvn formatter:format` : Formate le code source en utilisant un format spécifié.
64. `mvn formatter:validate` : Valide que le code source est correctement formaté.
65. `mvn jetty:run` : Exécute l'application dans le serveur Jetty.
66. `mvn jetty:run-war` : Exécute l'application WAR dans le serveur Jetty.
67. `mvn jetty:deploy-war` : Déploie l'application WAR dans le serveur Jetty.
68. `mvn jetty:stop` : Arrête le serveur Jetty.
69. `mvn tomcat7:run` : Exécute l'application dans le serveur Tomcat 7.
70. `mvn tomcat7:run-war` : Exécute l'application WAR dans le serveur Tomcat 7.
71. `mvn tomcat7:deploy` : Déploie l'application dans le serveur Tomcat 7.
72. `mvn tomcat7:undeploy` : Retire l'application du serveur Tomcat 7.
73. `mvn tomcat7:redeploy` : Redéploie l'application dans le serveur Tomcat 7.
74. `mvn tomcat7:start` : Démarre le serveur Tomcat 7.
75. `mvn tomcat7:stop` : Arrête le serveur Tomcat 7.
76. `mvn findbugs:findbugs` : Analyse le code source avec FindBugs.
77. `mvn findbugs:check` : Vérifie si des erreurs ont été détectées par FindBugs.
78. `mvn findbugs:gui` : Affiche l'interface graphique de FindBugs.
79. `mvn pmd:pmd` : Analyse le code source avec PMD.
80. `mvn pmd:check` : Vérifie si des erreurs ont été détectées par PMD.
81. `mvn pmd:cpd` : Détecte le code dupliqué avec PMD.
82. `mvn checkstyle:checkstyle` : Analyse le code source avec Checkstyle.
83. `mvn checkstyle:check` : Vérifie si des erreurs ont été détectées par Checkstyle.
84. `mvn jxr:jxr` : Génère des rapports de code source croisé.
85. `mvn cobertura:cobertura` : Génère des rapports de couverture de code avec Cobertura.
86. `mvn sonar:sonar` : Analyse le projet avec SonarQube.
87. `mvn liquibase:update` : Met à jour la base de données en utilisant Liquibase.
88. `mvn liquibase:rollback` : Annule les changements dans la base de données en utilisant Liquibase.
89. `mvn liquibase:status` : Affiche le statut des changements de base de données avec Liquibase.
90. `mvn liquibase:tag` : Étiquette la base de données avec Liquibase.
91. `mvn liquibase:diff` : Affiche les différences entre la base de données et le modèle avec Liquibase.
92. `mvn exec:java` : Exécute une classe Java avec le plugin exec.
93. `mvn exec:exec` : Exécute un processus externe avec le plugin exec.
94. `mvn antrun:run` : Exécute des tâches Ant avec le plugin antrun.
95. `mvn assembly:assembly` : Crée une archive avec le plugin assembly.
96. `mvn assembly:single` : Crée une archive unique avec le plugin assembly.
97. `mvn failsafe:integration-test` : Exécute les tests d'intégration avec le plugin failsafe.
98. `mvn failsafe:verify` : Vérifie les résultats des tests d'intégration avec le plugin failsafe.
99. `mvn gpg:sign` : Signe les artefacts avec GPG.
100. `mvn gpg:sign-and-deploy-file` : Signe et déploie un fichier avec GPG.
101. `mvn archetype:create` : Crée un nouveau projet à partir d'un archetype.
102. `mvn archetype:generate` : Génère un nouveau projet à partir d'un archetype interactif.
103. `mvn archetype:crawl` : Met à jour le catalogue d'archetypes.
104. `mvn build-helper:add-source` : Ajoute un répertoire source supplémentaire.
105. `mvn build-helper:add-resource` : Ajoute un répertoire de ressources supplémentaire.
106. `mvn build-helper:add-test-source` : Ajoute un répertoire source de test supplémentaire.
107. `mvn build-helper:add-test-resource` : Ajoute un répertoire de ressources de test supplémentaire.
108. `mvn build-helper:parse-version` : Analyse la version du projet.
109. `mvn build-helper:attach-artifact` : Attache un artefact supplémentaire au projet.
110. `mvn build-helper:remove-project-artifact` : Supprime l'artefact du projet du dépôt local.
111. `mvn build-helper:maven-version` : Affiche la version de Maven.
112. `mvn build-helper:regex-properties` : Définit des propriétés basées sur des expressions régulières.
113. `mvn build-helper:regex-filter` : Filtre les ressources en utilisant des expressions régulières.
114. `mvn build-helper:released-version` : Récupère la dernière version publiée d'un artefact.
115. `mvn build-helper:reserve-network-port` : Réserve un port réseau pour éviter les conflits pendant les tests.
116. `mvn build-helper:timestamp-property` : Définit une propriété avec le timestamp actuel.
117. `mvn build-helper:parse-version` : Analyse et décompose la version du projet en propriétés.
118. `mvn cargo:run` : Exécute l'application dans un conteneur avec le plugin Cargo.
119. `mvn cargo:start` : Démarre un conteneur avec le plugin Cargo.
120. `mvn cargo:stop` : Arrête un conteneur avec le plugin Cargo.
121. `mvn cargo:deploy` : Déploie un artefact dans un conteneur avec le plugin Cargo.
122. `mvn cargo:undeploy` : Retire un artefact d'un conteneur avec le plugin Cargo.
123. `mvn cargo:redeploy` : Redéploie un artefact dans un conteneur avec le plugin Cargo.
124. `mvn cargo:daemon` : Exécute le conteneur en mode daemon avec le plugin Cargo.
125. `mvn changelog:changelog` : Génère un journal des modifications à partir du système de contrôle de version.
126. `mvn changes:announcement-generate` : Génère une annonce de release.
127. `mvn changes:changes-report` : Génère un rapport des changements.
128. `mvn changes:jira-report` : Génère un rapport à partir des tickets JIRA.
129. `mvn changes:announcement-mail` : Envoie une annonce de release par e-mail.
130. `mvn changes:github-report` : Génère un rapport à partir des tickets GitHub.
131. `mvn clover:setup` : Prépare le projet pour Clover (outil de couverture de code).
132. `mvn clover:aggregate` : Agrège les données de couverture de plusieurs modules.
133. `mvn clover:clover` : Génère le rapport Clover.
134. `mvn clover:check` : Vérifie les seuils de couverture.
135. `mvn clover:instrument` : Instrumente le code pour la collecte de données de couverture.
136. `mvn clover:clean` : Supprime les données instrumentées.
137. `mvn dashboard:dashboard` : Génère un tableau de bord du projet.
138. `mvn dbunit:export` : Exporte les données de la base de données avec DBUnit.
139. `mvn dbunit:import` : Importe les données dans la base de données avec DBUnit.
140. `mvn dbunit:operation` : Exécute une opération DBUnit sur la base de données.
141. `mvn dependency:analyze-dep-mgt` : Analyse et vérifie la gestion des dépendances.
142. `mvn dependency:analyze-only` : Analyse les dépendances sans vérification.
143. `mvn dependency:analyze-report` : Génère un rapport d'analyse des dépendances.
144. `mvn dependency:build-classpath` : Génère un classpath à partir des dépendances.
145. `mvn dependency:copy-dependencies` : Copie les dépendances dans un emplacement spécifié.
146. `mvn dependency:get` : Télécharge un artefact du dépôt.
147. `mvn dependency:go-offline` : Télécharge toutes les dépendances pour travailler hors ligne.
148. `mvn dependency:list-repositories` : Liste les dépôts utilisés pour résoudre les dépendances.
149. `mvn dependency:properties` : Définit des propriétés pour chaque dépendance.
150. `mvn dependency:resolve-plugins` : Résout les plugins et leurs dépendances.
151. `mvn dependency:sources` : Télécharge les sources des dépendances.
152. `mvn dependency:tree-descriptor` : Génère un descripteur de l'arbre des dépendances.
153. `mvn doap:generate` : Génère une description du projet au format DOAP.
154. `mvn docck:check` : Vérifie la documentation du plugin.
155. `mvn ear:ear` : Génère un fichier EAR à partir du projet.
156. `mvn ear:generate-application-xml` : Génère le fichier `application.xml` pour le projet EAR.
157. `mvn eclipse:clean` : Supprime les fichiers de configuration d'Eclipse.
158. `mvn eclipse:eclipse` : Génère les fichiers de configuration pour Eclipse.
159. `mvn eclipse:to-maven` : Convertit un projet Eclipse en projet Maven.
160. `mvn enforcer:display-info` : Affiche les informations de l'environnement.
161. `mvn enforcer:enforce-once` : Exécute les règles d'application une seule fois.
162. `mvn flexmojos:compile-swf` : Compile un fichier SWF à partir de sources Flex.
163. `mvn flexmojos:compile-swc` : Compile un fichier SWC à partir de sources Flex.
164. `mvn flexmojos:asdoc` : Génère la documentation ASDoc pour Flex.
165. `mvn flexmojos:optimizer` : Optimise un fichier SWF.
166. `mvn flexmojos:swc-dependency` : Génère des dépendances à partir de fichiers SWC.
167. `mvn flexmojos:test-run` : Exécute les tests Flex.
168. `mvn gpg:clearsign` : Signe un fichier avec une signature claire GPG.
169. `mvn gpg:passphrase` : Fournit une passphrase pour GPG.
170. `mvn help:active-profiles` : Affiche les profils actifs.
171. `mvn help:all-profiles` : Affiche tous les profils.
172. `mvn help:evaluate` : Évalue une expression Maven.
173. `mvn help:effective-pom` : Affiche le POM effectif.
174. `mvn help:effective-settings` : Affiche les paramètres effectifs.
175. `mvn help:system` : Affiche les propriétés système.
176. `mvn idea:clean` : Supprime les fichiers de configuration d'IntelliJ IDEA.
177. `mvn idea:idea` : Génère les fichiers de configuration pour IntelliJ IDEA.
178. `mvn idea:module` : Génère le fichier de module pour IntelliJ IDEA.
179. `mvn idea:multiproject` : Génère les fichiers de configuration pour un projet multi-modules IntelliJ IDEA.
180. `mvn idea:resolve-dependencies` : Résout les dépendances pour IntelliJ IDEA.
181. `mvn idea:workspace` : Génère le fichier de workspace pour IntelliJ IDEA.
182. `mvn install:install-file` : Installe un fichier dans le dépôt local.
183. `mvn install:install` : Installe le projet dans le dépôt local.
184. `mvn j2ee:generate-application-xml` : Génère le fichier `application.xml` pour le projet J2EE.
185. `mvn j2ee:generate-client` : Génère un client pour le projet J2EE.
186. `mvn j2ee:generate-deployment-descriptor` : Génère le descripteur de déploiement pour le projet J2EE.
187. `mvn j2ee:generate-ejb-client` : Génère un client EJB pour le projet J2EE.
188. `mvn j2ee:generate-ejb-deployment-descriptor` : Génère le descripteur de déploiement EJB pour le projet J2EE.
189. `mvn j2ee:generate-web-deployment-descriptor` : Génère le descripteur de déploiement web pour le projet J2EE.
190. `mvn j2ee:inplace` : Déploie le projet J2EE en mode "in-place".
191. `mvn j2ee:package-client` : Emballe le client du projet J2EE.
192. `mvn j2ee:package-ejb` : Emballe l'EJB du projet J2EE.
193. `mvn j2ee:package-web` : Emballe le module web du projet J2EE.
194. `mvn j2ee:run` : Exécute le projet J2EE.
195. `mvn j2ee:start` : Démarre le serveur J2EE.
196. `mvn j2ee:stop` : Arrête le serveur J2EE.
197. `mvn j2ee:undeploy` : Retire le projet J2EE du serveur.
198. `mvn j2ee:verify` : Vérifie le projet J2EE.
199. `mvn jar:jar` : Génère un fichier JAR à partir du projet.
200. `mvn jar:test-jar` : Génère un fichier JAR pour les tests.
201. `mvn javadoc:javadoc` : Génère la documentation Javadoc du code source.
202. `mvn javadoc:test-javadoc` : Génère la documentation Javadoc du code source de test.
203. `mvn javadoc:jar` : Emballe la documentation Javadoc dans un JAR.
204. `mvn javadoc:test-jar` : Emballe la documentation Javadoc des tests dans un JAR.
205. `mvn javadoc:aggregate` : Agrège la documentation Javadoc de plusieurs modules.
206. `mvn javadoc:help` : Affiche l'aide du plugin Javadoc.
207. `mvn jaxb2:xjc` : Génère du code à partir d'un schéma XML avec JAXB2.
208. `mvn jaxb2:testXjc` : Génère du code pour les tests à partir d'un schéma XML avec JAXB2.
209. `mvn jboss-as:deploy` : Déploie le projet sur un serveur JBoss AS.
210. `mvn jboss-as:undeploy` : Retire le projet d'un serveur JBoss AS.
211. `mvn jboss-as:run` : Exécute le serveur JBoss AS.
212. `mvn jboss-as:start` : Démarre le serveur JBoss AS.
213. `mvn jboss-as:stop` : Arrête le serveur JBoss AS.
214. `mvn jboss-as:redeploy` : Redéploie le projet sur un serveur JBoss AS.
215. `mvn jboss-as:add-resource` : Ajoute une ressource au serveur JBoss AS.
216. `mvn jboss-as:remove-resource` : Supprime une ressource du serveur JBoss AS.
217. `mvn jboss-as:execute-commands` : Exécute des commandes sur le serveur JBoss AS.
218. `mvn jboss-as:shutdown` : Arrête le serveur JBoss AS.
219. `mvn jboss-as:status` : Affiche le statut du serveur JBoss AS.
220. `mvn jgitflow:feature-start` : Démarre une nouvelle fonctionnalité avec JGitFlow.
221. `mvn jgitflow:feature-finish` : Termine une fonctionnalité avec JGitFlow.
222. `mvn jgitflow:release-start` : Démarre une nouvelle release avec JGitFlow.
223. `mvn jgitflow:release-finish` : Termine une release avec JGitFlow.
224. `mvn jgitflow:hotfix-start` : Démarre un correctif avec JGitFlow.
225. `mvn jgitflow:hotfix-finish` : Termine un correctif avec JGitFlow.
226. `mvn jgitflow:support-start` : Démarre une branche de support avec JGitFlow.
227. `mvn jgitflow:support-finish` : Termine une branche de support avec JGitFlow.
228. `mvn jgitflow:feature-list` : Liste les fonctionnalités en cours avec JGitFlow.
229. `mvn jgitflow:release-list` : Liste les releases en cours avec JGitFlow.
230. `mvn jgitflow:hotfix-list` : Liste les correctifs en cours avec JGitFlow.
231. `mvn jgitflow:support-list` : Liste les branches de support avec JGitFlow.
232. `mvn jsonschema2pojo:generate` : Génère des classes Java à partir d'un schéma JSON.
233. `mvn karaf:assembly` : Crée une distribution personnalisée de Karaf.
234. `mvn karaf:archive` : Crée une archive de la distribution Karaf.
235. `mvn karaf:client` : Exécute une commande sur une instance Karaf.
236. `mvn karaf:features-add-to-repository` : Ajoute des fonctionnalités à un dépôt Karaf.
237. `mvn karaf:features-create-kar` : Crée un KAR (Karaf Archive) à partir de fonctionnalités.
238. `mvn karaf:features-generate-descriptor` : Génère un descripteur de fonctionnalités pour Karaf.
239. `mvn karaf:features-install` : Installe des fonctionnalités dans Karaf.
240. `mvn karaf:features-list` : Liste les fonctionnalités disponibles dans Karaf.
241. `mvn karaf:features-start` : Démarre des fonctionnalités dans Karaf.
242. `mvn karaf:features-stop` : Arrête des fonctionnalités dans Karaf.
243. `mvn karaf:features-uninstall` : Désinstalle des fonctionnalités de Karaf.
244. `mvn karaf:kar` : Génère un KAR (Karaf Archive).
245. `mvn karaf:run` : Exécute une instance de Karaf.
246. `mvn karaf:shell` : Ouvre une console shell Karaf.
247. `mvn license:add-third-party` : Ajoute des licences tierces au projet.
248. `mvn license:aggregate-add-third-party` : Agrège et ajoute des licences tierces pour les modules.
249. `mvn license:aggregate-download-licenses` : Télécharge les licences pour tous les modules.
250. `mvn license:check-file-header` : Vérifie les en-têtes de fichier pour les licences.
251. `mvn license:comment-style-list` : Liste les styles de commentaires disponibles pour les licences.
252. `mvn license:download-licenses` : Télécharge les licences des dépendances.
253. `mvn license:format` : Formate les en-têtes de fichier avec la licence.
254. `mvn license:help` : Affiche l'aide du plugin de licence.
255. `mvn license:remove-file-header` : Supprime les en-têtes de fichier de licence.
256. `mvn license:third-party-report` : Génère un rapport des licences tierces.
257. `mvn liquibase:changelogSync` : Marque tous les changements comme appliqués dans la base de données.
258. `mvn liquibase:clearCheckSums` : Efface les sommes de contrôle de la base de données.
259. `mvn liquibase:dbDoc` : Génère une documentation de la base de données.
260. `mvn liquibase:dropAll` : Supprime toutes les tables, vues et objets de la base de données.
261. `mvn liquibase:futureRollbackSQL` : Génère le SQL pour annuler les futurs changements.
262. `mvn liquibase:help` : Affiche l'aide du plugin Liquibase.
263. `mvn liquibase:listLocks` : Liste les verrous actifs sur la base de données.
264. `mvn liquibase:releaseLocks` : Libère tous les verrous sur la base de données.
265. `mvn liquibase:rollback` : Annule un certain nombre de changements dans la base de données.
266. `mvn liquibase:rollbackToDate` : Annule les changements jusqu'à une certaine date.
267. `mvn liquibase:rollbackToTag` : Annule les changements jusqu'à une certaine balise.
268. `mvn liquibase:status` : Affiche le statut des changements non appliqués.
269. `mvn liquibase:tag` : Attribue une balise à la base de données.
270. `mvn liquibase:update` : Applique les changements à la base de données.
271. `mvn liquibase:updateSQL` : Génère le SQL pour appliquer les changements.
272. `mvn liquibase:updateTestingRollback` : Teste les scripts de rollback.
273. `mvn maven-antrun-plugin:run` : Exécute des tâches Ant dans Maven.
274. `mvn maven-archetype-plugin:generate` : Génère un nouveau projet à partir d'un archetype.
275. `mvn maven-assembly-plugin:assembly` : Crée une archive du projet.
276. `mvn maven-changelog-plugin:changelog` : Génère un journal des modifications.
277. `mvn maven-clean-plugin:clean` : Nettoie les fichiers générés.
278. `mvn maven-compiler-plugin:compile` : Compile les sources du projet.
279. `mvn maven-compiler-plugin:testCompile` : Compile les sources de test du projet.
280. `mvn maven-deploy-plugin:deploy` : Déploie l'artefact dans un dépôt distant.
281. `mvn maven-enforcer-plugin:enforce` : Exécute les règles d'application.
282. `mvn maven-install-plugin:install` : Installe l'artefact dans le dépôt local.
283. `mvn maven-jar-plugin:jar` : Crée un JAR du projet.
284. `mvn maven-javadoc-plugin:javadoc` : Génère la documentation Javadoc.
285. `mvn maven-release-plugin:prepare` : Prépare une release.
286. `mvn maven-release-plugin:perform` : Effectue une release.
287. `mvn maven-release-plugin:rollback` : Annule une préparation de release.
288. `mvn maven-resources-plugin:resources` : Copie les ressources du projet.
289. `mvn maven-resources-plugin:testResources` : Copie les ressources de test du projet.
290. `mvn maven-site-plugin:site` : Génère le site du projet.
291. `mvn maven-surefire-plugin:test` : Exécute les tests du projet.
292. `mvn maven-war-plugin:war` : Crée un WAR du projet.
293. `mvn nexus-staging:deploy` : Déploie l'artefact dans Nexus Staging.
294. `mvn nexus-staging:release` : Publie l'artefact depuis Nexus Staging.
295. `mvn nexus-staging:drop` : Supprime l'artefact de Nexus Staging.
296. `mvn org.apache.maven.plugins:maven-antrun-plugin:1.8:run` : Exécute une version spécifique du plugin Antrun.
297. `mvn org.apache.maven.plugins:maven-assembly-plugin:2.6:assembly` : Exécute une version spécifique du plugin Assembly.
298. `mvn org.apache.maven.plugins:maven-compiler-plugin:3.8.0:compile` : Exécute une version spécifique du plugin Compiler.
299. `mvn org.apache.maven.plugins:maven-deploy-plugin:2.8.2:deploy` : Exécute une version spécifique du plugin Deploy.
300. `mvn org.apache.maven.plugins:maven-install-plugin:2.5.2:install` : Exécute une version spécifique du plugin Install.
301. `mvn dependency:analyze` : Analyse les dépendances du projet et rapporte les dépendances inutilisées ou non déclarées.
302. `mvn dependency:tree` : Affiche l'arbre des dépendances du projet.
303. `mvn dependency:purge-local-repository` : Supprime les dépendances du dépôt local et les re-télécharge.
304. `mvn dependency:copy` : Copie une dépendance spécifique dans un emplacement spécifié.
305. `mvn dependency:unpack` : Décompresse une dépendance dans un emplacement spécifié.
306. `mvn dependency:resolve` : Résout toutes les dépendances du projet.
307. `mvn dependency:resolve-plugins` : Résout tous les plugins et leurs dépendances.
308. `mvn dependency:copy-dependencies` : Copie toutes les dépendances du projet.
309. `mvn dependency:analyze-report` : Génère un rapport sur les dépendances du projet.
310. `mvn dependency:analyze-only` : Analyse les dépendances sans échouer le build.
311. `mvn dependency:analyze-duplicate` : Analyse et rapporte les dépendances en double.
312. `mvn dependency:list` : Liste toutes les dépendances du projet.
313. `mvn dependency:build-classpath` : Génère un classpath à partir des dépendances du projet.
314. `mvn dependency:sources` : Télécharge les sources des dépendances.
315. `mvn dependency:resolve-classpath` : Résout le classpath du projet.
316. `mvn dependency:get` : Télécharge une dépendance spécifique.
317. `mvn dependency:properties` : Affiche les propriétés des dépendances.
318. `mvn exec:exec` : Exécute un programme externe.
319. `mvn exec:java` : Exécute une classe Java avec les dépendances du projet.
320. `mvn versions:display-dependency-updates` : Affiche les mises à jour disponibles pour les dépendances.
321. `mvn versions:display-plugin-updates` : Affiche les mises à jour disponibles pour les plugins.
322. `mvn versions:set` : Modifie les versions des dépendances et/ou des plugins.
323. `mvn versions:lock-snapshots` : Verrouille les versions des snapshots.
324. `mvn versions:unlock-snapshots` : Déverrouille les versions des snapshots.
325. `mvn versions:commit` : Confirme les modifications de versions.
326. `mvn versions:revert` : Annule les modifications de versions.
327. `mvn versions:use-latest-releases` : Met à jour les dépendances et plugins vers les dernières versions.
328. `mvn versions:use-latest-snapshots` : Met à jour les dépendances et plugins vers les derniers snapshots.
329. `mvn versions:use-latest-versions` : Met à jour les dépendances et plugins vers les dernières versions ou snapshots.
330. `mvn versions:use-next-releases` : Met à jour les dépendances et plugins vers la prochaine version.
331. `mvn versions:use-next-snapshots` : Met à jour les dépendances et plugins vers le prochain snapshot.
332. `mvn versions:use-next-versions` : Met à jour les dépendances et plugins vers la prochaine version ou snapshot.
333. `mvn versions:use-releases` : Force l'utilisation de versions release pour les dépendances et plugins.
334. `mvn versions:use-snapshots` : Force l'utilisation de versions snapshot pour les dépendances et plugins.
335. `mvn site:site` : Génère le site du projet.
336. `mvn site:deploy` : Déploie le site du projet sur un serveur.
337. `mvn site:run` : Exécute un serveur pour prévisualiser le site.
338. `mvn site:stage` : Prépare le site pour le déploiement.
339. `mvn site:stage-deploy` : Déploie le site préparé.
340. `mvn site:attach-descriptor` : Attache un descripteur supplémentaire au site.
341. `mvn site:jar` : Emballe le site dans un JAR.
342. `mvn site:effective-site` : Affiche le site effectif.
343. `mvn site:help` : Affiche l'aide du plugin site.
344. `mvn clean:clean` : Nettoie les fichiers générés par Maven.
345. `mvn clean:help` : Affiche l'aide du plugin clean.
346. `mvn compiler:compile` : Compile les sources du projet.
347. `mvn compiler:testCompile` : Compile les sources de test du projet.
348. `mvn compiler:help` : Affiche l'aide du plugin compiler.
349. `mvn surefire:test` : Exécute les tests du projet.
350. `mvn surefire:help` : Affiche l'aide du plugin surefire.
351. `mvn install:install` : Installe l'artefact du projet dans le dépôt local.
352. `mvn install:help` : Affiche l'aide du plugin install.
353. `mvn deploy:deploy` : Déploie l'artefact du projet dans un dépôt distant.
354. `mvn deploy:help` : Affiche l'aide du plugin deploy.
355. `mvn archetype:generate` : Génère un nouveau projet à partir d'un archetype.
356. `mvn archetype:create-from-project` : Crée un archetype à partir du projet actuel.
357. `mvn archetype:crawl` : Recherche des archetypes dans les dépôts configurés.
358. `mvn archetype:help` : Affiche l'aide du plugin archetype.
359. `mvn assembly:assembly` : Crée une archive du projet avec ses dépendances.
360. `mvn assembly:single` : Crée une archive du projet sans ses dépendances.
361. `mvn assembly:help` : Affiche l'aide du plugin assembly.
362. `mvn release:prepare` : Prépare une release.
363. `mvn release:perform` : Effectue une release.
364. `mvn release:clean` : Nettoie les fichiers temporaires créés lors de la préparation de la release.
365. `mvn release:rollback` : Annule une préparation de release.
366. `mvn release:branch` : Crée une branche pour la release.
367. `mvn release:help` : Affiche l'aide du plugin release.
368. `mvn validate` : Valide que le projet est correct.
369. `mvn initialize` : Initialise les propriétés du build et d'autres tâches préliminaires.
370. `mvn generate-sources` : Génère les sources supplémentaires nécessaires pour le build.
371. `mvn process-sources` : Traite les sources.
372. `mvn generate-resources` : Génère les ressources.
373. `mvn process-resources` : Copie et traite les ressources.
374. `mvn package` : Emballe le code compilé dans un format distribuable.
375. `mvn verify` : Effectue des vérifications pour confirmer que le package est valide.
376. `mvn install` : Installe le package dans le dépôt local.
377. `mvn deploy` : Copie le package final dans un dépôt distant.
378. `mvn pre-clean` : Exécute des tâches avant le nettoyage.
379. `mvn post-clean` : Exécute des tâches après le nettoyage.
380. `mvn pre-site` : Exécute des tâches avant la génération du site.
381. `mvn post-site` : Exécute des tâches après la génération du site.
382. `mvn site-deploy` : Déploie le site généré.
383. `mvn pre-integration-test` : Exécute des tâches avant les tests d'intégration.
384. `mvn integration-test` : Exécute les tests d'intégration.
385. `mvn post-integration-test` : Exécute des tâches après les tests d'intégration.
386. `mvn process-test-sources` : Traite les sources de test.
387. `mvn process-test-resources` : Traite les ressources de test.
388. `mvn test-compile` : Compile les sources de test.
389. `mvn test` : Exécute les tests.
390. `mvn prepare-package` : Exécute des tâches avant l'emballage.
391. `mvn package` : Emballe le projet.
392. `mvn pre-verify` : Exécute des tâches avant la vérification.
393. `mvn verify` : Vérifie le package.
394. `mvn install` : Installe le package.
395. `mvn deploy` : Déploie le package.
396. `mvn pre-site` : Exécute des tâches avant la génération du site.
397. `mvn site` : Génère le site du projet.
398. `mvn post-site` : Exécute des tâches après la génération du site.
399. `mvn site-deploy` : Déploie le site généré.
400. `mvn scm:checkout` : Effectue un checkout du code source depuis le système de gestion de versions.
401. `mvn scm:update` : Met à jour le code source depuis le système de gestion de versions.
402. `mvn scm:checkin` : Effectue un checkin du code source dans le système de gestion de versions.
403. `mvn scm:tag` : Crée une balise dans le système de gestion de versions.
404. `mvn scm:branch` : Crée une branche dans le système de gestion de versions.
405. `mvn scm:status` : Affiche le statut du code source dans le système de gestion de versions.
406. `mvn scm:add` : Ajoute des fichiers au système de gestion de versions.
407. `mvn scm:remove` : Supprime des fichiers du système de gestion de versions.
408. `mvn scm:diff` : Affiche les différences entre le code source local et celui du système de gestion de versions.
409. `mvn scm:export` : Exporte le code source depuis le système de gestion de versions.
410. `mvn scm:validate` : Valide les paramètres de configuration du système de gestion de versions.
411. `mvn scm:changelog` : Génère un journal des modifications depuis le système de gestion de versions.
412. `mvn scm:help` : Affiche l'aide du plugin SCM.
413. `mvn tomcat7:run` : Exécute le projet dans un serveur Tomcat 7 intégré.
414. `mvn tomcat7:run-war` : Exécute le WAR du projet dans un serveur Tomcat 7 intégré.
415. `mvn tomcat7:deploy` : Déploie le projet sur un serveur Tomcat 7.
416. `mvn tomcat7:undeploy` : Retire le projet d'un serveur Tomcat 7.
417. `mvn tomcat7:redeploy` : Redéploie le projet sur un serveur Tomcat 7.
418. `mvn tomcat7:help` : Affiche l'aide du plugin Tomcat 7.
419. `mvn jetty:run` : Exécute le projet dans un serveur Jetty intégré.
420. `mvn jetty:run-war` : Exécute le WAR du projet dans un serveur Jetty intégré.
421. `mvn jetty:deploy` : Déploie le projet sur un serveur Jetty.
422. `mvn jetty:undeploy` : Retire le projet d'un serveur Jetty.
423. `mvn jetty:redeploy` : Redéploie le projet sur un serveur Jetty.
424. `mvn jetty:help` : Affiche l'aide du plugin Jetty.
425. `mvn wildfly:deploy` : Déploie le projet sur un serveur WildFly.
426. `mvn wildfly:undeploy` : Retire le projet d'un serveur WildFly.
427. `mvn wildfly:redeploy` : Redéploie le projet sur un serveur WildFly.
428. `mvn wildfly:start` : Démarre le serveur WildFly.
429. `mvn wildfly:stop` : Arrête le serveur WildFly.
430. `mvn wildfly:run` : Exécute le serveur WildFly.
431. `mvn wildfly:help` : Affiche l'aide du plugin WildFly.
432. `mvn cargo:run` : Exécute le projet dans un serveur intégré avec Cargo.
433. `mvn cargo:start` : Démarre le serveur avec Cargo.
434. `mvn cargo:stop` : Arrête le serveur avec Cargo.
435. `mvn cargo:deploy` : Déploie le projet sur un serveur avec Cargo.
436. `mvn cargo:undeploy` : Retire le projet d'un serveur avec Cargo.
437. `mvn cargo:redeploy` : Redéploie le projet sur un serveur avec Cargo.
438. `mvn cargo:help` : Affiche l'aide du plugin Cargo.
439. `mvn jboss-as:deploy` : Déploie le projet sur un serveur JBoss AS.
440. `mvn jboss-as:undeploy` : Retire le projet d'un serveur JBoss AS.
441. `mvn jboss-as:redeploy` : Redéploie le projet sur un serveur JBoss AS.
442. `mvn jboss-as:start` : Démarre le serveur JBoss AS.
443. `mvn jboss-as:stop` : Arrête le serveur JBoss AS.
444. `mvn jboss-as:run` : Exécute le serveur JBoss AS.
445. `mvn jboss-as:help` : Affiche l'aide du plugin JBoss AS.
446. `mvn glassfish:deploy` : Déploie le projet sur un serveur GlassFish.
447. `mvn glassfish:undeploy` : Retire le projet d'un serveur GlassFish.
448. `mvn glassfish:redeploy` : Redéploie le projet sur un serveur GlassFish.
449. `mvn glassfish:start` : Démarre le serveur GlassFish.
450. `mvn glassfish:stop` : Arrête le serveur GlassFish.
451. `mvn glassfish:run` : Exécute le serveur GlassFish.
452. `mvn glassfish:help` : Affiche l'aide du plugin GlassFish.
453. `mvn weblogic:deploy` : Déploie le projet sur un serveur WebLogic.
454. `mvn weblogic:undeploy` : Retire le projet d'un serveur WebLogic.
455. `mvn weblogic:redeploy` : Redéploie le projet sur un serveur WebLogic.
456. `mvn weblogic:start` : Démarre le serveur WebLogic.
457. `mvn weblogic:stop` : Arrête le serveur WebLogic.
458. `mvn weblogic:run` : Exécute le serveur WebLogic.
459. `mvn weblogic:help` : Affiche l'aide du plugin WebLogic.
460. `mvn websphere:deploy` : Déploie le projet sur un serveur WebSphere.
461. `mvn websphere:undeploy` : Retire le projet d'un serveur WebSphere.
462. `mvn websphere:redeploy` : Redéploie le projet sur un serveur WebSphere.
463. `mvn websphere:start` : Démarre le serveur WebSphere.
464. `mvn websphere:stop` : Arrête le serveur WebSphere.
465. `mvn websphere:run` : Exécute le serveur WebSphere.
466. `mvn websphere:help` : Affiche l'aide du plugin WebSphere.
467. `mvn sonar:sonar` : Analyse le projet avec SonarQube.
468. `mvn sonar:help` : Affiche l'aide du plugin SonarQube.
469. `mvn checkstyle:checkstyle` : Vérifie le style du code avec Checkstyle.
470. `mvn checkstyle:check` : Vérifie le style du code et échoue si des violations sont trouvées.
471. `mvn checkstyle:help` : Affiche l'aide du plugin Checkstyle.
472. `mvn pmd:pmd` : Analyse le code avec PMD.
473. `mvn pmd:check` : Vérifie le code avec PMD et échoue si des violations sont trouvées.
474. `mvn pmd:cpd` : Détecte le code dupliqué avec PMD.
475. `mvn pmd:help` : Affiche l'aide du plugin PMD.
476. `mvn findbugs:findbugs` : Analyse le code avec FindBugs.
477. `mvn findbugs:check` : Vérifie le code avec FindBugs et échoue si des bugs sont trouvés.
478. `mvn findbugs:gui` : Affiche l'interface graphique de FindBugs.
479. `mvn findbugs:help` : Affiche l'aide du plugin FindBugs.
480. `mvn jacoco:prepare-agent` : Prépare l'agent JaCoCo pour la mesure de la couverture du code.
481. `mvn jacoco:report` : Génère un rapport de couverture du code avec JaCoCo.
482. `mvn jacoco:check` : Vérifie la couverture du code avec JaCoCo et échoue si elle est en dessous d'un seuil.
483. `mvn jacoco:help` : Affiche l'aide du plugin JaCoCo.
484. `mvn jxr:jxr` : Génère un rapport de cross-referencing du code.
485. `mvn jxr:test-jxr` : Génère un rapport de cross-referencing du code de test.
486. `mvn jxr:help` : Affiche l'aide du plugin JXR.
487. `mvn enforcer:enforce` : Exécute les règles d'application avec le plugin Enforcer.
488. `mvn enforcer:display-info` : Affiche des informations sur l'environnement de build.
489. `mvn enforcer:help` : Affiche l'aide du plugin Enforcer.
490. `mvn formatter:format` : Formate le code source avec le plugin Formatter.
491. `mvn formatter:validate` : Vérifie si le code est bien formaté.
492. `mvn formatter:help` : Affiche l'aide du plugin Formatter.
493. `mvn spotbugs:spotbugs` : Analyse le code avec SpotBugs.
494. `mvn spotbugs:check` : Vérifie le code avec SpotBugs et échoue si des bugs sont trouvés.
495. `mvn spotbugs:gui` : Affiche l'interface graphique de SpotBugs.
496. `mvn spotbugs:help` : Affiche l'aide du plugin SpotBugs.
497. `mvn license:format` : Ajoute des en-têtes de licence aux fichiers du projet.
498. `mvn license:check` : Vérifie si les en-têtes de licence sont présents.
499. `mvn license:remove` : Supprime les en-têtes de licence des fichiers du projet.
500. `mvn license:help` : Affiche l'aide du plugin License.




