import * as turmaDisciplinaModel from "../models/turmaDisciplinaModel.js";

export async function getTurmaDisciplina(req, res) {
  try {
    const response = await turmaDisciplinaModel.getTurmaDisciplina();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar os dados " });
  }
}

export async function getTurmasDisciplinaById(req, res) {
  try {
    const { id } = req.params;
    const response = await turmaDisciplinaModel.getTurmasDisciplinaById(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}

export async function getTurmasByDisciplinaId(req, res) {
  try {
    const { id } = req.params;
    const response = await turmaDisciplinaModel.getTurmasByDisciplinaId(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinaByTurmaId(req, res) {
  try {
    const { id } = req.params;
    const response = await turmaDisciplinaModel.getDisciplinaByTurmaId(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
