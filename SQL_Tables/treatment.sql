-- Table: public.treatment

-- DROP TABLE IF EXISTS public.treatment;

CREATE TABLE IF NOT EXISTS public.treatment
(
    treatment integer NOT NULL,
    appointment_ integer NOT NULL,
    treatment_type character varying(20) COLLATE pg_catalog."default" NOT NULL,
    medication character varying(50) COLLATE pg_catalog."default",
    symptoms character varying(250) COLLATE pg_catalog."default",
    tooth integer,
    comments_ character varying(250) COLLATE pg_catalog."default",
    CONSTRAINT treatment_pkey PRIMARY KEY (treatment),
    CONSTRAINT treatment_appointment__fkey FOREIGN KEY (appointment_)
        REFERENCES public.appointment (appointment_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.treatment
    OWNER to postgres;