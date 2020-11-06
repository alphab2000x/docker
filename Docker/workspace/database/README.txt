#########################
#                       #
#	POSTGRES        #
#                       #
#########################


Nous allons créer une base de données sur docker avec postgres :

docker-compose:

	version: "3.2"
	services:
		database:
			image: postgres
			ports:
			   - "5432:5432"  
			networks:
			   node_net:
				 ipv4_address: 172.28.1.8
			volumes:
			   - database-data:/var/lib/postgresql/data
			env_file:
			   - ./database/database.env

	volumes:
		database-data:

				 
	networks:
	  node_net:
		ipam:
		  driver: default
		  config:
			- subnet: 172.28.0.0/16

Pour construire notre docker-compose:

	docker-compose up -d //Construit, (re) crée, démarre et s'attache à des conteneurs pour un service.
	
Pour l'éxécuter dans un termainal de commande:
	
	docker exec -it workspace_database_1 bash
	
Connexion à la base de données:

	psql -U abarry -d db

Création de table:

	CREATE TABLE utilisateur
	(
		id INT PRIMARY KEY NOT NULL,
		nom VARCHAR(100),
		prenom VARCHAR(100),
		email VARCHAR(255),
		date_naissance DATE,
		pays VARCHAR(255),
		ville VARCHAR(255),
		code_postal VARCHAR(5),
		nombre_achat INT
	)
	
	SELECT * FROM utilisateur;
	
Quitter la base de données:

	\q