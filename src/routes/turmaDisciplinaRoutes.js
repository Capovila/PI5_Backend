import express from "express";
import * as turmaDisciplinaController from "../controllers/turmaDisciplinaController.js";

const router = express.Router();

router.get("/", turmaDisciplinaController.getTurmaDisciplina);
router.get("/:id", turmaDisciplinaController.getDisciplinaByTurmaId);
router.get("/turma/:id", turmaDisciplinaController.getDisciplinaByTurmaId);
router.get(
  "/disciplina/:id",
  turmaDisciplinaController.getTurmasByDisciplinaId
);

router.post("/adicionar", turmaDisciplinaController.addTurmaDisciplina);

router.delete("/delete/:id", turmaDisciplinaController.deleteTurmaDisciplina);

export default router;
