import * as professoresModel from "../models/professoresModel.js";

export async function getProfessores(req, res) {
  try {
    const response = await professoresModel.getProfessores();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar os dados " });
  }
}

export async function getProfessoresById(req, res) {
  try {
    const { id } = req.params;
    const response = await professoresModel.getProfessoresById(id);

    if (!response) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Erro ao puxar registro" });
  }
}
