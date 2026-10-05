DROP DATABASE IF EXISTS oficina_carros;

CREATE DATABASE oficina_carros;

USE oficina_carros;

ALTER TABLE clientes
MODIFY COLUMN data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;


SHOW TABLES;

-- =========================================================
-- 1. TABELAS
-- =========================================================

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    data_cadastro DATE NOT NULL
);


CREATE TABLE veiculos (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    placa VARCHAR(7) NOT NULL UNIQUE,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    ano INT NOT NULL,

    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),

    CHECK (ano BETWEEN 1950 AND 2100)
);


CREATE TABLE mecanicos (
    id_mecanico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    especialidade VARCHAR(100) NOT NULL,
    data_contratacao DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ATIVO'
);


CREATE TABLE servicos (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao VARCHAR(255),
    preco DECIMAL(10,2) NOT NULL,
    tempo_estimado INT NOT NULL DEFAULT 60,
    status VARCHAR(20) NOT NULL DEFAULT 'ATIVO'
);


CREATE TABLE ordens_servico (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_veiculo INT NOT NULL,
    id_mecanico INT NOT NULL,
    data_abertura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_fechamento DATETIME,
    status VARCHAR(30) NOT NULL DEFAULT 'ABERTA',
    observacoes VARCHAR(255),

    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),

    FOREIGN KEY (id_veiculo)
        REFERENCES veiculos(id_veiculo),

    FOREIGN KEY (id_mecanico)
        REFERENCES mecanicos(id_mecanico)
);


CREATE TABLE itens_servico (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
    id_servico INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 1,
    preco_unitario DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (id_ordem)
        REFERENCES ordens_servico(id_ordem),

    FOREIGN KEY (id_servico)
        REFERENCES servicos(id_servico)
);


CREATE TABLE historico (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
    acao VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    data_alteracao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_ordem)
        REFERENCES ordens_servico(id_ordem)
);


CREATE TABLE historico_precos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_servico INT NOT NULL,
    preco_anterior DECIMAL(10,2) NOT NULL,
    preco_novo DECIMAL(10,2) NOT NULL,
    data_alteracao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_servico)
        REFERENCES servicos(id_servico)
);


CREATE TABLE historico_status_ordem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
    status_anterior VARCHAR(30) NOT NULL,
    novo_status VARCHAR(30) NOT NULL,
    data_alteracao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_ordem)
        REFERENCES ordens_servico(id_ordem)
);


-- =========================================================
-- 2. DADOS
-- =========================================================

INSERT INTO clientes
(nome, cpf, email, data_cadastro)
VALUES
('João da Silva','11111111111','joao@email.com','2026-01-10'),
('Maria Souza','22222222222','maria@email.com','2026-01-12'),
('Carlos Oliveira','33333333333','carlos@email.com','2026-01-15'),
('Ana Pereira','44444444444','ana@email.com','2026-01-18'),
('Pedro Santos','55555555555','pedro@email.com','2026-01-20'),
('Lucas Rodrigues','66666666666','lucas@email.com','2026-01-22'),
('Fernanda Costa','77777777777','fernanda@email.com','2026-01-25'),
('Rafael Martins','88888888888','rafael@email.com','2026-01-28'),
('Gabriel Almeida','99999999999','gabriel@email.com','2026-02-01'),
('Juliana Lima','12345678900','juliana@email.com','2026-02-03');


INSERT INTO veiculos
(id_cliente, placa, marca, modelo, ano)
VALUES
(1,'ABC1D23','Volkswagen','Gol',2018),
(2,'DEF2E34','Chevrolet','Onix',2020),
(3,'GHI3F45','Fiat','Uno',2017),
(4,'JKL4G56','Ford','Ka',2019),
(5,'MNO5H67','Toyota','Corolla',2021),
(6,'PQR6I78','Honda','Civic',2020),
(7,'STU7J89','Hyundai','HB20',2022),
(8,'VWX8K90','Renault','Sandero',2018),
(9,'YZA9L01','Fiat','Argo',2021),
(10,'BCD0M12','Chevrolet','Tracker',2023),
(1,'EFG1N23','Ford','Fiesta',2016),
(2,'HIJ2O34','Volkswagen','Polo',2022);


INSERT INTO mecanicos
(nome, cpf, especialidade, data_contratacao)
VALUES
('Carlos Mendes','11111111111','Motor','2023-02-10'),
('Joao Silva','22222222222','Freios','2022-08-15'),
('Marcos Oliveira','33333333333','Suspensao','2024-01-20'),
('Rafael Souza','44444444444','Eletrica','2021-05-12'),
('Lucas Pereira','55555555555','Injecao Eletronica','2023-11-05');


INSERT INTO servicos
(nome, descricao, preco, tempo_estimado)
VALUES
('Troca de oleo','Troca do oleo do motor',150.00,60),
('Troca de pastilhas','Troca das pastilhas de freio',280.00,90),
('Alinhamento','Alinhamento das rodas',120.00,60),
('Balanceamento','Balanceamento das rodas',100.00,45),
('Revisao do motor','Revisao completa do motor',800.00,240),
('Troca de bateria','Substituicao da bateria',450.00,60),
('Suspensao','Manutencao da suspensao',650.00,180),
('Diagnostico eletronico','Analise eletronica',200.00,60),
('Troca de embreagem','Troca do kit de embreagem',1200.00,300),
('Troca de correia','Troca da correia dentada',700.00,180);


INSERT INTO ordens_servico
(id_cliente, id_veiculo, id_mecanico, data_abertura, status, observacoes)
VALUES
(1,1,1,'2026-03-01 08:00:00','ABERTA','Revisao geral'),
(2,2,2,'2026-03-02 09:00:00','EM_ANDAMENTO','Problema no freio'),
(3,3,3,'2026-03-03 10:00:00','CONCLUIDA','Problema na suspensao'),
(4,4,4,'2026-03-04 08:30:00','CONCLUIDA','Falha eletrica'),
(5,5,1,'2026-03-05 09:30:00','ABERTA','Revisao do motor'),
(6,6,2,'2026-03-06 10:00:00','EM_ANDAMENTO','Troca de pastilhas'),
(7,7,3,'2026-03-07 11:00:00','CONCLUIDA','Alinhamento'),
(8,8,4,'2026-03-08 08:00:00','ABERTA','Diagnostico'),
(9,9,5,'2026-03-09 09:00:00','EM_ANDAMENTO','Problema na injecao'),
(10,10,1,'2026-03-10 10:00:00','CONCLUIDA','Troca de correia');


INSERT INTO itens_servico
(id_ordem, id_servico, quantidade, preco_unitario)
VALUES
(1,1,1,150.00),
(1,3,1,120.00),
(2,2,1,280.00),
(3,7,1,650.00),
(4,8,1,200.00),
(5,5,1,800.00),
(5,1,1,150.00),
(6,2,1,280.00),
(7,3,1,120.00),
(7,4,1,100.00),
(8,8,1,200.00),
(9,8,1,200.00),
(10,10,1,700.00);


-- =========================================================
-- 3. CONSULTAS
-- =========================================================

-- WHERE

SELECT *
FROM servicos
WHERE preco > 500;


-- ORDER BY + LIMIT

SELECT *
FROM servicos
ORDER BY preco DESC
LIMIT 5;


-- LIKE

SELECT *
FROM clientes
WHERE nome LIKE '%Silva%';


-- BETWEEN

SELECT *
FROM servicos
WHERE preco BETWEEN 100 AND 500;


-- IN

SELECT *
FROM ordens_servico
WHERE status IN ('ABERTA','EM_ANDAMENTO');


-- AND

SELECT *
FROM servicos
WHERE preco > 200
AND status = 'ATIVO';


-- OR

SELECT *
FROM ordens_servico
WHERE status = 'ABERTA'
OR status = 'EM_ANDAMENTO';


-- =========================================================
-- 4. FUNÇÕES DE AGREGAÇÃO
-- =========================================================

SELECT COUNT(*) AS total_clientes
FROM clientes;


SELECT SUM(preco) AS soma_servicos
FROM servicos;


SELECT AVG(preco) AS preco_medio
FROM servicos;


SELECT MIN(preco) AS menor_preco
FROM servicos;


SELECT MAX(preco) AS maior_preco
FROM servicos;


-- =========================================================
-- 5. GROUP BY + HAVING
-- =========================================================

SELECT
    status,
    COUNT(*) AS quantidade
FROM ordens_servico
GROUP BY status;


SELECT
    status,
    COUNT(*) AS quantidade
FROM ordens_servico
GROUP BY status
HAVING COUNT(*) > 2;


-- =========================================================
-- 6. JOINS
-- =========================================================

SELECT
    c.nome AS cliente,
    v.modelo,
    v.placa
FROM clientes c
INNER JOIN veiculos v
    ON c.id_cliente = v.id_cliente;


SELECT
    os.id_ordem,
    c.nome AS cliente,
    v.modelo AS veiculo,
    m.nome AS mecanico,
    os.status
FROM ordens_servico os
INNER JOIN clientes c
    ON os.id_cliente = c.id_cliente
INNER JOIN veiculos v
    ON os.id_veiculo = v.id_veiculo
INNER JOIN mecanicos m
    ON os.id_mecanico = m.id_mecanico;


SELECT
    os.id_ordem,
    s.nome AS servico,
    i.quantidade,
    i.preco_unitario,
    i.quantidade * i.preco_unitario AS total
FROM itens_servico i
INNER JOIN ordens_servico os
    ON i.id_ordem = os.id_ordem
INNER JOIN servicos s
    ON i.id_servico = s.id_servico;


-- =========================================================
-- CONSULTAS DE CLIENTES E VEÍCULOS
-- =========================================================

SELECT *
FROM clientes
ORDER BY nome;


SELECT *
FROM clientes
WHERE nome LIKE 'A%'
ORDER BY nome;


SELECT *
FROM clientes
WHERE nome LIKE '%a%'
ORDER BY nome;


SELECT
    c.nome,
    v.placa,
    v.marca,
    v.modelo,
    v.ano
FROM clientes c
INNER JOIN veiculos v
    ON c.id_cliente = v.id_cliente
WHERE c.id_cliente = 1;


SELECT *
FROM veiculos
WHERE marca = 'Toyota'
OR marca = 'Volkswagen'
ORDER BY marca;


SELECT *
FROM veiculos
WHERE ano BETWEEN 2019 AND 2022
ORDER BY ano;


SELECT *
FROM veiculos
ORDER BY ano DESC
LIMIT 5;


SELECT
    c.nome AS cliente,
    COUNT(v.id_veiculo) AS quantidade_veiculos
FROM clientes c
LEFT JOIN veiculos v
    ON c.id_cliente = v.id_cliente
GROUP BY c.id_cliente, c.nome
ORDER BY quantidade_veiculos DESC;


SELECT
    c.nome AS cliente,
    COUNT(v.id_veiculo) AS quantidade_veiculos
FROM clientes c
INNER JOIN veiculos v
    ON c.id_cliente = v.id_cliente
GROUP BY c.id_cliente, c.nome
HAVING COUNT(v.id_veiculo) > 1
ORDER BY quantidade_veiculos DESC;


-- =========================================================
-- 7. SUBCONSULTAS
-- =========================================================

-- Serviços acima da média

SELECT
    nome,
    preco
FROM servicos
WHERE preco > (
    SELECT AVG(preco)
    FROM servicos
);


-- Mecânicos que possuem ordens

SELECT
    nome
FROM mecanicos
WHERE id_mecanico IN (
    SELECT id_mecanico
    FROM ordens_servico
);


-- Veículos que possuem ordens

SELECT
    placa,
    modelo
FROM veiculos
WHERE id_veiculo IN (
    SELECT id_veiculo
    FROM ordens_servico
);


-- =========================================================
-- SUBCONSULTAS ADICIONAIS
-- =========================================================

SELECT
    nome,
    preco
FROM servicos
WHERE preco = (
    SELECT MAX(preco)
    FROM servicos
);


SELECT
    nome
FROM clientes
WHERE id_cliente IN (
    SELECT id_cliente
    FROM veiculos
);


-- =========================================================
-- 8. PROCEDURES
-- =========================================================

DELIMITER $$


CREATE PROCEDURE cadastrar_cliente(
    IN p_nome VARCHAR(100),
    IN p_cpf VARCHAR(11),
    IN p_email VARCHAR(100)
)
BEGIN

    INSERT INTO clientes
    (
        nome,
        cpf,
        email,
        data_cadastro
    )
    VALUES
    (
        p_nome,
        p_cpf,
        p_email,
        CURDATE()
    );

END $$


CREATE PROCEDURE cadastrar_servico(
    IN p_nome VARCHAR(100),
    IN p_descricao VARCHAR(255),
    IN p_preco DECIMAL(10,2),
    IN p_tempo INT
)
BEGIN

    INSERT INTO servicos
    (
        nome,
        descricao,
        preco,
        tempo_estimado
    )
    VALUES
    (
        p_nome,
        p_descricao,
        p_preco,
        p_tempo
    );

END $$


CREATE PROCEDURE alterar_preco(
    IN p_id INT,
    IN p_preco DECIMAL(10,2)
)
BEGIN

    UPDATE servicos
    SET preco = p_preco
    WHERE id_servico = p_id;

END $$


CREATE PROCEDURE listar_ordens()
BEGIN

    SELECT
        os.id_ordem,
        c.nome AS cliente,
        v.modelo AS veiculo,
        m.nome AS mecanico,
        os.status
    FROM ordens_servico os
    INNER JOIN clientes c
        ON os.id_cliente = c.id_cliente
    INNER JOIN veiculos v
        ON os.id_veiculo = v.id_veiculo
    INNER JOIN mecanicos m
        ON os.id_mecanico = m.id_mecanico;

END $$


-- Procedure para cadastrar veículo

CREATE PROCEDURE cadastrar_veiculo(
    IN p_id_cliente INT,
    IN p_marca VARCHAR(50),
    IN p_modelo VARCHAR(50),
    IN p_placa VARCHAR(10),
    IN p_ano INT
)
BEGIN

    IF NOT EXISTS (
        SELECT 1
        FROM clientes
        WHERE id_cliente = p_id_cliente
    ) THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cliente não encontrado';

    END IF;


    IF p_ano < 1900 OR p_ano > 2100 THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ano do veículo inválido';

    END IF;


    INSERT INTO veiculos
    (
        id_cliente,
        marca,
        modelo,
        placa,
        ano
    )
    VALUES
    (
        p_id_cliente,
        p_marca,
        p_modelo,
        p_placa,
        p_ano
    );

END $$


DELIMITER ;


-- =========================================================
-- 9. TRIGGERS
-- =========================================================

DELIMITER $$


CREATE TRIGGER registrar_nova_ordem
AFTER INSERT ON ordens_servico
FOR EACH ROW
BEGIN

    INSERT INTO historico
    (
        id_ordem,
        acao,
        descricao
    )
    VALUES
    (
        NEW.id_ordem,
        'CRIACAO',
        'Nova ordem de servico criada'
    );

END $$


CREATE TRIGGER registrar_status
AFTER UPDATE ON ordens_servico
FOR EACH ROW
BEGIN

    IF OLD.status <> NEW.status THEN

        INSERT INTO historico
        (
            id_ordem,
            acao,
            descricao
        )
        VALUES
        (
            NEW.id_ordem,
            'ALTERACAO',
            CONCAT(
                'Status alterado de ',
                OLD.status,
                ' para ',
                NEW.status
            )
        );

    END IF;

END $$


CREATE TRIGGER registrar_servico
AFTER INSERT ON itens_servico
FOR EACH ROW
BEGIN

    INSERT INTO historico
    (
        id_ordem,
        acao,
        descricao
    )
    VALUES
    (
        NEW.id_ordem,
        'SERVICO',
        'Servico adicionado a ordem'
    );

END $$


-- Trigger para histórico de alteração de preço

CREATE TRIGGER registrar_alteracao_preco
AFTER UPDATE ON servicos
FOR EACH ROW
BEGIN

    IF OLD.preco <> NEW.preco THEN

        INSERT INTO historico_precos
        (
            id_servico,
            preco_anterior,
            preco_novo,
            data_alteracao
        )
        VALUES
        (
            OLD.id_servico,
            OLD.preco,
            NEW.preco,
            NOW()
        );

    END IF;

END $$


DELIMITER ;


-- =========================================================
-- 10. TESTES
-- =========================================================

CALL cadastrar_cliente(
    'Cliente Teste',
    '98765432100',
    'teste@email.com'
);


CALL cadastrar_servico(
    'Troca de filtro',
    'Troca do filtro de ar',
    90.00,
    30
);


CALL alterar_preco(1,160.00);


CALL listar_ordens();


-- Teste do trigger

UPDATE ordens_servico
SET status = 'CONCLUIDA'
WHERE id_ordem = 1;


SELECT *
FROM historico;


-- Teste do histórico de preço

UPDATE servicos
SET preco = 700.00
WHERE id_servico = 1;


SELECT *
FROM historico_precos;


-- =========================================================
-- VALOR TOTAL DE CADA ORDEM
-- =========================================================

SELECT
    os.id_ordem,
    c.nome AS cliente,
    SUM(i.quantidade * i.preco_unitario) AS valor_total
FROM ordens_servico os
INNER JOIN clientes c
    ON os.id_cliente = c.id_cliente
INNER JOIN itens_servico i
    ON os.id_ordem = i.id_ordem
GROUP BY os.id_ordem, c.nome
ORDER BY valor_total DESC;


-- =========================================================
-- TESTES DE INTEGRIDADE
-- =========================================================

-- Cliente válido

INSERT INTO clientes
(
    nome,
    cpf,
    telefone
)
VALUES
(
    'Cliente Teste 2',
    '22233344455',
    '48988887777'
);


-- Veículo com cliente inexistente
-- Este comando deve apresentar erro de FOREIGN KEY

INSERT INTO veiculos
(
    id_cliente,
    marca,
    modelo,
    placa,
    ano
)
VALUES
(
    9999,
    'Fiat',
    'Uno',
    'ZZZ9Z99',
    2022
);


-- Serviço com preço negativo
-- A estrutura atual não possui CHECK para preço.
-- O comando é mantido como teste.

INSERT INTO servicos
(
    nome,
    descricao,
    preco
)
VALUES
(
    'Serviço inválido',
    'Teste de preço negativo',
    -500.00
);


-- Exclusão de cliente
-- Este comando pode apresentar erro caso o cliente
-- possua veículos ou ordens relacionadas.

DELETE FROM clientes
WHERE id_cliente = 1;


-- Ordem com veículo inexistente
-- Este comando deve apresentar erro de FOREIGN KEY

INSERT INTO ordens_servico
(
    id_cliente,
    id_veiculo,
    id_mecanico,
    status
)
VALUES
(
    9999,
    9999,
    1,
    'ABERTA'
);


-- =========================================================
-- CONSULTAS FINAIS
-- =========================================================

SELECT *
FROM clientes;


SELECT *
FROM veiculos;


SELECT *
FROM mecanicos;


SELECT *
FROM servicos;


SELECT *
FROM ordens_servico;


SELECT *
FROM itens_servico;


SELECT *
FROM historico;