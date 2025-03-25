CREATE TABLE Turmas ( 
    id_turma mediumint not null auto_increment primary key,
    data_inicio date,
    semestre int
);

CREATE TABLE Alunos (
    ra_aluno INT NOT NULL PRIMARY KEY,
    nome text not null,
    id_turma mediumint not null,  
    CONSTRAINT fk_id_turma FOREIGN KEY (id_turma) REFERENCES Turmas(id_turma)
);

CREATE TABLE Disciplinas(
    id_disciplina mediumint not null auto_increment primary key,
    nome text not null,
    descricao text not null,
    area_relacionada text not null
);

create table Notas (
     ra_aluno mediumint not null,
     constraint fk_id_disciplina foreign key (id_disciplina) references Disciplinas(id_disciplina)
     id_disciplina mediumint not null,
     constraint fk_id_disciplina foreign key (id_disciplina) references Disciplinas(id_disciplina)
)
