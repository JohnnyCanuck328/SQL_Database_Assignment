-- Table: public.patient

-- DROP TABLE IF EXISTS public.patient;

CREATE TABLE IF NOT EXISTS public.patient
(
    patient_id integer NOT NULL,
    gender character(1) COLLATE pg_catalog."default" NOT NULL,
    insurance character varying(20) COLLATE pg_catalog."default" NOT NULL,
    email_address character varying(50) COLLATE pg_catalog."default" NOT NULL,
    date_of_birth date NOT NULL,
    age_status character varying(20) COLLATE pg_catalog."default" NOT NULL,
    guardian_id integer,
    CONSTRAINT patient_pkey PRIMARY KEY (patient_id),
    CONSTRAINT patient_guardian_id_fkey FOREIGN KEY (guardian_id)
        REFERENCES public.user_ (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT patient_patient_id_fkey FOREIGN KEY (patient_id)
        REFERENCES public.user_ (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.patient
    OWNER to postgres;