import { pool } from "../config/config.js";

//GET
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

//POST
export async function addTurmas(data_inicio, isGraduated) {
  const response = await pool.query(
    `INSERT INTO Turmas (data_inicio, isGraduated) VALUES (?,?)`,
    [data_inicio, isGraduated]
  );
  return response;
}

//DELETE
export async function deleteTurma(id) {
  const [rows] = await pool.query(`DELETE FROM Turmas WHERE id_turma = ?`, [
    id,
  ]);
  return rows;
}

//PATCH
export async function patchTurma(data_inicio, isGraduated, id) {
  const response = await pool.query(
    `UPDATE Turmas SET data_inicio=?, isGraduated=? WHERE id_turma = ?`,
    [data_inicio, isGraduated, id]
  );
  return response;
}
