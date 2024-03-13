CREATE TABLE public."user" (
	user_id serial NOT NULL,
	user_identifier uuid NOT NULL,
	f_name varchar NOT NULL,
	m_name varchar NULL,
	l_name varchar NOT NULL,
	primary_contact_number varchar NOT NULL,
	primary_email varchar NOT NULL,
	secondary_contact_number varchar NOT NULL,
	secondary_email varchar NOT NULL,
	address varchar NOT NULL,
	pincode varchar NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (user_id)
)
TABLESPACE pg_default
;
