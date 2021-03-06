--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book (
    ticket_id integer,
    passenger_id integer NOT NULL
);


ALTER TABLE public.book OWNER TO postgres;

--
-- Name: book_passenger_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."book_passenger_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."book_passenger_ID_seq" OWNER TO postgres;

--
-- Name: book_passenger_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."book_passenger_ID_seq" OWNED BY public.book.passenger_id;


--
-- Name: corresponds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.corresponds (
    ticket_id integer NOT NULL,
    seat_number integer NOT NULL
);


ALTER TABLE public.corresponds OWNER TO postgres;

--
-- Name: passenger; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.passenger (
    passenger_id integer NOT NULL,
    name character varying(80),
    gender character varying(80),
    age integer,
    username character varying(80),
    password character varying(80),
    email character varying(80),
    phone character varying(80)
);


ALTER TABLE public.passenger OWNER TO postgres;

--
-- Name: passenger_passenger_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."passenger_passenger_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."passenger_passenger_ID_seq" OWNER TO postgres;

--
-- Name: passenger_passenger_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."passenger_passenger_ID_seq" OWNED BY public.passenger.passenger_id;


--
-- Name: plane; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plane (
    "plane_ID" integer NOT NULL,
    type character varying(80),
    name character varying(80),
    num_seats integer
);


ALTER TABLE public.plane OWNER TO postgres;

--
-- Name: plane_plane_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."plane_plane_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."plane_plane_ID_seq" OWNER TO postgres;

--
-- Name: plane_plane_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."plane_plane_ID_seq" OWNED BY public.plane."plane_ID";


--
-- Name: seat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.seat (
    "ticket_ID" integer NOT NULL,
    seat_number integer,
    id integer
);


ALTER TABLE public.seat OWNER TO postgres;

--
-- Name: ticket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket (
    ticket_id integer NOT NULL,
    "plane_ID" integer,
    departure_city character varying(80),
    arrival_city character varying(80),
    cost character varying(80),
    departure_time character varying(80),
    arrival_time character varying(80),
    boarding_time character varying(80)
);


ALTER TABLE public.ticket OWNER TO postgres;

--
-- Name: ticket_ticket_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."ticket_ticket_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ticket_ticket_ID_seq" OWNER TO postgres;

--
-- Name: ticket_ticket_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."ticket_ticket_ID_seq" OWNED BY public.ticket.ticket_id;


--
-- Name: book passenger_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book ALTER COLUMN passenger_id SET DEFAULT nextval('public."book_passenger_ID_seq"'::regclass);


--
-- Name: passenger passenger_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passenger ALTER COLUMN passenger_id SET DEFAULT nextval('public."passenger_passenger_ID_seq"'::regclass);


--
-- Name: plane plane_ID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plane ALTER COLUMN "plane_ID" SET DEFAULT nextval('public."plane_plane_ID_seq"'::regclass);


--
-- Name: ticket ticket_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket ALTER COLUMN ticket_id SET DEFAULT nextval('public."ticket_ticket_ID_seq"'::regclass);


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.book (ticket_id, passenger_id) FROM stdin;
1	7
2	2
3	3
4	4
5	5
\.


--
-- Data for Name: corresponds; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.corresponds (ticket_id, seat_number) FROM stdin;
1	7
\.


--
-- Data for Name: passenger; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.passenger (passenger_id, name, gender, age, username, password, email, phone) FROM stdin;
1	John Doe	M	25	JohnDoey	password	JD123@gmail.com	4808887777
2	Jane Doe	F	23	JaneDoey	password	JD321@gmail.com	4805674567
3	Hugh Jackson	M	40	HugeJack	password	Imswole@gmail.com	4564564566
4	Chris Hammel	M	32	Hammel11	password	Hammel112@gmail.com	2345672345
7	James	M	21	username	password	Testemail@gmail.com	4801231234
\.


--
-- Data for Name: plane; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plane ("plane_ID", type, name, num_seats) FROM stdin;
123	Boeing 737	maestro	126
\.


--
-- Data for Name: seat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.seat ("ticket_ID", seat_number, id) FROM stdin;
1	7	28
1	7	28
2	50	36
3	57	13
4	93	32
5	11	226
6	290	69
\.


--
-- Data for Name: ticket; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket (ticket_id, "plane_ID", departure_city, arrival_city, cost, departure_time, arrival_time, boarding_time) FROM stdin;
1	123	Phoenix	Houston	200	7:30PM	10:30PM	7:00PM
2	123	Phoenix	Houston	200	7:30PM	10:30PM	7:00PM
3	724	Los Angeles	New York City	350	12:00PM	6:00PM	11:30AM
4	910	Portland	Miami	200	8:00AM	2:00PM	7:30AM
\.


--
-- Name: book_passenger_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."book_passenger_ID_seq"', 2, true);


--
-- Name: passenger_passenger_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."passenger_passenger_ID_seq"', 7, true);


--
-- Name: plane_plane_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."plane_plane_ID_seq"', 1, false);


--
-- Name: ticket_ticket_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."ticket_ticket_ID_seq"', 1, false);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (passenger_id);


--
-- Name: corresponds corresponds_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.corresponds
    ADD CONSTRAINT corresponds_pkey PRIMARY KEY (ticket_id, seat_number);


--
-- Name: passenger passenger_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passenger
    ADD CONSTRAINT passenger_pkey PRIMARY KEY (passenger_id);


--
-- Name: passenger passenger_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passenger
    ADD CONSTRAINT passenger_username_key UNIQUE (username);


--
-- Name: plane plane_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plane
    ADD CONSTRAINT plane_pkey PRIMARY KEY ("plane_ID");


--
-- Name: ticket ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket
    ADD CONSTRAINT ticket_pkey PRIMARY KEY (ticket_id);


--
-- PostgreSQL database dump complete
--

