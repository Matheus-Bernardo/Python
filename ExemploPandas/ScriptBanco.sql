drop database Apartamento;
create database Apartamento;
use Apartamento;

CREATE TABLE apartamento(
	codigo_Apartamento INT NOT NULL PRIMARY KEY ,
	cidade varchar(60) ,
    metros_quadrados tinyint(30),
    quartos tinyint not null,
    banheiro tinyint not null,
    estacionamento tinyint not null,
    animais varchar(15),
	valor_aluguel float not null,
    valor_iptu float not null,
    valor_seguranca float not null,
    total_compras float);
    
DELIMITER //

CREATE TRIGGER calcular_total_compras_before_insert
BEFORE INSERT ON apartamento
FOR EACH ROW
BEGIN
    SET NEW.total_compras = NEW.valor_aluguel + NEW.valor_iptu + NEW.valor_seguranca;
END;

//

CREATE TRIGGER calcular_total_compras_before_update
BEFORE UPDATE ON apartamento
FOR EACH ROW
BEGIN
    SET NEW.total_compras = NEW.valor_aluguel + NEW.valor_iptu + NEW.valor_seguranca;
END;
//
DELIMITER ;


