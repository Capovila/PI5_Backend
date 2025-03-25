import express from "express";
import * as turmaDisciplinaController from "../controllers/turmaDisciplinaController.js";

const router = express.Router();

router.get("/", turmaDisciplinaController.getTurmaDisciplina);
router.get("/:id", turmaDisciplinaController.getDisciplinaByTurmaId);
router.get("/turmas/:id", turmaDisciplinaController.getDisciplinaByTurmaId);
router.get(
  "/disciplinas/:id",
  turmaDisciplinaController.getTurmasByDisciplinaId
);

export default router;
