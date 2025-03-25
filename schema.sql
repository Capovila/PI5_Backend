create table Professores(
    ra_professor int not null primary key,
    email text not null,
    senha text not null,
    is_admin boolean not null,
    is_liberado boolean not null
);


CREATE TABLE Disciplinas(
    id_disciplina mediumint not null auto_increment primary key,
    nome text not null,
    descricao text not null,
    area_relacionada text not null,
    ra_professor int not null,
    CONSTRAINT fk_ra_professor FOREIGN KEY (ra_professor) REFERENCES Professores(ra_professor)
);


CREATE TABLE Turmas ( 
    id_turma mediumint not null auto_increment primary key,
    data_inicio date,
    semestre int,
    isGraduated boolean
   
);

CREATE TABLE Alunos (
    ra_aluno INT NOT NULL PRIMARY KEY,
    nome text not null,
    id_turma mediumint not null,  
    CONSTRAINT fk_id_turma FOREIGN KEY (id_turma) REFERENCES Turmas(id_turma)
);


create table Notas (
    id_notas mediumint not null auto_increment primary key,
     ra_aluno int not null,
     constraint fk_ra_aluno foreign key (ra_aluno) references Alunos(ra_aluno),
     id_disciplina mediumint not null,
     constraint fk_id_disciplina foreign key (id_disciplina) references Disciplinas(id_disciplina),
     nota float not null,
     semestre int not null
);

create table Turma_Disciplina(
    id_turma_disciplina mediumint not null auto_increment primary key,
    id_turma mediumint not null, 
    CONSTRAINT fk_id_turma_disciplina FOREIGN KEY (id_turma) REFERENCES Turmas(id_turma),
    id_disciplina mediumint not null,
    constraint fk_id_disciplina_turma foreign key (id_disciplina) references Disciplinas(id_disciplina),
    semestre int not null,
    taxa_aprovacao float not null
);

--############################################################################################################################
--DADOS PARA TESTE
--############################################################################################################################

-- Inserindo Professores
INSERT INTO Professores (ra_professor, email, senha, is_admin, is_liberado) VALUES
(101, 'prof1@email.com', 'senha123', true, true),
(102, 'prof2@email.com', 'senha456', false, true),
(103, 'prof3@email.com', 'senha789', false, false),
(104, 'prof4@email.com', 'senhaabc', false, true),
(105, 'prof5@email.com', 'senhadef', true, true);

-- Inserindo Disciplinas
INSERT INTO Disciplinas (nome, descricao, area_relacionada, ra_professor) VALUES
('Matemática', 'Cálculo diferencial e integral', 'Exatas', 101),
('História', 'História do Brasil e Geral', 'Humanas', 102),
('Programação', 'Lógica e desenvolvimento em Python', 'Tecnologia', 103),
('Física', 'Mecânica Clássica e Termodinâmica', 'Exatas', 104),
('Química', 'Composição e transformação das substâncias', 'Exatas', 105);

-- Inserindo Turmas
INSERT INTO Turmas (data_inicio, semestre, isGraduated) VALUES
('2024-02-01', 1, false),
('2024-02-01', 2, false),
('2023-08-01', 3, true),
('2023-08-01', 4, true),
('2022-03-01', 5, true);

-- Inserindo Alunos
INSERT INTO Alunos (ra_aluno, nome, id_turma) VALUES
(2023001, 'Ana Silva', 1),
(2023002, 'Carlos Mendes', 2),
(2023003, 'Fernanda Rocha', 3),
(2023004, 'João Pereira', 4),
(2023005, 'Mariana Santos', 5);

-- Inserindo Notas
INSERT INTO Notas (ra_aluno, id_disciplina, nota, semestre) VALUES
(2023001, 1, 8.5, 1),
(2023002, 2, 7.0, 2),
(2023003, 3, 9.2, 3),
(2023004, 4, 6.8, 4),
(2023005, 5, 7.5, 5);

-- Inserindo Turma_Disciplina
INSERT INTO Turma_Disciplina (id_turma, id_disciplina, semestre, taxa_aprovacao) VALUES
(1, 1, 1, 85.5),
(2, 2, 2, 75.0),
(3, 3, 3, 90.2),
(4, 4, 4, 80.0),
(5, 5, 5, 88.4);


