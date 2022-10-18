-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.delegaciones
(
    id_delegacion bigint NOT NULL,
    nombre character varying(100),
    PRIMARY KEY (id_delegacion)
);

CREATE TABLE IF NOT EXISTS public.accidentes
(
    periodo smallint,
    id_delegacion bigint,
    numero bigint
);

ALTER TABLE IF EXISTS public.accidentes
    ADD FOREIGN KEY (id_delegacion)
    REFERENCES public.delegaciones (id_delegacion) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;


CREATE TABLE IF NOT EXISTS public.vehiculos
(
    periodo smallint,
    id_delegacion bigint,
    numero bigint
);

ALTER TABLE IF EXISTS public.vehiculos
    ADD FOREIGN KEY (id_delegacion)
    REFERENCES public.delegaciones (id_delegacion) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;

INSERT INTO delegaciones (id_delegacion,nombre) VALUES (1,'Azcapotzalco');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (2,'Coyoacán');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (3,'Cuajimalpa de Morelos');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (4,'Gustavo A. Madero');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (5,'Iztacalco');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (6,'Iztapalapa');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (7,'La Magdalena Contreras');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (8,'Milpa Alta');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (9,'Álvaro Obregón');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (10,'Tláhuac');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (11,'Tlalpan');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (12,'Xochimilco');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (13,'Benito Juárez');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (14,'Cuauhtémoc');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (15,'Miguel Hidalgo');
INSERT INTO delegaciones (id_delegacion,nombre) VALUES (16,'Venustiano Carranza');

