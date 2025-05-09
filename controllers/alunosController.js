import { supabase } from "../config/supabase.js";

//GET
export async function getAlunos(req, res) {
  try {
    const { data } = await supabase.from("alunos").select();
    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

export async function getAlunosById(req, res) {
  try {
    const { id } = req.params;
    const { data } = await supabase.from("alunos").select().eq("ra_aluno", id);

    if (data == null || data.length == 0) {
      return res
        .status(404)
        .json({ error: "Registro nao encontrado: ", response });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getAlunosByTurma(req, res) {
  try {
    const { turma } = req.params;
    const { data } = await supabase
      .from("alunos")
      .select()
      .eq("id_turma", turma);

    if (data == null || data.length == 0) {
      return res
        .status(404)
        .json({ error: "Registro nao encontrado: ", response });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getAlunosPagination(req, res) {
  try {
    const { page, limit } = req.body;

    const { data } = await supabase
      .from("alunos")
      .select()
      .range((page - 1) * limit, page * limit - 1);

    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado: ", data });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addAluno(req, res) {
  try {
    const { ra_aluno, nome, id_turma } = req.body;

    const response = await supabase.from("alunos").insert({
      ra_aluno,
      nome,
      id_turma,
    });

    if (response.status != 201) {
      return res
        .status(404)
        .json({ error: "Erro ao adicionar registro: ", response });
    }
    res.status(200).json(response.status);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao adicionar registro" });
  }
}

//DELETE
export async function deleteAluno(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase.from("alunos").delete().eq("ra_aluno", id);

    if (response.status == 409) {
      return res
        .status(409)
        .json({ error: "Erro ao deletar registro: ", response });
    }

    res.status(200).json("Registro deletado com sucesso");
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

    const response = await supabase
      .from("alunos")
      .update({
        nome,
        id_turma,
      })
      .eq("ra_aluno", id);

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao atualizar registro" });
  }
}
