--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-06-27 08:50:28

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
-- TOC entry 222 (class 1259 OID 16659)
-- Name: carrinho; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.carrinho (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    produto_id integer NOT NULL,
    nome_produto character varying(50),
    imagem_produto character varying(50),
    quantidade integer,
    observacao text,
    preco_total numeric(10,2)
);


ALTER TABLE public.carrinho OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16658)
-- Name: carrinho_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.carrinho_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.carrinho_id_seq OWNER TO postgres;

--
-- TOC entry 4834 (class 0 OID 0)
-- Dependencies: 221
-- Name: carrinho_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.carrinho_id_seq OWNED BY public.carrinho.id;


--
-- TOC entry 224 (class 1259 OID 16678)
-- Name: pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    data_pedido timestamp without time zone,
    forma_pagamento character varying(100),
    endereco_entrega character varying(400),
    status character varying(100),
    valor_total numeric(10,2),
    observacao text,
    itens_comprados text
);


ALTER TABLE public.pedido OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16677)
-- Name: pedido_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pedido_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pedido_id_seq OWNER TO postgres;

--
-- TOC entry 4835 (class 0 OID 0)
-- Dependencies: 223
-- Name: pedido_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pedido_id_seq OWNED BY public.pedido.id;


--
-- TOC entry 220 (class 1259 OID 16650)
-- Name: produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produto (
    id integer NOT NULL,
    nome_produto character varying(200) NOT NULL,
    tipo_produto character varying(200),
    tamanho character varying(200),
    ingrediente character varying(200),
    preco numeric(10,2) NOT NULL,
    descricao text,
    imagem character varying(250)
);


ALTER TABLE public.produto OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16649)
-- Name: produto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.produto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.produto_id_seq OWNER TO postgres;

--
-- TOC entry 4836 (class 0 OID 0)
-- Dependencies: 219
-- Name: produto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.produto_id_seq OWNED BY public.produto.id;


--
-- TOC entry 216 (class 1259 OID 16628)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    sobrenome character varying(100) NOT NULL,
    telefone character varying(20),
    email character varying(120) NOT NULL,
    senha character varying(100) NOT NULL,
    endereco character varying(200),
    numero_casa character varying(20),
    complemento character varying(100),
    bairro character varying(100),
    tipo_usuario character varying(20)
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16627)
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuario_id_seq OWNER TO postgres;

--
-- TOC entry 4837 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_id_seq OWNED BY public.usuario.id;


--
-- TOC entry 218 (class 1259 OID 16639)
-- Name: usuarioadmin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarioadmin (
    id integer NOT NULL,
    nome character varying(200),
    sobrenome character varying(200),
    email character varying(100) NOT NULL,
    senha character varying(200),
    tipo_cliente character varying(50)
);


ALTER TABLE public.usuarioadmin OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16638)
-- Name: usuarioadmin_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarioadmin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarioadmin_id_seq OWNER TO postgres;

--
-- TOC entry 4838 (class 0 OID 0)
-- Dependencies: 217
-- Name: usuarioadmin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarioadmin_id_seq OWNED BY public.usuarioadmin.id;


--
-- TOC entry 4657 (class 2604 OID 16662)
-- Name: carrinho id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho ALTER COLUMN id SET DEFAULT nextval('public.carrinho_id_seq'::regclass);


--
-- TOC entry 4658 (class 2604 OID 16681)
-- Name: pedido id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido ALTER COLUMN id SET DEFAULT nextval('public.pedido_id_seq'::regclass);


--
-- TOC entry 4656 (class 2604 OID 16653)
-- Name: produto id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto ALTER COLUMN id SET DEFAULT nextval('public.produto_id_seq'::regclass);


--
-- TOC entry 4654 (class 2604 OID 16631)
-- Name: usuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_seq'::regclass);


--
-- TOC entry 4655 (class 2604 OID 16642)
-- Name: usuarioadmin id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarioadmin ALTER COLUMN id SET DEFAULT nextval('public.usuarioadmin_id_seq'::regclass);


--
-- TOC entry 4826 (class 0 OID 16659)
-- Dependencies: 222
-- Data for Name: carrinho; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.carrinho (id, usuario_id, produto_id, nome_produto, imagem_produto, quantidade, observacao, preco_total) FROM stdin;
\.


--
-- TOC entry 4828 (class 0 OID 16678)
-- Dependencies: 224
-- Data for Name: pedido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedido (id, usuario_id, data_pedido, forma_pagamento, endereco_entrega, status, valor_total, observacao, itens_comprados) FROM stdin;
1	1	2024-06-27 08:25:25.051373	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	67.00	Duplo Bacon Brioche Cheddar   - Observação: sas \n\nPorção Batata Frita - Nuggets  - Observação: quero sem molho  \n\nCoca-Cola 350 ml  - Observação: sa \n	Duplo Bacon Brioche Cheddar  - Quantidade: 1\n\nPorção Batata Frita - Nuggets - Quantidade: 1\n\nCoca-Cola 350 ml - Quantidade: 1\n
\.


--
-- TOC entry 4824 (class 0 OID 16650)
-- Dependencies: 220
-- Data for Name: produto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produto (id, nome_produto, tipo_produto, tamanho, ingrediente, preco, descricao, imagem) FROM stdin;
1	X-Tudo Artesanal	Artesanal	Hamburguer Artesanal	Bacon - Calabresa - Salada - Molho - 1 Carne - Ovo - Cheddar	30.00	Um delicioso hamburguer artesanal, com a carne feita diretamente na grelha	xtudoartesanal.jpg
2	Brioche Artesanal 	Artesanal	Hamburguer Artesanal	Salada - Molho - Cebola - 1 Carne - Cheddar - Barbecue	25.00	Um delicioso hamburguer artesanal, com a carne feita diretamente na grelha	x-tudo-artesanal.jpg
3	Duplo Bacon Brioche Cheddar 	Artesanal	Hamburguer Artesanal	Bacon - Molho - 2 Carnes - Cheddar	30.00	Um delicioso hamburguer, com a carne feita diretamente na grelha e com muito cheddar	Cheddar.jpg
4	Duplo Burguer Brioche Barbecue	Artesanal	Hamburguer Artesanal	Salada - Molho - 2 Carnes - Barbecue	25.00	Um delicioso hamburguer, com a carne feita diretamente na grelha	663ccd6be0eef-barbecue.jpg
5	Duplo Brioche Salada 	Artesanal	Hamburguer Artesanal	Salada - Molho - 2 Carnes - Cheddar	23.00	Um delicioso hamburguer artesanal, com a carne feita diretamente na grelha	doubleSalada.jpg
6	Duplo Cheddar Brioche 	Artesanal	Hamburguer Artesanal	Molho - 2 Carnes - Cheddar	25.00	Um delicioso hamburguer artesanal, com a carne feita diretamente na grelha	Duplo-Cheddar.png
7	Brioche Salada	Artesanal	Hamburguer Artesanal	Salada - 1 Carne - Cheddar	20.00	Um delicioso hamburguer artesanal, com a carne feita diretamente na grelha	salada.jpg
8	Cheese Brioche Bacon	Artesanal	Hamburguer Artesanal	Bacon - Salada - Queijo - 1 Carne - Cheddar	22.00	Um delicioso hamburguer artesanal, com a carne feita diretamente na grelha	cheesesalada.jpg
9	Coca-Cola Zero 600 ml	Bebida	600 ml		10.00	Bem gelado 	coca600.jpg
10	Coca-Cola 350 ml	Bebida	350 ml		7.00	Bem gelado 	coca350.jpg
11	Coca-Cola 600 ml	Bebida	600 ml		10.00	Bem gelado 	coca.jpg
12	Guarana Antarctica 2 litro	Bebida	2 litros		14.00	Bem gelado 	guarana2.jpg
13	Guaravita	Bebida	290 ml		3.00	Bem gelado 	guaravita.jpg
14	H20 Limão	Bebida			8.00	Bem gelado 	h2o.jpg
15	Coca-Cola 350 Zero ml	Bebida	350 ml		7.00	Bem gelado 	coca.png
16	Coca-Cola 2L	Bebida	2 litros		14.00	Bem gelado 	coca_2litros.jpg
17	X-Tudo Picanha	Tradicional	Hamburguer Tradicional	Bacon - Calabresa - Salada - Molho - Queijo - 1 Carne - Ovo	18.00	Um delicioso hamburguer com carne de picanha	xtudopicanha.jpg
18	X-Cheddar Duplo	Tradicional	Hamburguer Tradicional	Molho - 2 Carnes - Cheddar	14.00	Um delicioso hamburguer com  bastante cheddar	663ccfa1b50cd-cheddar.jpg
19	X-Calabresa	Tradicional	Hamburguer Tradicional	Calabresa - Salada - Molho - Queijo - 1 Carne	14.00	Um delicioso hamburguer com carne 	calabresa.jpg
20	X-Eggs	Tradicional	Hamburguer Tradicional	Salada - Molho - Queijo - 1 Carne - Ovo	14.00	Um delicioso hamburguer com carne 	x_eggs.jpeg
21	X-Salada	Tradicional		Salada - Queijo - 1 Carne	12.00	Um delicioso hamburguer com carne  	x-salada.jpeg
22	X-Tudo 	Tradicional	Hamburguer Tradicional	Bacon - Calabresa - Salada - Molho - Queijo - 1 Carne - Ovo	15.00	Um delicioso hamburguer com carne recheado de bacon e calabresa 	Xtudo.jpg
23	X-Bacon	Tradicional		Bacon - Salada - Molho - Queijo - 1 Carne	14.00	Um delicioso hamburguer com carne 	x-tudo.jpg
24	Cheese Burguer 	Tradicional	Hamburguer Tradicional	Salada - Molho - 1 Carne	8.00	Um delicioso hamburguer com carne 	HAMBURGER.jpg
25	Batata Frita Maluca	Porcao	Porcao Grande	Bacon - Batata frita - Cheddar	35.00	Uma porção serve até 4 pessoas 	batamaluca.jpg
26	Batata Frita G	Porcao	Porcao Grande	Batata frita	25.00	Uma porção serve até 4 pessoas 	batataG.jpeg
27	Batata Frita M	Porcao	Porcao Media	Batata frita	15.00	Uma porção serve até 2 pessoas 	batataM.jpeg
28	Union Ring G	Porcao	Porcao Grande		25.00	Uma porção vem com 18 unidades	unionringG.jpg
29	Union Ring M	Porcao	Porcao Media		15.00	Uma porção vem com 9 unidades	unionringM.jpg
32	Nuggest M	Porcao	Porcao Media		12.00	Uma porção vem com 6 unidades	nuggest.png
33	Nuggest G	Porcao	Porcao Grande	Nuggets	20.00	Uma porção vem com 12 unidades	nuggest.png
34	Porção Batata Frita - Nuggets	Porcao	Porcao Media	Batata frita - Nuggets - Molho	30.00	Com bastante batata frita\r\nUma porção vem com 6 unidades	porcao.png
\.


--
-- TOC entry 4820 (class 0 OID 16628)
-- Dependencies: 216
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id, nome, sobrenome, telefone, email, senha, endereco, numero_casa, complemento, bairro, tipo_usuario) FROM stdin;
1	LUCAS	MOREIRA	21993432153	lukas.silvalsm11@gmail.com	102030	Rua Um	00	Lote 31 Quadra 2 	Centra-Duque de Caxias	Cliente
\.


--
-- TOC entry 4822 (class 0 OID 16639)
-- Dependencies: 218
-- Data for Name: usuarioadmin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarioadmin (id, nome, sobrenome, email, senha, tipo_cliente) FROM stdin;
1	LUCAS	MOREIRA	lukas.silvalsm@gmail.com	102030	Administrador
\.


--
-- TOC entry 4839 (class 0 OID 0)
-- Dependencies: 221
-- Name: carrinho_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.carrinho_id_seq', 3, true);


--
-- TOC entry 4840 (class 0 OID 0)
-- Dependencies: 223
-- Name: pedido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pedido_id_seq', 1, true);


--
-- TOC entry 4841 (class 0 OID 0)
-- Dependencies: 219
-- Name: produto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produto_id_seq', 34, true);


--
-- TOC entry 4842 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_id_seq', 1, true);


--
-- TOC entry 4843 (class 0 OID 0)
-- Dependencies: 217
-- Name: usuarioadmin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarioadmin_id_seq', 1, true);


--
-- TOC entry 4670 (class 2606 OID 16666)
-- Name: carrinho carrinho_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho
    ADD CONSTRAINT carrinho_pkey PRIMARY KEY (id);


--
-- TOC entry 4672 (class 2606 OID 16685)
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (id);


--
-- TOC entry 4668 (class 2606 OID 16657)
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id);


--
-- TOC entry 4660 (class 2606 OID 16637)
-- Name: usuario usuario_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_email_key UNIQUE (email);


--
-- TOC entry 4662 (class 2606 OID 16635)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- TOC entry 4664 (class 2606 OID 16648)
-- Name: usuarioadmin usuarioadmin_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarioadmin
    ADD CONSTRAINT usuarioadmin_email_key UNIQUE (email);


--
-- TOC entry 4666 (class 2606 OID 16646)
-- Name: usuarioadmin usuarioadmin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarioadmin
    ADD CONSTRAINT usuarioadmin_pkey PRIMARY KEY (id);


--
-- TOC entry 4673 (class 2606 OID 16672)
-- Name: carrinho carrinho_produto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho
    ADD CONSTRAINT carrinho_produto_id_fkey FOREIGN KEY (produto_id) REFERENCES public.produto(id);


--
-- TOC entry 4674 (class 2606 OID 16667)
-- Name: carrinho carrinho_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho
    ADD CONSTRAINT carrinho_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id);


--
-- TOC entry 4675 (class 2606 OID 16686)
-- Name: pedido pedido_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id);


-- Completed on 2024-06-27 08:50:28

--
-- PostgreSQL database dump complete
--

