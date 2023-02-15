-- Table: public.fee_charge

-- DROP TABLE IF EXISTS public.fee_charge;

CREATE TABLE IF NOT EXISTS public.fee_charge
(
    fee_identifier integer NOT NULL,
    procedure_ integer NOT NULL,
    fee_code integer NOT NULL,
    charge money NOT NULL,
    CONSTRAINT fee_charge_pkey PRIMARY KEY (fee_identifier),
    CONSTRAINT fee_charge_procedure__fkey FOREIGN KEY (procedure_)
        REFERENCES public.appointment_procedure (procedure_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.fee_charge
    OWNER to postgres;