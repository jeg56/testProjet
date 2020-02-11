-- Table: test13.refmarket

-- DROP TABLE test13.refmarket;

CREATE TABLE test13.refmarket2
(
    id integer NOT NULL DEFAULT nextval('test13.refmarket_id_seq'::regclass),
    nom character varying(200) COLLATE pg_catalog."default" NOT NULL,
    adresse character varying(200) COLLATE pg_catalog."default" NOT NULL,
    cp character varying(5) COLLATE pg_catalog."default" NOT NULL,
    ville character varying(200) COLLATE pg_catalog."default" NOT NULL,
    latitude numeric(15,11) NOT NULL,
    latitlongitudeude numeric(15,11) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    "plageHoraire_id" integer NOT NULL,
    CONSTRAINT refmarket_pkey PRIMARY KEY (id),
    CONSTRAINT "refmarket_plageHoraire_id_7b247091_fk_refplagehoraire_id" FOREIGN KEY ("plageHoraire_id")
        REFERENCES test13.refplagehoraire (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE test13.refmarket2
    OWNER to postgres;

-- Index: refmarket_plageHoraire_id_7b247091

-- DROP INDEX test13."refmarket_plageHoraire_id_7b247091";

CREATE INDEX "refmarket_plageHoraire_id_7b247091"
    ON test13.refmarket2 USING btree
    ("plageHoraire_id")
    TABLESPACE pg_default;