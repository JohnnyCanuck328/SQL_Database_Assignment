-- Table: public.invoice

-- DROP TABLE IF EXISTS public.invoice;

CREATE TABLE IF NOT EXISTS public.invoice
(
    invoice_id integer NOT NULL,
    date_of_issue date NOT NULL,
    contact_information character varying(500) COLLATE pg_catalog."default",
    patient_charge integer NOT NULL,
    insurance_charge integer NOT NULL,
    total_fee_charge integer NOT NULL,
    discount integer NOT NULL,
    penalty integer DEFAULT 0,
    CONSTRAINT invoice_pkey PRIMARY KEY (invoice_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.invoice
    OWNER to postgres;