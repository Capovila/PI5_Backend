import express from "express";
import * as alunosController from "../controllers/alunosController.js";

const router = express.Router();

router.get("/", alunosController.getAlunos);
router.post("/adicionar", alunosController.addAluno);
router.get("/:id", alunosController.getAlunosById);

router.get("/turma/:turma", alunosController.getAlunosByTurma);

export default router;
