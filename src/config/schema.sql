    create table Professores(
        ra_professor int not null primary key,
        nome text not null,
        email text not null,
        senha text not null,
        is_admin boolean not null,
        is_liberado boolean not null
    );

    CREATE TABLE Turmas ( 
        id_turma mediumint not null auto_increment primary key,
        data_inicio date,
        isGraduated boolean
    );

    CREATE TABLE Disciplinas(
        id_disciplina mediumint not null auto_increment primary key,
        nome text not null,
        descricao text not null,
        semestre int not null,
        area_relacionada text not null,
        ra_professor int not null,
        CONSTRAINT fk_ra_professor FOREIGN KEY (ra_professor) REFERENCES Professores(ra_professor)
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
        nota float not null
    );

    create table Turma_Disciplina(
        id_turma_disciplina mediumint not null auto_increment primary key,
        id_turma mediumint not null, 
        CONSTRAINT fk_id_turma_disciplina FOREIGN KEY (id_turma) REFERENCES Turmas(id_turma),
        id_disciplina mediumint not null,
        constraint fk_id_disciplina_turma foreign key (id_disciplina) references Disciplinas(id_disciplina),
        isConcluida boolean not null,
        taxa_aprovacao float
    );

    --############################################################################################################################
    --DADOS PARA TESTE
    --############################################################################################################################

-- Inserindo Professores
INSERT INTO Professores (ra_professor, nome, email, senha, is_admin, is_liberado) VALUES
(101, 'Roberto Silva', 'prof1@email.com', 'senha123', true, true),
(102, 'Carlos Almeida', 'prof2@email.com', 'senha456', false, true),
(103, 'Sandra Hahn', 'prof3@email.com', 'senha789', false, false),
(104, 'Johnatan Machado', 'prof4@email.com', 'senhaabc', false, true),
(105, 'Larissa Lima', 'prof5@email.com', 'senhadef', true, true);


-- Inserindo Turmas
INSERT INTO Turmas (data_inicio, isGraduated) VALUES
('2024-02-01', false),
('2024-02-01', false),
('2023-08-01', true),
('2023-08-01', true),
('2022-03-01', true);

-- Inserindo Disciplinas
INSERT INTO Disciplinas (nome, descricao, semestre, area_relacionada, ra_professor) VALUES
('Matemática', 'Cálculo diferencial e integral', 1, 'Exatas', 101),
('História', 'História do Brasil e Geral', 1, 'Humanas', 102),
('Programação', 'Lógica e desenvolvimento em Python', 2, 'Tecnologia', 103),
('Física', 'Mecânica Clássica e Termodinâmica', 2, 'Exatas', 104),
('Química', 'Composição e transformação das substâncias', 3, 'Exatas', 105);

-- Inserindo Alunos
INSERT INTO Alunos (ra_aluno, nome, id_turma) VALUES
(2023001, 'Ana Silva', 1),
(2023002, 'Carlos Mendes', 2),
(2023003, 'Fernanda Rocha', 3),
(2023004, 'João Pereira', 4),
(2023005, 'Mariana Santos', 5);

-- Inserindo Notas
INSERT INTO Notas (ra_aluno, id_disciplina, nota) VALUES
(2023001, 1, 8.5),  -- Ana Silva, Matemática
(2023002, 2, 7.0),  -- Carlos Mendes, História
(2023003, 3, 9.2),  -- Fernanda Rocha, Programação
(2023004, 4, 6.8),  -- João Pereira, Física
(2023005, 5, 7.5);  -- Mariana Santos, Química

-- Inserindo Turma_Disciplina
INSERT INTO Turma_Disciplina (id_turma, id_disciplina, taxa_aprovacao, isConcluida) VALUES
(1, 1, 85.5, false),  -- Turma 1, Matemática
(2, 2, 75.0, false),  -- Turma 2, História
(3, 3, 90.2, false),  -- Turma 3, Programação
(4, 4, 80.0, false),  -- Turma 4, Física
(5, 5, 88.4, false);  -- Turma 5, Química

