import express from "express";
import * as notasController from "../controllers/notasController.js";

const router = express.Router();

router.get("/", notasController.getNotas);
router.get("/:id", notasController.getNotasById);
router.get("/aluno/:id", notasController.getNotasByAlunoId);
router.get("/disciplina/:id", notasController.getNotasByDisciplinaId);

export default router;
