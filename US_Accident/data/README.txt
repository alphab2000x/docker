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

Créer tout d'abord une base de données:

	Il est important de faire attention à ce que le nombre de champ correspondent au nombre de features dans notre dataset

CREATE TABLE Public."US_Accidents_June20_mini" (IDAccident int, ID varchar(50),Source varchar(50),TMC varchar(50),Severity varchar(50),
Start_Time varchar(50), End_Time varchar(50),
Start_Lat varchar(50),Start_Lng varchar(50),End_Lat varchar(50),End_Lng varchar(50),
Distance varchar(50),Description varchar(300),Number varchar(50),
Street varchar(50),Side varchar(50),City varchar(50),County varchar(50),State varchar(50),
Zipcode varchar(50),Country varchar(50),Timezone varchar(50),Airport_Code varchar(50),Weather_Timestamp varchar(50),
Temperature varchar(50),Wind_Chill varchar(50),Humidity varchar(50),Pressure varchar(50), Visibility varchar(50),
Wind_Direction varchar(50),
Wind_Speed varchar(50),Precipitation varchar(50),
Weather_Condition varchar(50),
Amenity varchar(50),Bump varchar(50),Crossing varchar(50),Give_Way varchar(50),Junction varchar(50),
No_Exit varchar(50),Railway varchar(50),Roundabout varchar(50),Station varchar(50),Stop varchar(50),
Traffic_Calming varchar(50),Traffic_Signal varchar(50),Turning_Loop varchar(50),
Sunrise_Sunset varchar(50),Civil_Twilight varchar(50),Nautical_Twilight varchar(50),Astronomical_Twilight varchar(50));


Supprimer en cas d'erreur:

	DROP TABLE Public."US_Accidents_June20_mini";

Liées notre fichier csv à notre table de postgres:

	COPY Public."US_Accidents_June20_mini" FROM '/usr/src/postgres/US_Accidents_June20_mini.csv' DELIMITER ',' CSV;

Réquête de projection:

	SELECT * FROM Public."US_Accidents_June20_mini";

Exporter notre table dans un ficheir csv:

	COPY Public."US_Accidents_June20_mini" TO '/usr/src/postgres/US_Psql.csv' DELIMITER ',' CSV HEADER;

Donner les droits s'il faut :
	
	chmod 777 postgres/    //Si possible éviter de faire un chmod 777

	
	SELECT * FROM utilisateur;
	
Quitter la base de données:

	\q