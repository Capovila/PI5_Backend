import { pool } from "../config/config.js";

//GET
export async function getTurmaDisciplina() {
  const [rows] = await pool.query(`SELECT * FROM Turma_Disciplina`);
  return rows;
}

export async function getTurmasDisciplinaById(id) {
  const [rows] = await pool.query(
    `SELECT * FROM Turma_Disciplina WHERE id_turma_disciplina= ?`,
    [id]
  );
  return rows;
}

//todas as turmas que fazem a disciplina x
export async function getTurmasByDisciplinaId(id) {
  const [rows] = await pool.query(
    `SELECT * FROM Turma_Disciplina WHERE id_disciplina = ?`,
    [id]
  );
  return rows;
}

//todas as disciplinas da turma x
export async function getDisciplinaByTurmaId(id) {
  const [rows] = await pool.query(
    `SELECT * FROM Turma_Disciplina WHERE id_turma = ?`,
    [id]
  );
  return rows;
}

//POST
export async function addTurmaDisciplina(
  id_turma,
  id_disciplina,
  taxa_aprovacao,
  isConcluida
) {
  const response = await pool.query(
    `INSERT INTO Turma_Disciplina (id_turma, id_disciplina, taxa_aprovacao, isConcluida) VALUES (?,?,?,?)`,
    [id_turma, id_disciplina, taxa_aprovacao, isConcluida]
  );

  return response;
}

//DELETE
export async function deleteTurmaDisciplina(id) {
  const [rows] = await pool.query(
    `DELETE  FROM Turma_Disciplina WHERE id_turma_disciplina= ?`,
    [id]
  );
  return rows;
}

//PATCH
export async function patchTurmaDisciplina(
  id_turma,
  id_disciplina,
  taxa_aprovacao,
  isConcluida,
  id
) {
  const response = await pool.query(
    `UPDATE Turma_Disciplina SET id_turma=?, id_disciplina=?, taxa_aprovacao=?, isConcluida=? WHERE id_turma_disciplina=?`,
    [id_turma, id_disciplina, taxa_aprovacao, isConcluida, id]
  );

  return response;
}
