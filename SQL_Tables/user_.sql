-- Table: public.user_

-- DROP TABLE IF EXISTS public.user_;

CREATE TABLE IF NOT EXISTS public.user_
(
    userid integer NOT NULL,
    password_ character varying(50) COLLATE pg_catalog."default" NOT NULL,
    ssn integer NOT NULL,
    first_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    address character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user__pkey PRIMARY KEY (userid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.user_
    OWNER to postgres;