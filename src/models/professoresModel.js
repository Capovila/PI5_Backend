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
