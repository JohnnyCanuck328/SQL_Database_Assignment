-- Table: public.appointment

-- DROP TABLE IF EXISTS public.appointment;

CREATE TABLE IF NOT EXISTS public.appointment
(
    appointment_id integer NOT NULL,
    start_time time(0) without time zone NOT NULL,
    end_time time(0) without time zone NOT NULL,
    date_ date NOT NULL,
    appointment_type character varying(20) COLLATE pg_catalog."default",
    staus status_type,
    room_assigned integer NOT NULL,
    patient integer,
    dentist integer,
    record_ integer,
    invoice_ integer NOT NULL,
    CONSTRAINT appointment_pkey PRIMARY KEY (appointment_id),
    CONSTRAINT appointment_dentist_fkey FOREIGN KEY (dentist)
        REFERENCES public.employee (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT appointment_invoice__fkey FOREIGN KEY (invoice_)
        REFERENCES public.invoice (invoice_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT appointment_patient_fkey FOREIGN KEY (patient)
        REFERENCES public.patient (patient_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT appointment_record__fkey FOREIGN KEY (record_)
        REFERENCES public.record (record_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.appointment
    OWNER to postgres;