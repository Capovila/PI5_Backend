import * as turmasModel from "../models/turmasModel.js";

//GET
export async function getTurmas(req, res) {
  try {
    const response = await turmasModel.getTurmas();
    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

export async function getTurmasByDate(req, res) {
  try {
    const { data_inicio } = req.body;
    const response = await turmasModel.getTurmaByDate(data_inicio);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getTurmasById(req, res) {
  try {
    const { id } = req.params;
    const response = await turmasModel.getTurmaById(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getTurmasPagination(req, res) {
  try {
    const { page, limit } = req.body;

    const response = await turmasModel.getTurmasPagination(page, limit);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addTurmas(req, res) {
  try {
    const { data_inicio, isGraduated } = req.body;
    const response = await turmasModel.addTurmas(data_inicio, isGraduated);
    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

//DELETE
export async function deleteTurma(req, res) {
  try {
    const { id } = req.params;
    const response = await turmasModel.deleteTurma(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}

//PATCh
export async function patchTurma(req, res) {
  try {
    const { id } = req.params;
    const { data_inicio, isGraduated } = req.body;
    const response = await turmasModel.patchTurma(data_inicio, isGraduated, id);
    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}
