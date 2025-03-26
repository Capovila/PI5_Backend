import { pool } from "../config/config.js";

export async function getTurmas() {
  const [rows] = await pool.query(`SELECT * FROM Turmas`);
  return rows;
}

export async function getTurmaById(id) {
  const [rows] = await pool.query(`SELECT * FROM Turmas WHERE id_turma = ?`, [
    id,
  ]);
  return rows[0];
}

export async function getTurmaByDate(date) {
  const [rows] = await pool.query(
    `SELECT * FROM Turmas WHERE data_inicio = ?`,
    [date]
  );
  return rows;
}
