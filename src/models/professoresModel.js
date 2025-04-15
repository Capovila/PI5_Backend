import { pool } from "../config/config.js";

//GET
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

export async function getProfessoresPagination(limit, page) {
  const offset = (page - 1) * limit;
  const [rows] = await pool.query(
    `SELECT * FROM Professores LIMIT ? OFFSET ?`,
    [limit, offset]
  );
  return rows;
}

//POST
export async function addProfessores(
  ra_professor,
  nome,
  email,
  senha,
  is_admin,
  is_liberado
) {
  const response = await pool.query(
    `INSERT INTO Professores (ra_professor, nome, email, senha, is_admin, is_liberado) VALUES (?,?,?,?,?,?)`,
    [ra_professor, nome, email, senha, is_admin, is_liberado]
  );

  return response;
}

//DELETE
export async function deleteProfessor(id) {
  const [rows] = await pool.query(
    `DELETE FROM Professores WHERE ra_professor = ?`,
    [id]
  );
  return rows;
}

//PATCH
export async function patchProfessor(
  nome,
  email,
  senha,
  is_admin,
  is_liberado,
  ra_professor
) {
  const response = await pool.query(
    `UPDATE Professores SET nome = ?, email = ?, senha = ?, is_admin = ?, is_liberado = ? WHERE ra_professor = ?`,
    [nome, email, senha, is_admin, is_liberado, ra_professor]
  );

  return response;
}

export async function liberarProfessor(id) {
  const response = await pool.query(
    `UPDATE Professores SET is_liberado = 1 WHERE ra_professor = ?`,
    [id]
  );

  return response;
}

export async function tornarProfessorAdmin(id) {
  const response = await pool.query(
    `UPDATE Professores SET is_admin = 1 WHERE ra_professor = ?`,
    [id]
  );

  return response;
}
export async function removerProfessorAdmin(id) {
  const response = await pool.query(
    `UPDATE Professores SET is_admin = 0 WHERE ra_professor = ?`,
    [id]
  );

  return response;
}
