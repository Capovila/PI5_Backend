import { supabase } from "../config/supabase.js";

//GET
export async function getTurmaDisciplina(req, res) {
  try {
    const { data } = await supabase.from("turma_disciplina").select();
    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

export async function getTurmasDisciplinaById(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("turma_disciplina")
      .select()
      .eq("id_turma_disciplina", id);

    if (data.length == 0 || data == null) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getTurmasByDisciplinaId(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("turma_disciplina")
      .select()
      .eq("id_disciplina", id);

    if (data.length == 0 || data == null) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinaByTurmaId(req, res) {
  try {
    const { id } = req.params;
    const { data } = await supabase
      .from("turma_disciplina")
      .select()
      .eq("id_turma", id);

    if (data.length == 0 || data == null) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addTurmaDisciplina(req, res) {
  try {
    const { id_turma, id_disciplina, taxa_aprovacao, is_concluida } = req.body;

    const response = await supabase.from("turma_disciplina").insert([
      {
        id_turma: id_turma,
        id_disciplina: id_disciplina,
        taxa_aprovacao: taxa_aprovacao,
        is_concluida: is_concluida,
      },
    ]);

    if (response.status != 201) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

//DELETE
export async function deleteTurmaDisciplina(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase
      .from("turma_disciplina")
      .delete()
      .eq("id_turma_disciplina", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao apagar registro" });
  }
}

//PATCH
export async function patchTurmaDisciplina(req, res) {
  try {
    const { id } = req.params;
    const { id_turma, id_disciplina, taxa_aprovacao, is_concluida } = req.body;

    const response = await supabase
      .from("turma_disciplina")
      .update({
        id_turma,
        id_disciplina,
        taxa_aprovacao,
        is_concluida,
      })
      .eq("id_turma_disciplina", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

export async function concluirDisciplina(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase
      .from("turma_disciplina")
      .update({
        is_concluida: true,
      })
      .eq("id_turma_disciplina", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}
