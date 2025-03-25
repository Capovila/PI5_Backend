import { pool } from "../config/config.js";

export async function getAlunos() {
  const [rows] = await pool.query(`SELECT * FROM Alunos`);
  return rows;
}

export async function getAlunosById(id) {
  const [rows] = await pool.query(`SELECT * FROM Alunos WHERE ra_aluno = ?`, [
    id,
  ]);
  return rows;
}
