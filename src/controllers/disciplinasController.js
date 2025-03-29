import * as disciplinasModel from "../models/disciplinasModel.js";

//GET
export async function getDisciplinas(req, res) {
  try {
    const response = await disciplinasModel.getDisciplinas();
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

export async function getDisciplinasBySemestre(req, res) {
  try {
    const { semestre } = req.params;
    const response = await disciplinasModel.getDisciplinasBySemestre(semestre);

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinasByArea(req, res) {
  try {
    const { area_relacionada } = req.body;
    const response = await disciplinasModel.getDisciplinasByArea(
      area_relacionada
    );

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinasById(req, res) {
  try {
    const { id } = req.params;
    const response = await disciplinasModel.getDisciplinasById(id);

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinasByProfessorRa(req, res) {
  try {
    const { ra } = req.params;
    const response = await disciplinasModel.getDisciplinasByProfessorRa(ra);

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addDisciplina(req, res) {
  try {
    const { nome, descricao, semestre, area_relacionada, ra_professor } =
      req.body;
    const response = await disciplinasModel.addDisciplina(
      nome,
      descricao,
      semestre,
      area_relacionada,
      ra_professor
    );
    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao adicionar registro" });
  }
}

//DELETE
export async function deleteDisciplina(req, res) {
  try {
    const { id } = req.params;
    const response = await disciplinasModel.deleteDisciplina(id);

    if (response.length == 0) {
      return res
        .status(404)
        .json({ mensage: err, error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}
