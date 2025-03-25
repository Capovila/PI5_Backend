import { pool } from "../config/config.js";

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
