import { supabase } from "../config/supabase.js";

//GET
export async function getProfessores(req, res) {
  try {
    const { data } = await supabase.from("professores").select("*");

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

export async function getProfessoresById(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("professores")
      .select("*")
      .eq("ra_professor", id);

    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar registro" });
  }
}

export async function getProfessoresPagination(req, res) {
  try {
    const { limit, page } = req.body;

    const { data } = await supabase
      .from("professores")
      .select("*")
      .range((page - 1) * limit, page * limit - 1);

    if (data == null || data.length == 0) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(data);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

//POST
export async function addProfessores(req, res) {
  try {
    const { ra_professor, nome, email, senha, is_admin, is_liberado } =
      req.body;

    const response = await supabase.from("professores").insert([
      {
        ra_professor,
        nome,
        email,
        senha,
        is_admin,
        is_liberado,
      },
    ]);

    if (response.status != 201) {
      return res.status(404).json({ error: "Erro ao inserir o registro" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao puxar os dados " });
  }
}

//DELETE
export async function deleteProfessor(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase
      .from("professores")
      .delete()
      .eq("ra_professor", id);

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
export async function patchProfessor(req, res) {
  try {
    let { id } = req.params;
    let { nome, email, senha, is_admin, is_liberado } = req.body;

    const response = await supabase
      .from("professores")
      .update({
        nome,
        email,
        senha,
        is_admin,
        is_liberado,
      })
      .eq("ra_professor", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.error(err);
    res
      .status(500)
      .json({ message: err.message, error: "Erro ao puxar os dados" });
  }
}

export async function liberarProfessor(req, res) {
  try {
    const { id } = req.params;

    const response = await supabase
      .from("professores")
      .update({ is_liberado: true })
      .eq("ra_professor", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res.status(200).json(response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao liberar registro" });
  }
}

export async function professorAdmin(req, res) {
  try {
    const { id } = req.params;

    const { data } = await supabase
      .from("professores")
      .select("is_admin")
      .eq("ra_professor", id);

    const response = await supabase
      .from("professores")
      .update({
        is_admin: data[0].is_admin ? false : true,
      })
      .eq("ra_professor", id);

    if (response.status != 204) {
      return res.status(404).json({ error: "Registro nao encontrado" });
    }

    res
      .status(200)
      .json(
        data[0].is_admin
          ? "Professor removido dos admins"
          : "Professor adicionado aos admins"
      );
  } catch (err) {
    console.log(err);
    res.status(500).json({ mensage: err, error: "Erro ao liberar registro" });
  }
}

("");
