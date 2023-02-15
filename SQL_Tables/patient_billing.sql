-- Table: public.patient_billing

-- DROP TABLE IF EXISTS public.patient_billing;

CREATE TABLE IF NOT EXISTS public.patient_billing
(
    billing_id integer NOT NULL DEFAULT nextval('patient_billing_billing_id_seq'::regclass),
    date_of_visit date NOT NULL,
    start_time time(0) without time zone NOT NULL,
    end_time time(0) without time zone NOT NULL,
    procedure_ integer NOT NULL,
    patient_portion money,
    insurance_portion money,
    total_billing money NOT NULL,
    pay payment_type NOT NULL,
    CONSTRAINT patient_billing_pkey PRIMARY KEY (billing_id),
    CONSTRAINT patient_billing_procedure__fkey FOREIGN KEY (procedure_)
        REFERENCES public.appointment_procedure (procedure_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.patient_billing
    OWNER to postgres;