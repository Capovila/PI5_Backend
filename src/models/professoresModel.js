import { pool } from "../config/config.js";

export async function getProfessores() {
  const [rows] = await pool.query(`SELECT * FROM Professores`);
  return rows;
}

export async function getProfessoresById(id) {
  const [rows] = await pool.query(
    `SELECT * FROM Professores WHERE ra_professor = ?`,
    [id]
  );
  return rows;
}
