import express from "express";
import * as disciplinasController from "../controllers/disciplinasController.js";

const router = express.Router();

router.get("/", disciplinasController.getDisciplinas);
router.get("/area", disciplinasController.getDisciplinasByArea);
router.get("/pagination", disciplinasController.getDisciplinasPagination);
router.get(
  "/semestre/:semestre",
  disciplinasController.getDisciplinasBySemestre
);
router.get("/:id", disciplinasController.getDisciplinasById);
router.get("/professor/:ra", disciplinasController.getDisciplinasByProfessorRa);

router.post("/", disciplinasController.addDisciplina);

router.delete("/:id", disciplinasController.deleteDisciplina);

router.put("/:id", disciplinasController.patchDisciplina);

export default router;
