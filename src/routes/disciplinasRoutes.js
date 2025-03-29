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

router.delete("/delete/:id", disciplinasController.deleteDisciplina);

router.put("/patch/:id", disciplinasController.patchDisciplina);

export default router;
