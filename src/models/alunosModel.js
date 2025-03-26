import { pool } from "../config/config.js";

//GET
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

export async function getAlunosByTurma(turma) {
  const [rows] = await pool.query(`SELECT * FROM Alunos WHERE id_turma = ?`, [
    turma,
  ]);
  return rows;
}

//POST
export async function addAlunos(ra_aluno, nome, id_turma) {
  const response = await pool.query(
    `INSERT INTO Alunos (ra_aluno, nome, id_turma) VALUES (?,?,?)`,
    [ra_aluno, nome, id_turma]
  );
  return response;
}
