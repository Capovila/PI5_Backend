import * as alunosModel from "../models/alunosModel.js";

//GET
export async function getAlunos(req, res) {
  try {
    const response = await alunosModel.getAlunos();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
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
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getAlunosByTurma(req, res) {
  try {
    const { turma } = req.params;
    const response = await alunosModel.getAlunosByTurma(turma);

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
export async function addAluno(req, res) {
  try {
    const { ra_aluno, nome, id_turma } = req.body;
    const response = await alunosModel.addAlunos(ra_aluno, nome, id_turma);
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao adicionar registro" });
  }
}

//DELETE
export async function deleteAluno(req, res) {
  try {
    const { id } = req.params;
    const response = await alunosModel.deleteAluno(id);

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
export async function patchAluno(req, res) {
  try {
    const { nome, id_turma } = req.body;
    const { id } = req.params;
    const response = await alunosModel.patchAluno(id, nome, id_turma);

    if (response.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao atualizar registro" });
  }
}
