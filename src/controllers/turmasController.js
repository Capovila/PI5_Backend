import * as turmasModel from "../models/turmasModel.js";

export async function getTurmas(req, res) {
  try {
    const turmas = await turmasModel.getTurmas();
    res.status(200).json(turmas);
  } catch (error) {
    res.status(500).json({ error: "Erro ao puxar os dados" });
  }
}

export async function getTurmasById(req, res) {
  try {
    const { id } = req.params;
    const turma = await turmasModel.getTurmaById(id);

    if (!turma) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(turma);
  } catch (error) {
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
