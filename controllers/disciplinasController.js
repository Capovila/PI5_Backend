import { supabase } from "../config/supabase.js";

//GET
export async function getDisciplinas(req, res) {
  try {
    const { data } = await supabase.from("disciplinas").select();

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados" });
  }
}

export async function getDisciplinasBySemestre(req, res) {
  try {
    const { semestre } = req.params;
    const { data } = await supabase
      .from("disciplinas")
      .select()
      .eq("semestre", semestre);

    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinasByArea(req, res) {
  try {
    const { area_relacionada } = req.body;

    const { data } = await supabase
      .from("disciplinas")
      .select()
      .eq("area_relacionada", area_relacionada);
    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinasById(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("disciplinas")
      .select()
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

export async function getDisciplinasByProfessorRa(req, res) {
  try {
    const { ra } = req.params;

    const { data } = await supabase
      .from("disciplinas")
      .select()
      .eq("ra_professor", ra);
    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }
    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getDisciplinasPagination(req, res) {
  try {
    const { limit, page } = req.body;

    const { data } = await supabase
      .from("disciplinas")
      .select()
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
export async function addDisciplina(req, res) {
  try {
    const { nome, descricao, semestre, area_relacionada, ra_professor } =
      req.body;

    const response = await supabase.from("disciplinas").insert({
      nome,
      descricao,
      semestre,
      area_relacionada,
      ra_professor,
    });

    if (response.status != 201) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

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

    const response = await supabase
      .from("disciplinas")
      .delete()
      .eq("id_disciplina", id);

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
export async function patchDisciplina(req, res) {
  try {
    const { nome, descricao, semestre, area_relacionada, ra_professor } =
      req.body;
    const { id } = req.params;

    const response = await supabase
      .from("disciplinas")
      .update({
        nome,
        descricao,
        semestre,
        area_relacionada,
        ra_professor,
      })
      .eq("id_disciplina", id);

    if (response.status != 200) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao adicionar registro" });
  }
}
