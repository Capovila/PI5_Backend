import * as notasModel from "../models/notasModel.js";

export async function getNotas(req, res) {
  try {
    const response = await notasModel.getNotas();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar os dados " });
  }
}

export async function getNotasById(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.getNotasById(id);

    if (!response) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}

export async function getNotasByDisciplinaId(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.getNotasByDisciplinaId(id);

    if (!response) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}

export async function getNotasByAlunoId(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.getNotasByAlunoId(id);

    if (!response) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
