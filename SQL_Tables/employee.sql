-- Table: public.employee

-- DROP TABLE IF EXISTS public.employee;

CREATE TABLE IF NOT EXISTS public.employee
(
    employee_id integer NOT NULL,
    role_ character varying(20) COLLATE pg_catalog."default" NOT NULL,
    salary money NOT NULL,
    branch_id integer NOT NULL,
    CONSTRAINT employee_pkey PRIMARY KEY (employee_id),
    CONSTRAINT employee_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.user_ (userid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employee
    OWNER to postgres;