CREATE DATABASE oficina;

USE oficina;

-- MECÂNICOS
CREATE TABLE mecanicos (
    id_mecanico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    especialidade VARCHAR(100) NOT NULL,
    data_contratacao DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ATIVO'
);

-- SERVIÇOS
CREATE TABLE servicos (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao VARCHAR(255),
    preco DECIMAL(10,2) NOT NULL,
    tempo_estimado INT NOT NULL DEFAULT 60,
    status VARCHAR(20) NOT NULL DEFAULT 'ATIVO',

    CHECK (preco >= 0),
    CHECK (tempo_estimado > 0)
);
INSERT INTO mecanicos
(nome, cpf, especialidade, data_contratacao)
VALUES
('Carlos Mendes', '11111111111', 'Motor', '2023-02-10'),
('Joao Silva', '22222222222', 'Freios', '2022-08-15'),
('Marcos Oliveira', '33333333333', 'Suspensao', '2024-01-20'),
('Rafael Souza', '44444444444', 'Eletrica', '2021-05-12'),
('Lucas Pereira', '55555555555', 'Injecao Eletronica', '2023-11-05');


-- pip install mysql-connector-python