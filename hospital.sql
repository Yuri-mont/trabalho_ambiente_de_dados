CREATE TABLE pessoa (
    CPF  INT NOT NULL PRIMARY KEY,
    nome CHAR(200),
    sexo ENUM('M', 'F'),
    idade INT
);

CREATE TABLE Hospitais (
	cadastro INT NOT NULL PRIMARY KEY,
    CEP int,
    horario_func time
);
create table Doutores(
	CRM int not null primary key,
    nome char(200),
    especialiade char(50)
);
CREATE TABLE Atendimento(
    id INT PRIMARY KEY,
    CPF INT,
    CRM INT,
    cadastro INT,
    FOREIGN KEY (CPF) REFERENCES pessoa(CPF),
    FOREIGN KEY (CRM) REFERENCES Doutores(CRM),
    FOREIGN KEY (cadastro) REFERENCES Hospitais(cadastro)
);


