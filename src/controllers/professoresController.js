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
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getProfessoresPagination(req, res) {
  try {
    const { limit, page } = req.body;

    const response = await professoresModel.getProfessoresPagination(
      limit,
      page
    );

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
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
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}

//PATCH
export async function patchProfessor(req, res) {
  try {
    let { id } = req.params;
    let { nome, email, senha, is_admin, is_liberado } = req.body;

    console.log(id);
    const response = await professoresModel.patchProfessor(
      nome,
      email,
      senha,
      is_admin,
      is_liberado,
      id
    );

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.error(err);
    res
      .status(500)
      .json({ message: err.message, error: "Erro ao puxar os dados" });
  }
}

export async function liberarProfessor(req, res) {
  try {
    const { id } = req.params;
    const response = await professoresModel.liberarProfessor(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao liberar registro" });
  }
}

export async function tornarProfessorAdmin(req, res) {
  try {
    const { id } = req.params;
    const response = await professoresModel.tornarProfessorAdmin(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao liberar registro" });
  }
}
export async function removerProfessorAdmin(req, res) {
  try {
    const { id } = req.params;
    const response = await professoresModel.removerProfessorAdmin(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao liberar registro" });
  }
}
("");
