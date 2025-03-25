import { pool } from "../config/config.js";

export async function getDisciplinas() {
  const [rows] = await pool.query(`SELECT * FROM Disciplinas`);
  return rows;
}

export async function getDisciplinasById(id) {
  const [rows] = await pool.query(
    `SELECT * FROM Disciplinas WHERE id_disciplina = ?`,
    [id]
  );
  return rows;
}
