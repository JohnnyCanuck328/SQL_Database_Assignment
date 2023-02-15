-- Table: public.patient_phone

-- DROP TABLE IF EXISTS public.patient_phone;

CREATE TABLE IF NOT EXISTS public.patient_phone
(
    patient_ integer NOT NULL,
    phone_number character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT patient_phone_pkey PRIMARY KEY (phone_number),
    CONSTRAINT patient_phone_patient__fkey FOREIGN KEY (patient_)
        REFERENCES public.patient (patient_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.patient_phone
    OWNER to postgres;