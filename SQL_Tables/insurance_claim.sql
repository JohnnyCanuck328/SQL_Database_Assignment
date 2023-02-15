-- Table: public.insurance_claim

-- DROP TABLE IF EXISTS public.insurance_claim;

CREATE TABLE IF NOT EXISTS public.insurance_claim
(
    claim_id integer NOT NULL,
    insurance_charge integer,
    patient_insurance integer NOT NULL,
    invoice_ integer NOT NULL,
    CONSTRAINT insurance_claim_pkey PRIMARY KEY (claim_id),
    CONSTRAINT insurance_claim_invoice__fkey FOREIGN KEY (invoice_)
        REFERENCES public.invoice (invoice_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT insurance_claim_patient_insurance_fkey FOREIGN KEY (patient_insurance)
        REFERENCES public.patient (patient_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.insurance_claim
    OWNER to postgres;