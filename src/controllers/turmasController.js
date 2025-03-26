import * as turmasModel from "../models/turmasModel.js";

export async function getTurmas(req, res) {
  try {
    const response = await turmasModel.getTurmas();
    res.status(200).json(response);
  } catch (error) {
    res.status(500).json({ error: "Erro ao puxar os dados" });
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
  } catch (error) {
    res.status(500).json({ error: "Erro ao puxar registro" });
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
  } catch (error) {
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
