import { pool } from "../config/config.js";

//GET
export async function getNotas() {
  const [rows] = await pool.query(`SELECT * FROM Notas`);
  return rows;
}

export async function getNotasById(id) {
  const [rows] = await pool.query(`SELECT * FROM Notas WHERE id_notas = ?`, [
    id,
  ]);
  return rows;
}

//todas as notas da disciplina
export async function getNotasByDisciplinaId(id) {
  const [rows] = await pool.query(
    `SELECT * FROM Notas WHERE id_disciplina = ?`,
    [id]
  );
  return rows;
}

//todas as notas do aluno
export async function getNotasByAlunoId(id) {
  const [rows] = await pool.query(`SELECT * FROM Notas WHERE ra_aluno = ?`, [
    id,
  ]);
  return rows;
}

//POST
export async function addNotas(ra_aluno, id_disciplina, nota) {
  const response = await pool.query(
    `INSERT INTO Notas (ra_aluno, id_disciplina, nota) VALUES (?, ?, ?)`,
    [ra_aluno, id_disciplina, nota]
  );

  return response;
}
