import * as alunosModel from "../models/alunosModel.js";

export async function getAlunos(req, res) {
  try {
    const response = await alunosModel.getAlunos();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar os dados" });
  }
}

export async function getAlunosById(req, res) {
  try {
    const { id } = req.params;
    const response = await alunosModel.getAlunosById(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
