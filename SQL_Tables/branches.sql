-- Table: public.branches

-- DROP TABLE IF EXISTS public.branches;

CREATE TABLE IF NOT EXISTS public.branches
(
    branch_id integer NOT NULL,
    city character(20) COLLATE pg_catalog."default" NOT NULL,
    manager integer NOT NULL,
    receptionist_one integer NOT NULL,
    receptionist_two integer,
    CONSTRAINT branches_pkey PRIMARY KEY (branch_id),
    CONSTRAINT branches_manager_fkey FOREIGN KEY (manager)
        REFERENCES public.employee (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT branches_receptionist_one_fkey FOREIGN KEY (receptionist_one)
        REFERENCES public.employee (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT branches_receptionist_two_fkey FOREIGN KEY (receptionist_two)
        REFERENCES public.employee (employee_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.branches
    OWNER to postgres;