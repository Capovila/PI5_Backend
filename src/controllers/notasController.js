import * as notasModel from "../models/notasModel.js";

//GET
export async function getNotas(req, res) {
  try {
    const response = await notasModel.getNotas();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

export async function getNotasById(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.getNotasById(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getNotasByDisciplinaId(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.getNotasByDisciplinaId(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getNotasByAlunoId(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.getNotasByAlunoId(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addNotas(req, res) {
  try {
    const { ra_aluno, id_disciplina, nota } = req.body;
    const response = await notasModel.addNotas(ra_aluno, id_disciplina, nota);
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

//DELETE
export async function deleteNotas(req, res) {
  try {
    const { id } = req.params;
    const response = await notasModel.deleteNotas(id);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}
