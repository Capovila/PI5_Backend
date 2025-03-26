import express from "express";
import * as disciplinasController from "../controllers/disciplinasController.js";

const router = express.Router();

router.get("/", disciplinasController.getDisciplinas);
router.get("/area", disciplinasController.getDisciplinasByArea);
router.get(
  "/semestre/:semestre",
  disciplinasController.getDisciplinasBySemestre
);
router.get("/:id", disciplinasController.getDisciplinasById);
router.get("/professor/:ra", disciplinasController.getDisciplinasByProfessorRa);

router.post("/adicionar", disciplinasController.addDisciplina);

export default router;
