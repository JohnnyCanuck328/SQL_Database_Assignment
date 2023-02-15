-- Table: public.employee_location

-- DROP TABLE IF EXISTS public.employee_location;

CREATE TABLE IF NOT EXISTS public.employee_location
(
    branch_id integer NOT NULL,
    employee_id integer NOT NULL,
    CONSTRAINT employee_location_pkey PRIMARY KEY (branch_id, employee_id),
    CONSTRAINT employee_location_branch_id_fkey FOREIGN KEY (branch_id)
        REFERENCES public.branches (branch_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT employee_location_employee_id_fkey FOREIGN KEY (employee_id)
        REFERENCES public.employee (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employee_location
    OWNER to postgres;