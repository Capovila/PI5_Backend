import express from "express";
import * as notasController from "../controllers/notasController.js";

const router = express.Router();

router.get("/", notasController.getNotas);
router.get("/:id", notasController.getNotasById);
router.get("/aluno/:id", notasController.getNotasByAlunoId);
router.get("/disciplina/:id", notasController.getNotasByDisciplinaId);

router.post("/adicionar", notasController.addNotas);

router.delete("/delete/:id", notasController.deleteNotas);

export default router;
