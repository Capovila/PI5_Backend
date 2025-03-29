import * as professoresModel from "../models/professoresModel.js";

//GET
export async function getProfessores(req, res) {
  try {
    const response = await professoresModel.getProfessores();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

export async function getProfessoresById(req, res) {
  try {
    const { id } = req.params;
    const response = await professoresModel.getProfessoresById(id);

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addProfessores(req, res) {
  try {
    const { ra_professor, nome, email, senha, is_admin, is_liberado } =
      req.body;
    const response = await professoresModel.addProfessores(
      ra_professor,
      nome,
      email,
      senha,
      is_admin,
      is_liberado
    );
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

//DELETE
export async function deleteProfessor(req, res) {
  try {
    const { id } = req.params;
    const response = await professoresModel.deleteProfessor(id);

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}
