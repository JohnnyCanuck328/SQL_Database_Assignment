-- Table: public.appointment_procedure

-- DROP TABLE IF EXISTS public.appointment_procedure;

CREATE TABLE IF NOT EXISTS public.appointment_procedure
(
    procedure_id integer NOT NULL,
    procedure_code integer NOT NULL,
    date_ date NOT NULL,
    patient_proc integer NOT NULL,
    tooth_involved integer NOT NULL,
    proc_type procedure_type NOT NULL,
    appointment_ integer NOT NULL,
    description character varying(250) COLLATE pg_catalog."default",
    dose_amount character varying(50) COLLATE pg_catalog."default",
    invoice_ integer,
    CONSTRAINT appointment_procedure_pkey PRIMARY KEY (procedure_id),
    CONSTRAINT appointment_procedure_appointment__fkey FOREIGN KEY (appointment_)
        REFERENCES public.appointment (appointment_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT appointment_procedure_invoice__fkey FOREIGN KEY (invoice_)
        REFERENCES public.invoice (invoice_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT appointment_procedure_patient_proc_fkey FOREIGN KEY (patient_proc)
        REFERENCES public.patient (patient_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.appointment_procedure
    OWNER to postgres;