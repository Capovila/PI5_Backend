import * as disciplinasModel from "../models/disciplinasModel.js";

export async function getAlunos(req, res) {
  try {
    const response = await disciplinasModel.getDisciplinas();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar os dados" });
  }
}

export async function getAlunosBySemestre(req, res) {
  try {
    const { semestre } = req.params;
    const response = await disciplinasModel.getDisciplinasBySemestre(semestre);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}

export async function getAlunosByArea(req, res) {
  try {
    const { area_relacionada } = req.body;
    const response = await disciplinasModel.getDisciplinasByArea(
      area_relacionada
    );

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}

export async function getAlunosById(req, res) {
  try {
    const { id } = req.params;
    const response = await disciplinasModel.getDisciplinasById(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
