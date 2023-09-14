CREATE DATABASE IF NOT EXISTS DBCondo;
USE DBCondo;

-- DROP TABLES IF THEY EXIST
DROP TABLE IF EXISTS comunicados_anexos;
DROP TABLE IF EXISTS comunicados;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS perfis;

-- CREATE TABLES IF THEY DO NOT EXIST
CREATE TABLE IF NOT EXISTS perfis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    perfil VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    apartamento VARCHAR(255) NOT NULL,
    bloco VARCHAR(255) NOT NULL,
    telefone VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    perfil_id INT,
    FOREIGN KEY (perfil_id) REFERENCES perfis(id)
);

CREATE TABLE IF NOT EXISTS comunicados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    idsanexos TEXT NOT NULL,
    data_insercao DATETIME DEFAULT CURRENT_TIMESTAMP,
    excluido BIT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS comunicados_anexos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    anexos_bs64 TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS notificacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo_mensagem VARCHAR(255) NOT NULL,
    texto_mensagem VARCHAR(255) NOT NULL,
    telefone VARCHAR(13) NOT NULL,  
    token VARCHAR(13) NOT NULL,
    usuario_id INT NOT NULL,
    usuario_criador_id INT NOT NULL DEFAULT 0, -- Alterar posteriormente para utilizar o id do usuário que fez o insert
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
	data_envio DATETIME DEFAULT CURRENT_TIMESTAMP,    
    sucesso BIT DEFAULT 0
    /*,FOREIGN KEY (usuario_id) REFERENCES clientes(id)*/
    -- Adicionar posteriormente foreign key do usuário que fez o insert e usuário destino
);


-- Inserções de perfis
INSERT INTO perfis (perfil, descricao) VALUES ('Administrador', 'Perfil com acesso administrativo ao sistema.');
INSERT INTO perfis (perfil, descricao) VALUES ('Síndico', 'Perfil para os síndicos do condomínio.');
INSERT INTO perfis (perfil, descricao) VALUES ('Porteiro', 'Perfil para os porteiros do condomínio.');
INSERT INTO perfis (perfil, descricao) VALUES ('Morador', 'Perfil para os moradores do condomínio.');

-- SELECT FROM TABLES
SELECT * FROM perfis;
SELECT * FROM clientes;
SELECT * FROM comunicados;
SELECT * FROM comunicados_anexos;

SELECT count(id) FROM clientes WHERE usuario='alexsander2' or apartamento='195' or email='alexsandersf125@gmail.com'