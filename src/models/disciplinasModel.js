import { pool } from "../config/config.js";

//GET
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

export async function getDisciplinasBySemestre(semestre) {
  const [rows] = await pool.query(
    `SELECT * FROM Disciplinas WHERE semestre = ?`,
    [semestre]
  );
  return rows;
}

export async function getDisciplinasByArea(area) {
  const [rows] = await pool.query(
    `SELECT * FROM Disciplinas WHERE area_relacionada = ?`,
    [area]
  );
  return rows;
}

export async function getDisciplinasByProfessorRa(ra) {
  const [rows] = await pool.query(
    `SELECT * FROM Disciplinas WHERE ra_professor = ?`,
    [ra]
  );
  return rows;
}

//POST
export async function addDisciplina(
  nome,
  descricao,
  semestre,
  area_relacionada,
  ra_professor
) {
  const response = await pool.query(
    `INSERT INTO Disciplinas (nome, descricao, semestre, area_relacionada, ra_professor) VALUES (?,?,?,?,?)`,
    [nome, descricao, semestre, area_relacionada, ra_professor]
  );
  return response;
}
