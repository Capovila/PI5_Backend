import { supabase } from "../config/supabase.js";

//GET
export async function getNotas(req, res) {
  try {
    const { data } = await supabase.from("notas").select("*");

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

export async function getNotasById(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("notas")
      .select("*")
      .eq("id_notas", id);

    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getNotasByDisciplinaId(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("notas")
      .select("*")
      .eq("id_disciplina", id);
    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }
    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getNotasByAlunoId(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("notas")
      .select("*")
      .eq("ra_aluno", id);
    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }
    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getNotasPagination(req, res) {
  try {
    const { limit, page } = req.body;

    const { data } = await supabase
      .from("notas")
      .select("*")
      .range((page - 1) * limit, page * limit - 1);
    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }
    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addNotas(req, res) {
  try {
    const { ra_aluno, id_disciplina, nota } = req.body;

    const response = await supabase.from("notas").insert({
      ra_aluno: ra_aluno,
      id_disciplina: id_disciplina,
      nota: nota,
    });

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
export async function deleteNotas(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase.from("notas").delete().eq("id_notas", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}

//PATCH
export async function patchNotas(req, res) {
  try {
    const { id } = req.params;
    const { ra_aluno, id_disciplina, nota } = req.body;

    const response = await supabase
      .from("notas")
      .update({
        ra_aluno: ra_aluno,
        id_disciplina: id_disciplina,
        nota: nota,
      })
      .eq("id_notas", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}
