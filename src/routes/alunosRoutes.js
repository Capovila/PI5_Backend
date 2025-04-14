import express from "express";
import * as alunosController from "../controllers/alunosController.js";

const router = express.Router();

router.get("/", alunosController.getAlunos);
router.get("/pagination", alunosController.getAlunosPagination);
router.get("/:id", alunosController.getAlunosById);
router.get("/turma/:turma", alunosController.getAlunosByTurma);

router.post("/adicionar", alunosController.addAluno);

router.delete("/delete/:id", alunosController.deleteAluno);

router.put("/patch/:id", alunosController.patchAluno);

export default router;
