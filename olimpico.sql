--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-06-25 22:19:32

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
-- TOC entry 222 (class 1259 OID 16594)
-- Name: carrinho; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.carrinho (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    nome_produto character varying(200),
    imagem_produto character varying(200),
    produto_id integer NOT NULL,
    quantidade integer,
    observacao text,
    preco_total numeric(10,2)
);


ALTER TABLE public.carrinho OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16593)
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
-- TOC entry 224 (class 1259 OID 16613)
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
-- TOC entry 223 (class 1259 OID 16612)
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
-- TOC entry 220 (class 1259 OID 16585)
-- Name: produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produto (
    id integer NOT NULL,
    nome_produto character varying(200),
    tipo_produto character varying(200),
    tamanho character varying(200),
    ingrediente character varying(200),
    preco numeric(10,2),
    descricao text,
    imagem character varying(250)
);


ALTER TABLE public.produto OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16584)
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
-- TOC entry 216 (class 1259 OID 16563)
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
-- TOC entry 215 (class 1259 OID 16562)
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
-- TOC entry 218 (class 1259 OID 16574)
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
-- TOC entry 217 (class 1259 OID 16573)
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
-- TOC entry 4657 (class 2604 OID 16597)
-- Name: carrinho id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho ALTER COLUMN id SET DEFAULT nextval('public.carrinho_id_seq'::regclass);


--
-- TOC entry 4658 (class 2604 OID 16616)
-- Name: pedido id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido ALTER COLUMN id SET DEFAULT nextval('public.pedido_id_seq'::regclass);


--
-- TOC entry 4656 (class 2604 OID 16588)
-- Name: produto id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto ALTER COLUMN id SET DEFAULT nextval('public.produto_id_seq'::regclass);


--
-- TOC entry 4654 (class 2604 OID 16566)
-- Name: usuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_seq'::regclass);


--
-- TOC entry 4655 (class 2604 OID 16577)
-- Name: usuarioadmin id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarioadmin ALTER COLUMN id SET DEFAULT nextval('public.usuarioadmin_id_seq'::regclass);


--
-- TOC entry 4826 (class 0 OID 16594)
-- Dependencies: 222
-- Data for Name: carrinho; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.carrinho (id, usuario_id, nome_produto, imagem_produto, produto_id, quantidade, observacao, preco_total) FROM stdin;
21	2	X-Tudo Artesanal	xtudoartesanal.jpg	1	2	Vou querer sem molho por favor 	60.00
22	2	Duplo Bacon Brioche Cheddar 	Cheddar.jpg	3	1	Eu quero com bastante queijo	30.00
23	2	Batata Frita Maluca	batataG.jpeg	2	1	com pouca sal	38.00
44	3	Duplo Bacon Brioche Cheddar 	Cheddar.jpg	3	1	sa	30.00
\.


--
-- TOC entry 4828 (class 0 OID 16613)
-- Dependencies: 224
-- Data for Name: pedido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedido (id, usuario_id, data_pedido, forma_pagamento, endereco_entrega, status, valor_total, observacao, itens_comprados) FROM stdin;
1	3	2024-06-25 15:37:00.413844	CARTAO	Rua Um	PENDENTE	210.00	\N	Duplo Bacon Brioche Cheddar  - Quantidade: 1 - Observação: sas\nDuplo Bacon Brioche Cheddar  - Quantidade: 3 - Observação: sasa\nDuplo Bacon Brioche Cheddar  - Quantidade: 2 - Observação: 212\nDuplo Bacon Brioche Cheddar  - Quantidade: 1 - Observação: quero sem nada
2	3	2024-06-25 15:38:40.55249	CARTAO	Rua Um	PENDENTE	68.00	\N	Batata Frita Maluca - Quantidade: 1 - Observação: com pouco sal pf\nDuplo Bacon Brioche Cheddar  - Quantidade: 1 - Observação: com bastante molho 
3	3	2024-06-25 15:42:06.357223	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	PENDENTE	30.00	\N	Duplo Bacon Brioche Cheddar  - Quantidade: 1 - Observação: sasa
4	3	2024-06-25 15:50:06.887079	DINHEIRO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	PENDENTE	68.00	{}	Batata Frita Maluca - Quantidade: 1 \nX-Tudo Artesanal - Quantidade: 1 
5	3	2024-06-25 15:51:58.669969	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	PENDENTE	30.00		Duplo Bacon Brioche Cheddar  - Quantidade: 1 
6	3	2024-06-25 16:11:38.05043	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	PENDENTE	68.00	Batata Frita Maluca - Quantidade: 1 - Observação: quero com bastante batata\r\n\nDuplo Bacon Brioche Cheddar  - Quantidade: 1 - Observação: quero com bastante molho 	Batata Frita Maluca - Quantidade: 1\nDuplo Bacon Brioche Cheddar  - Quantidade: 1
7	3	2024-06-25 16:12:57.746188	DINHEIRO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	PENDENTE	30.00	Duplo Bacon Brioche Cheddar   - Observação: sas	Duplo Bacon Brioche Cheddar  - Quantidade: 1
8	1	2024-06-25 16:53:30.937861	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	PENDENTE	60.00	Duplo Bacon Brioche Cheddar   - Observação: Quero com bastante molho 	Duplo Bacon Brioche Cheddar  - Quantidade: 2
9	1	2024-06-25 19:52:03.808263	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	90.00	Duplo Bacon Brioche Cheddar   - Observação: sasa \n\nDuplo Bacon Brioche Cheddar   - Observação: asa \n\nDuplo Bacon Brioche Cheddar   - Observação: sas \n	Duplo Bacon Brioche Cheddar  - Quantidade: 1\n\nDuplo Bacon Brioche Cheddar  - Quantidade: 1\n\nDuplo Bacon Brioche Cheddar  - Quantidade: 1\n
10	1	2024-06-25 19:53:42.290104	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	128.00	X-Tudo Artesanal  - Observação: Quero Sem nada de molho \n\nDuplo Bacon Brioche Cheddar   - Observação: Um delicioso hamburguer \n\nBatata Frita Maluca  - Observação: quero textar  \n	X-Tudo Artesanal - Quantidade: 2\n\nDuplo Bacon Brioche Cheddar  - Quantidade: 1\n\nBatata Frita Maluca - Quantidade: 1\n
11	1	2024-06-25 19:54:22.219102	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	106.00	Batata Frita Maluca  - Observação: sasa \n\nX-Tudo Artesanal  - Observação: sasa \n	Batata Frita Maluca - Quantidade: 2\n\nX-Tudo Artesanal - Quantidade: 1\n
12	3	2024-06-25 20:06:37.11827	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	60.00	Duplo Bacon Brioche Cheddar   - Observação: sas \n	Duplo Bacon Brioche Cheddar  - Quantidade: 2\n
13	3	2024-06-25 20:08:04.938259	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	68.00	Duplo Bacon Brioche Cheddar   - Observação: sas \n\nBatata Frita Maluca  - Observação: sasas \n	Duplo Bacon Brioche Cheddar  - Quantidade: 1\n\nBatata Frita Maluca - Quantidade: 1\n
14	3	2024-06-25 20:12:50.279691	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	30.00	Duplo Bacon Brioche Cheddar   - Observação: sasa \n	Duplo Bacon Brioche Cheddar  - Quantidade: 1\n
15	3	2024-06-25 20:27:52.901647	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	76.00	Batata Frita Maluca  - Observação: sasa \n	Batata Frita Maluca - Quantidade: 2\n
16	3	2024-06-25 20:29:32.464685	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	98.00	Duplo Bacon Brioche Cheddar   - Observação: sasa \n\nBatata Frita Maluca  - Observação: sasa \n	Duplo Bacon Brioche Cheddar  - Quantidade: 2\n\nBatata Frita Maluca - Quantidade: 1\n
17	1	2024-06-25 20:45:40.826294	CARTAO	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	128.00	Duplo Bacon Brioche Cheddar   - Observação: sasa \n\nX-Tudo Artesanal  - Observação: sasa \n\nBatata Frita Maluca  - Observação: dsd \n	Duplo Bacon Brioche Cheddar  - Quantidade: 1\n\nX-Tudo Artesanal - Quantidade: 2\n\nBatata Frita Maluca - Quantidade: 1\n
18	1	2024-06-25 21:58:29.456107	PIX	Rua Um - 00 - Lote 31 Quadra 2  - Centra-Duque de Caxias - 21993432153	Preparando	30.00	Duplo Bacon Brioche Cheddar   - Observação: sasa \n	Duplo Bacon Brioche Cheddar  - Quantidade: 1\n
\.


--
-- TOC entry 4824 (class 0 OID 16585)
-- Dependencies: 220
-- Data for Name: produto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produto (id, nome_produto, tipo_produto, tamanho, ingrediente, preco, descricao, imagem) FROM stdin;
1	X-Tudo Artesanal	Artesanal	Hamburguer Artesanal	Bacon - Calabresa - Salada - Molho - 1 Carne - Ovo	30.00	Um hamburguer delicioso com uma blend feita diretamente na basa 	xtudoartesanal.jpg
2	Batata Frita Maluca	Porcao	Porcao Grande		38.00	Serve ate 5 pessoas	batataG.jpeg
3	Duplo Bacon Brioche Cheddar 	Artesanal	Hamburguer Artesanal	Bacon - Molho - 1 Carne - Cheddar	30.00	Um delicioso hamburguer	Cheddar.jpg
\.


--
-- TOC entry 4820 (class 0 OID 16563)
-- Dependencies: 216
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id, nome, sobrenome, telefone, email, senha, endereco, numero_casa, complemento, bairro, tipo_usuario) FROM stdin;
1	Marcos	MOREIRA	21993432153	lukas.silvalsm@gmail.com	102030	Rua Um	00	Lote 31 Quadra 2 	Centra-Duque de Caxias	Cliente
2	Marcos	Silva	21993432153	lukas.silvalsm@hotmail.com	102030	Rua Professor	00	63	Santa Lucia	Cliente
3	Larissa 	MOREIRA	21993432153	teste@teste.com	102030	Rua Um	00	Lote 31 Quadra 2 	Centra-Duque de Caxias	Cliente
\.


--
-- TOC entry 4822 (class 0 OID 16574)
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

SELECT pg_catalog.setval('public.carrinho_id_seq', 45, true);


--
-- TOC entry 4840 (class 0 OID 0)
-- Dependencies: 223
-- Name: pedido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pedido_id_seq', 18, true);


--
-- TOC entry 4841 (class 0 OID 0)
-- Dependencies: 219
-- Name: produto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produto_id_seq', 3, true);


--
-- TOC entry 4842 (class 0 OID 0)
-- Dependencies: 215
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_id_seq', 3, true);


--
-- TOC entry 4843 (class 0 OID 0)
-- Dependencies: 217
-- Name: usuarioadmin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarioadmin_id_seq', 1, true);


--
-- TOC entry 4670 (class 2606 OID 16601)
-- Name: carrinho carrinho_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho
    ADD CONSTRAINT carrinho_pkey PRIMARY KEY (id);


--
-- TOC entry 4672 (class 2606 OID 16620)
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (id);


--
-- TOC entry 4668 (class 2606 OID 16592)
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id);


--
-- TOC entry 4660 (class 2606 OID 16572)
-- Name: usuario usuario_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_email_key UNIQUE (email);


--
-- TOC entry 4662 (class 2606 OID 16570)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- TOC entry 4664 (class 2606 OID 16583)
-- Name: usuarioadmin usuarioadmin_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarioadmin
    ADD CONSTRAINT usuarioadmin_email_key UNIQUE (email);


--
-- TOC entry 4666 (class 2606 OID 16581)
-- Name: usuarioadmin usuarioadmin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarioadmin
    ADD CONSTRAINT usuarioadmin_pkey PRIMARY KEY (id);


--
-- TOC entry 4673 (class 2606 OID 16607)
-- Name: carrinho carrinho_produto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho
    ADD CONSTRAINT carrinho_produto_id_fkey FOREIGN KEY (produto_id) REFERENCES public.produto(id);


--
-- TOC entry 4674 (class 2606 OID 16602)
-- Name: carrinho carrinho_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrinho
    ADD CONSTRAINT carrinho_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id);


--
-- TOC entry 4675 (class 2606 OID 16621)
-- Name: pedido pedido_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id);


-- Completed on 2024-06-25 22:19:32

--
-- PostgreSQL database dump complete
--

