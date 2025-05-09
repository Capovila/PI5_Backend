import { supabase } from "../config/supabase.js";

//GET
export async function getTurmas(req, res) {
  try {
    const { data } = await supabase.from("turmas").select();

    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

export async function getTurmasByDate(req, res) {
  try {
    const { data_inicio } = req.body;

    const { data } = await supabase
      .from("turmas")
      .select()
      .eq("data_inicio", data_inicio);

    if (data.length == 0 || data == null) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getTurmasById(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase.from("turmas").select().eq("id_turma", id);

    if (data.length == 0 || data == null) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getTurmasPagination(req, res) {
  try {
    const { page, limit } = req.body;

    const { data } = await supabase
      .from("turmas")
      .select()
      .range((page - 1) * limit, page * limit - 1);

    if (data.length == 0 || data == null) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

//POST
export async function addTurmas(req, res) {
  try {
    const { data_inicio, isgraduated } = req.body;

    const response = await supabase.from("turmas").insert({
      data_inicio,
      isgraduated,
    });

    if (response.status != 201) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

//DELETE
export async function deleteTurma(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase.from("turmas").delete().eq("id_turma", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao deletar registro" });
  }
}

//PATCh
export async function patchTurma(req, res) {
  try {
    const { id } = req.params;
    const { data_inicio, isgraduated } = req.body;

    const response = await supabase
      .from("turmas")
      .update({
        data_inicio,
        isgraduated,
      })
      .eq("id_turma", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

export async function graduateTurma(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase
      .from("turmas")
      .update({
        isgraduated: true,
      })
      .eq("id_turma", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}
