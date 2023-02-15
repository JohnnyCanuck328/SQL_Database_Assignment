-- Table: public.record

-- DROP TABLE IF EXISTS public.record;

CREATE TABLE IF NOT EXISTS public.record
(
    record_id integer NOT NULL,
    price integer,
    visit_type character varying(50) COLLATE pg_catalog."default",
    assigned_dentist character varying(50) COLLATE pg_catalog."default",
    additional_notes character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT record_pkey PRIMARY KEY (record_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.record
    OWNER to postgres;